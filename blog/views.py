from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST

from .models import Post


def home(request):
    posts = Post.objects.select_related('author', 'author__profile')
    staff_picks = posts.filter(featured=True)[:3]
    topics = (
        Post.objects.order_by('topic')
        .values_list('topic', flat=True)
        .distinct()
    )
    context = {
        'posts': posts,
        'staff_picks': staff_picks,
        'topics': topics,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')


@require_POST
def clap_post(request, pk):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Sign in to clap on posts.'}, status=403)
    post = get_object_or_404(Post, pk=pk)
    post.add_clap(request.user, amount=1)
    return JsonResponse({'claps_count': post.claps_count})
