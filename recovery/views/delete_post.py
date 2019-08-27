from recovery.models import Post
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

class DeletePostView(LoginRequiredMixin, generic.DeleteView):
    class Meta:
        app_label = 'recovery'

    login_url = '/users/login/'
    redirect_field_name = '/'
    model = Post
    template_name = 'recovery/confirm_delete_post.html'

    def get_success_url(self):
        pk = self.request.user.pk
        messages.error(self.request, 'Запись удалена')
        super(DeletePostView, self)
        return reverse_lazy('profile', kwargs={'pk':pk})
