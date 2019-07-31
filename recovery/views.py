from .models import Post, Athlet, Article
from django.utils import timezone
from django.views import generic
from itertools import chain
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

class AboutView(generic.TemplateView):
    template_name = 'recovery/about.html'

class SearchResultsView(generic.ListView):
    model = Post, Article, Athlet
    template_name = 'recovery/search_results.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            post_results        = Post.objects.search(query)
            article_results      = Article.objects.search(query)
            athlet_results     = Athlet.objects.search(query)

            # combine querysets
            queryset_chain = chain(
                    post_results,
                    article_results,
                    athlet_results
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs) # since qs is actually a list
            return qs
        return Post.objects.none()
