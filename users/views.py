from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import UserRegisterForm


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
