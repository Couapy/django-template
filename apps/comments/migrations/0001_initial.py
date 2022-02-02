# Generated by Django 3.0.8 on 2021-03-14 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='body')),
                ('publication_date', models.DateTimeField(auto_now_add=True, verbose_name='publication date')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='lastest modification date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='author')),
                ('replies', models.ManyToManyField(blank=True, to='comments.Comment', verbose_name='replies to this comment')),
                ('user_liked', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='users that have liked this comment')),
            ],
        ),
        migrations.CreateModel(
            name='CommentZone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True, verbose_name='name')),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled')),
                ('comments', models.ManyToManyField(blank=True, to='comments.Comment', verbose_name='root comments')),
            ],
        ),
    ]
