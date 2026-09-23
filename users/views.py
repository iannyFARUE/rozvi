from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from blog.models import Post
from blog.views import POSTS_PER_PAGE

from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm


def register(request):
    if request.user.is_authenticated:
        return redirect('blog-home')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome to Rozvi, {user.username}! Your account has been created.')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    posts_qs = Post.objects.filter(author=request.user).select_related('author', 'author__profile')
    post_count = posts_qs.count()

    paginator = Paginator(posts_qs, POSTS_PER_PAGE)
    posts = paginator.get_page(request.GET.get('page'))
    page_range = paginator.get_elided_page_range(posts.number, on_each_side=3, on_ends=1)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'posts': posts,
        'page_range': page_range,
        'post_count': post_count,
    }
    return render(request, 'users/profile.html', context)
