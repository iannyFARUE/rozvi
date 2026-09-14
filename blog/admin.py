from django.contrib import admin
from django.utils.text import Truncator

from .models import Clap, Comment, Post, Profile


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ('author', 'body', 'is_approved', 'created_at')
    readonly_fields = ('created_at',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'topic', 'featured', 'claps_count', 'date_posted')
    list_filter = ('topic', 'featured', 'date_posted')
    search_fields = ('title', 'excerpt', 'content', 'author__username')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('claps_count',)
    date_hierarchy = 'date_posted'
    inlines = [CommentInline]


@admin.register(Clap)
class ClapAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'count', 'updated_at')
    list_filter = ('updated_at',)
    search_fields = ('post__title', 'user__username')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'short_body', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'created_at')
    search_fields = ('body', 'author__username', 'post__title')

    def short_body(self, obj):
        return Truncator(obj.body).chars(60)

    short_body.short_description = 'Comment'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar_color')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')
