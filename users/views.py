from .forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from recovery.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

class SignUp(generic.View):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class Profile(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'registration/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = context['user']
        user_posts = Post.objects.filter(created_by=user).order_by('-created_at')
        context = {'user':user, 'user_posts':user_posts}
        return context


