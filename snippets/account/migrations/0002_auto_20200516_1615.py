# Generated by Django 3.0.4 on 2020-05-16 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Photo de profil'),
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default='', max_length=64, verbose_name="Nom d'utilisateur"),
        ),
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.URLField(blank=True, null=True, verbose_name='Site web'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Biographie'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
