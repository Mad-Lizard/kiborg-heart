from .models import Post, Athlet, Article
from django.utils import timezone
from django.views import generic, View
from django.shortcuts import render
# Create your views here.

class PostListView(generic.ListView):
    model = Post
    paginate_by = 10
    context_object_name = 'posts'
    queryset = Post.objects.filter(published_at__lte=timezone.now())

class PostDetailView(generic.DetailView):
    model = Post

class AthletListView(generic.ListView):
    model = Athlet
    paginate_by = 5
    context_object_name = 'athlets'
    queryset = Athlet.objects.filter(published_at__lte=timezone.now())

class AthletDetailView(generic.DetailView):
    model = Athlet

class ArticleListView(generic.ListView):
    model = Article
    paginate_by = 10
    context_object_name = 'articles'
    queryset = Article.objects.filter(published_at__lte=timezone.now())

class ArticleDetailView (generic.DetailView):
    model = Article

class AboutView(View):
    def get(self, request):
        return render(request, 'recovery/about.html')
