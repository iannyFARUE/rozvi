from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('posts/new/', views.post_create, name='blog-post-create'),
    path('posts/<int:pk>/edit/', views.post_update, name='blog-post-edit'),
    path('posts/<int:pk>/clap/', views.clap_post, name='blog-post-clap'),
]