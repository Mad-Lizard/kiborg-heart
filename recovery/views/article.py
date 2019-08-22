from recovery.models import Article
from django.views import generic
from django.utils import timezone

class ArticleListView(generic.ListView):
    model = Article
    paginate_by = 10
    context_object_name = 'articles'
    queryset = Article.objects.filter(published_at__lte=timezone.now())

    class Meta:
        app_label = 'recovery'

class ArticleDetailView (generic.DetailView):
    model = Article

    class Meta:
        app_label = 'recovery'