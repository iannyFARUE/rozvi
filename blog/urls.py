from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('posts/<int:pk>/clap/', views.clap_post, name='blog-post-clap'),
]