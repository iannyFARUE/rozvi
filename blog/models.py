import random

from django.conf import settings
from django.db import models, transaction
from django.db.models import F
from django.utils import timezone
from django.utils.text import Truncator, slugify

AVATAR_COLORS = [
    'bg-emerald-600',
    'bg-indigo-600',
    'bg-rose-600',
    'bg-amber-600',
    'bg-sky-600',
    'bg-violet-600',
]


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    bio = models.CharField(max_length=300, blank=True)
    avatar_color = models.CharField(max_length=20, choices=[(c, c) for c in AVATAR_COLORS], blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

    def save(self, *args, **kwargs):
        if not self.avatar_color:
            self.avatar_color = random.choice(AVATAR_COLORS)
        super().save(*args, **kwargs)

    @property
    def display_name(self):
        return self.user.get_full_name() or self.user.username

    @property
    def initials(self):
        parts = self.display_name.split()[:2]
        return ''.join(part[0] for part in parts).upper()


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    topic = models.CharField(max_length=100, db_index=True)
    excerpt = models.CharField(max_length=300, blank=True)
    content = models.TextField()
    read_time = models.PositiveSmallIntegerField(
        default=0, help_text='Estimated reading time in minutes; auto-calculated if left blank.'
    )
    claps_count = models.PositiveIntegerField(default=0, editable=False)
    featured = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._build_unique_slug()
        if not self.excerpt:
            self.excerpt = Truncator(self.content).words(30)
        if not self.read_time:
            word_count = len(self.content.split())
            self.read_time = max(1, round(word_count / 200))
        super().save(*args, **kwargs)

    def _build_unique_slug(self):
        base_slug = slugify(self.title)[:200] or 'post'
        slug = base_slug
        suffix = 1
        while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            suffix += 1
            slug = f'{base_slug}-{suffix}'
        return slug

    @property
    def comment_count(self):
        return self.comments.count()

    def add_clap(self, user, amount=1):
        """Record `amount` claps from `user`, capped per user, and keep claps_count in sync."""
        if amount < 1:
            raise ValueError('amount must be at least 1')
        with transaction.atomic():
            clap, _ = Clap.objects.select_for_update().get_or_create(post=self, user=user)
            granted = min(amount, Clap.MAX_CLAPS_PER_USER - clap.count)
            if granted <= 0:
                return clap
            clap.count += granted
            clap.save(update_fields=['count', 'updated_at'])
            Post.objects.filter(pk=self.pk).update(claps_count=F('claps_count') + granted)
            self.claps_count += granted
        return clap


class Clap(models.Model):
    MAX_CLAPS_PER_USER = 50

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='claps')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='claps')
    count = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['post', 'user'], name='one_clap_row_per_user_per_post'),
        ]
        ordering = ['-updated_at']

    def __str__(self):
        return f'{self.user} clapped {self.count}x on "{self.post}"'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    body = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'Comment by {self.author} on "{self.post}"'
