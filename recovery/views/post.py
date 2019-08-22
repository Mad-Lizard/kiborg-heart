from recovery.models import Post
from django.utils import timezone
from django.views import generic

class PostListView(generic.ListView):
    model = Post
    paginate_by = 10
    context_object_name = 'posts'
    queryset = Post.objects.filter(published_at__lte=timezone.now())

    class Meta:
        app_label = 'recovery'

class PostDetailView(generic.DetailView):
    model = Post

    class Meta:
        app_label = 'recovery'