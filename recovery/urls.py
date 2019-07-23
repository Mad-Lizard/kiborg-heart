from django.urls import path
from . import views

urlpatterns = [
    path('', views.AboutView.as_view(), name='about'),
    path('posts', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('athlets', views.AthletListView.as_view(), name='athlet_list'),
    path('athlet/<int:pk>/', views.AthletDetailView.as_view(), name='athlet_detail'),
    path('articles', views.ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
]
