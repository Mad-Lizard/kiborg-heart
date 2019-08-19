from .models import Post, Athlet, Article
from .forms import PostCreationForm
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.db import IntegrityError
from django.views import generic
from itertools import chain
from django.urls import reverse
from django.contrib import messages
#from django.contrib.auth.mixins import LoginRequireMixin TODO

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
            post_results = Post.objects.search(query)
            article_results = Article.objects.search(query)
            athlet_results = Athlet.objects.search(query)

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

class AddPostView(generic.edit.CreateView):
    model = Post
    form_class = PostCreationForm
    template_name = 'recovery/add_post.html'

    def get_success_url(self, pk):
        return reverse('post_detail', kwargs={'pk': pk})

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
        if self.object.is_visible:
            self.object.is_visible = 1
        if self.object.is_published == True:
            self.object.published_at = timezone.now()
            self.object.save()
            pk = self.object.pk
            messages.success(self.request, 'Запись опубликована')
            return HttpResponseRedirect(self.get_success_url(pk))
        else:
            self.object.save()
            messages.success(self.request, 'Запись сохранена')
            return render(self.request, 'recovery/add_post.html', {'form':form})

    def form_invalid(self, form):
        messages.error(self.request, 'Не удалось сохранить запись')
        return render(self.request, 'recovery/add_post.html', {'form':form})


