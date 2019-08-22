from django.contrib.auth import get_user_model
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
        constraints = [
            models.UniqueConstraint(fields=['title', 'created_by'], name = 'уникальная запись')
            ]


    title = models.CharField('заголовок', max_length=100, blank=False, null=False)
    description = models.TextField('описание', max_length=1000)
    text = models.TextField('текст')
    image = models.ImageField('изображение', upload_to='images/', default='images/default.jpg', blank=True)
    image_name = models.CharField('подпись к изображению', max_length=100, default='', blank=True)
    video = EmbedVideoField('ссылка на видео', blank=True, null=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField('публиковать', default=False)
    published_at = models.DateTimeField(blank=True, null=True)

    objects = PostableMixinManager()

    @property
    def publish(self):
        if self.published_at == True:
            self.published_at = timezone.now()
        else:
            self.published_at = ''
        return self.published_at


    def __str__(self):
        return self.title


class Article(PostableMixin):
    link = models.CharField('ссылка на первоисточник', max_length=500, blank=True)
    link_name = models.CharField('название ссылки', max_length=150, blank=True)

class Post(PostableMixin):
    is_visible = models.BooleanField('открытый доступ', default=False)


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
    name = models.CharField('имя', max_length=350)
    surname = models.CharField('фамилия', max_length=350)
    image = ImageField('изображение', upload_to='images/', default='images/default.jpg')
    web_site = models.CharField('ссылка на сайт', max_length=500, blank=True)
    web_site_name = models.CharField('название сайта', max_length=150, blank=True)
    e_mail = models.EmailField('email', max_length=254, blank=True)
    date_of_birth = models.IntegerField('дата рождения', blank=True, null=True)
    date_of_dearth = models.IntegerField('дата смерти', blank=True, null=True)
    country = CountryField('страна', blank=True, null=True)
    sport = models.CharField('вид активности', max_length=500)
    diagnosis = models.CharField('диагноз', max_length=500)
    surgery = models.CharField('выполненная операция', max_length=500, blank=True)
    date_of_surgery = models.CharField('дата проведения операции', max_length=250, blank=True, null=True)
    description = models.TextField('описание', blank=True, null=True)
    text = models.TextField('текст', blank=True, null=True)
    video = EmbedVideoField('ссылка на видео', blank=True)
    published_at = models.DateTimeField('публиковать', blank=True, null=True)

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
