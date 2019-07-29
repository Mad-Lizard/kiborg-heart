from django.conf import settings
from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
from embed_video.fields import EmbedVideoField
from sorl.thumbnail import ImageField
from django.db.models import Q

class PostableMixinManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) |
                         Q(description__icontains=query)|
                         Q(text__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()
        return qs

class PostableMixin(models.Model):
    class Meta:
        abstract=True
        ordering = ['published_at']

    title = models.CharField(max_length=200)
    description = models.TextField()
    text = models.TextField()
    image = ImageField(upload_to='images/', default='images/default.jpg', blank=True)
    video = EmbedVideoField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)

    objects = PostableMixinManager()

    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Article(PostableMixin):
    link = models.CharField(max_length=500, blank=True)
    link_name = models.CharField(max_length=150, blank=True)

class Post(PostableMixin):
    mood = models.CharField(max_length=500, blank=True, null=True)

class AthletManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(name__icontains=query) |
                         Q(surname__icontains=query) |
                         Q(sport__icontains=query) |
                         Q(country__icontains=query) |
                         Q(diagnosis__icontains=query) |
                         Q(surgery__icontains=query) |
                         Q(description__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()
        return qs

class Athlet(models.Model):
    name = models.CharField(max_length=350)
    surname = models.CharField(max_length=350)
    image = ImageField(upload_to='images/', default='images/default.jpg')
    web_site = models.CharField(max_length=500, blank=True)
    web_site_name = models.CharField(max_length=150, blank=True)
    e_mail = models.EmailField(max_length=254, blank=True)
    date_of_birth = models.IntegerField(blank=True, null=True)
    date_of_dearth = models.IntegerField(blank=True, null=True)
    country = CountryField(blank=True, null=True)
    sport = models.CharField(max_length=500)
    diagnosis = models.CharField(max_length=500)
    surgery = models.CharField(max_length=500, blank=True)
    date_of_surgery = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    video = EmbedVideoField(blank=True)
    published_at = models.DateTimeField(blank=True, null=True)

    objects = AthletManager()

    def __str__(self):
        return self.name + ' ' + self.surname

    @property
    def date(self):
        if self.date_of_dearth == None:
            return 'настоящее время'
        else:
            return self.date_of_dearth

    class Meta:
        ordering = ['surname']
