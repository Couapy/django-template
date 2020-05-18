from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    username = models.CharField(
        verbose_name="Nom d'utilisateur",
        max_length=64,
        default="",
    )
    bio = models.TextField(
        verbose_name="Biographie",
        max_length=500,
        blank=True,
        null=True,
    )
    website = models.URLField(
        verbose_name="Site web",
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        verbose_name="Photo de profil",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.user.__str__()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
