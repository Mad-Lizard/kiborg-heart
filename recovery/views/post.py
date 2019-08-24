from recovery.models import Post
from django.views import generic

class PostListView(generic.ListView):
    class Meta:
        app_label = 'recovery'

    model = Post
    paginate_by = 10
    context_object_name = 'posts'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            posts0 = Post.objects.filter(is_published=True, is_visible=True)
            posts1 = Post.objects.filter(created_by=self.request.user.id, is_visible=False)
            posts = posts0 | posts1
            return posts
        else:
            return Post.objects.filter(is_published=True, is_visible=True)


class PostDetailView(generic.DetailView):
    model = Post

    class Meta:
        app_label = 'recovery'