from recovery.models import Post
from recovery.forms import PostCreationForm
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

class UpdatePostView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = PostCreationForm
    template_name = 'recovery/update_post.html'
    slug_url_kwarg = 'pk'
    context_object_name = 'post'

    class Meta:
        app_label = 'recovery'


    def form_valid(self, form):
        post = form.save(commit=False)
        post.created_by = self.request.user
        pk = post.pk
        db_post = self.model.objects.get(pk=pk)
        if self.request.FILES:
            image = self.request.FILES['image']
            post.image.save(image.name, image)
        if post.is_visible:
            post.is_visible = 1
        if (post.is_published == True and db_post.published_at == None):
            post.published_at = timezone.now()
            post.save()
            messages.success(self.request, 'Запись опубликована')
            return HttpResponseRedirect(reverse('update_post', kwargs={'pk': pk}))
        else:
            self.object.save()
            messages.success(self.request, 'Обновления сохранены')
            return HttpResponseRedirect(reverse('update_post', kwargs={'pk': pk}))
