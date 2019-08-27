from recovery.models import Post
from recovery.forms import PostCreationForm
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db import IntegrityError
from django.views import generic
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

class AddPostView(LoginRequiredMixin, generic.edit.CreateView):
    login_url = '/users/login/'
    redirect_field_name = '/'
    model = Post
    form_class = PostCreationForm
    template_name = 'recovery/add_post.html'

    class Meta:
        app_label = 'recovery'

    def get_success_publish_url(self, pk):
        return reverse('post_detail', kwargs={'pk': pk})

    def get_success_save_url(self, pk):
        return reverse('profile', kwargs={'pk': pk})

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return render(request, 'recovery/add_post.html', {'form':form})

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        try:
            form.is_valid()
            return self.form_valid(form)
        except IntegrityError as e:
            messages.error(self.request, 'Не уникальный заголовок записи.')
            return render(self.request, 'recovery/add_post.html', {'form':form,})
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.created_at = timezone.now()
        if self.request.FILES:
            image = self.request.FILES['image']
            self.object.image.save(image.name, image)
        if self.object.is_visible:
            self.object.is_visible = 1
        if self.object.is_published == True:
            self.object.published_at = timezone.now()
            self.object.save()
            pk = self.object.pk
            messages.success(self.request, 'Запись опубликована')
            return HttpResponseRedirect(self.get_success_publish_url(pk))
        else:
            self.object.save()
            pk = self.request.user.pk
            messages.success(self.request, 'Запись сохранена')
            return HttpResponseRedirect(self.get_success_save_url(pk))

    def form_invalid(self, form):
        messages.error(self.request, 'Не удалось сохранить запись')
        return render(self.request, 'recovery/add_post.html', {'form':form})