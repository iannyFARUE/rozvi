from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import PostForm
from .models import Post


def _distinct_topics():
    return (
        Post.objects.order_by('topic')
        .values_list('topic', flat=True)
        .distinct()
    )


def home(request):
    posts = Post.objects.select_related('author', 'author__profile')
    staff_picks = posts.filter(featured=True)[:3]
    topics = _distinct_topics()
    context = {
        'posts': posts,
        'staff_picks': staff_picks,
        'topics': topics,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')


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


@require_POST
def clap_post(request, pk):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Sign in to clap on posts.'}, status=403)
    post = get_object_or_404(Post, pk=pk)
    post.add_clap(request.user, amount=1)
    return JsonResponse({'claps_count': post.claps_count})
