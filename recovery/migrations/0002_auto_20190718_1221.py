# Generated by Django 2.1 on 2019-07-18 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recovery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['published_at']},
        ),
        migrations.AlterModelOptions(
            name='athlet',
            options={'ordering': ['surname']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['published_at']},
        ),
        migrations.AddField(
            model_name='article',
            name='link_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='athlet',
            name='web_site_name',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
