from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Athlet, Article

admin.site.register(Post, SummernoteModelAdmin)
admin.site.register(Athlet, SummernoteModelAdmin)
admin.site.register(Article, SummernoteModelAdmin)
