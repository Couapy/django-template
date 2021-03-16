from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from comments.models import CommentZone


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    tags = models.ManyToManyField(to="Tag")
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    body = models.TextField()
    description = models.TextField()
    publication_date = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )
    modification_date = models.DateTimeField(
        auto_now=True,
        null=True,
    )
    comment_zone = models.OneToOneField(
        to="comments.CommentZone",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    available = models.BooleanField(
        verbose_name='Available for public',
        default=True,
    )

    def __str__(self):
        return self.title


class Tag(models.Model):
    """Tag model."""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Post)
def create_comment_zone(sender, instance, created, **kwargs):
    if created:
        comment_zone = CommentZone(name="Post #" + str(instance.pk))
        instance.comment_zone = comment_zone
        instance.save()
