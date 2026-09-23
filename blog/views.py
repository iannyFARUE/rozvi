from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import CommentForm, PostForm
from .models import Post

POSTS_PER_PAGE = 6


def _distinct_topics():
    return (
        Post.objects.order_by('topic')
        .values_list('topic', flat=True)
        .distinct()
    )


def home(request):
    posts_qs = Post.objects.select_related('author', 'author__profile')
    staff_picks = posts_qs.filter(featured=True)[:3]
    topics = _distinct_topics()

    paginator = Paginator(posts_qs, POSTS_PER_PAGE)
    posts = paginator.get_page(request.GET.get('page'))
    page_range = paginator.get_elided_page_range(posts.number, on_each_side=3, on_ends=1)

    context = {
        'posts': posts,
        'page_range': page_range,
        'staff_picks': staff_picks,
        'topics': topics,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')


def post_detail(request, slug):
    post = get_object_or_404(
        Post.objects.select_related('author', 'author__profile'),
        slug=slug,
    )
    comments = post.comments.filter(parent__isnull=True).select_related('author', 'author__profile')
    context = {
        'post': post,
        'comments': comments,
    }
    return render(request, 'blog/post_detail.html', context)


@login_required
@require_POST
def comment_create(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        comment.save()
    else:
        messages.error(request, 'Your comment could not be posted.')
    return redirect(post.get_absolute_url() + '#comments')


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Your story has been published.')
            return redirect('blog-home')
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form': form, 'topics': _distinct_topics()})


def _get_owned_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        raise PermissionDenied('You can only manage your own stories.')
    return post


@login_required
def post_update(request, pk):
    post = _get_owned_post(request, pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your story has been updated.')
            return redirect('blog-home')
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {'form': form, 'topics': _distinct_topics(), 'post': post})


@login_required
def post_delete(request, pk):
    post = _get_owned_post(request, pk)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Your story has been deleted.')
        return redirect('blog-home')

    return render(request, 'blog/post_confirm_delete.html', {'post': post})


@require_POST
def clap_post(request, pk):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Sign in to clap on posts.'}, status=403)
    post = get_object_or_404(Post, pk=pk)
    post.add_clap(request.user, amount=1)
    return JsonResponse({'claps_count': post.claps_count})
