from django.conf import settings
from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
from embed_video.fields import EmbedVideoField

# Model for dairy Post
    #title
    #description
    #text
    #created_at
    #published_at

class PostableMixin(models.Model):
    class Meta:
        abstract=True
        ordering = ['published_at']

    title = models.CharField(max_length=200)
    description = models.TextField()
    text = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    video = EmbedVideoField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Article(PostableMixin):
    link = models.CharField(max_length=500, blank=True)

class Post(PostableMixin):
    mood = models.CharField(max_length=500, blank=True, null=True)

class Athlet(models.Model):
    name = models.CharField(max_length=350)
    surname = models.CharField(max_length=350)
    image = models.ImageField(upload_to='images/')
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
