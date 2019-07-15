from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Athlet, Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#import datetime
from django.utils import timezone
from django.views import generic
# Create your views here.

class PostListView(generic.ListView):
    model = Post
    paginate_by = 3
    context_object_name = 'posts'
    queryset = Post.objects.filter(published_at__lte=timezone.now())

class PostDetailView(generic.DetailView):
    model = Post

#def post_detail(request, pk):
#    post = get_object_or_404(Post, pk=pk)
#    return render(request, 'recovery/post_detail.html', {'post':post})

class AthletListView(generic.ListView):
    model = Athlet
    paginate_by = 10
    context_object_name = 'athlets'
    queryset = Athlet.objects.filter(published_at__lte=timezone.now())

#def athlet_list(request):
#    page = request.GET.get('page', 1)
#    paginator = Paginator(athlets_list, 3)
#    try:
#        athlets = paginator.page(page)
#    except PageNotAnInteger:
#        athlets = paginator.page(1)
#    except EmptyPage:
#        athlets = paginator.page(paginator.num_pages)
#    return render(request, 'recovery/athlet_list.html', {'athlets':athlets})

#def athlet_detail(request, pk):
#    athlet = get_object_or_404(Athlet, pk=pk)
#    athlet.date_of_dearth = athlet.date()
#    return render(request, 'recovery/athlet_detail.html', {'athlet':athlet})

class AthletDetailView(generic.DetailView):
    model = Athlet

class ArticleListView(generic.ListView):
    model = Article
    paginate_by = 10
    context_object_name = 'articles'
    queryset = Article.objects.filter(published_at__lte=timezone.now())

#def article_list(request):
#    articles_list = Article.objects.filter(published_at__lte=timezone.now()).order_by('published_at')
#    page = request.GET.get('page', 1)

#    paginator = Paginator(articles_list, 10)
#    try:
#        articles = paginator.page(page)
#    except PageNotAnInteger:
#        articles = paginator.page(1)
#    except EmptyPage:
#        articles = paginator.page(paginator.num_pages)
#    return render(request, 'recovery/article_list.html', {'articles':articles})

#def article_detail(request, pk):
#    article = get_object_or_404(Article, pk=pk)
#    return render(request, 'recovery/article_detail.html', {'article':article})

class ArticleDetailView (generic.DetailView):
    model = Article
