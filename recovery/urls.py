from django.urls import path
from . import views
#from django.conf.urls.static import static
#from django.conf import settings

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('athlets', views.AthletListView.as_view(), name='athlet_list'),
    path('athlet/<int:pk>/', views.AthletDetailView.as_view(), name='athlet_detail'),
    path('articles', views.ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
]

#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
