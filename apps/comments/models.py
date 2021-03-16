from django.db import models
from django.conf import settings

class CommentZone(models.Model):
    """Represents a comment zone."""
    name = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name="name",
    )
    comments = models.ManyToManyField(
        to="Comment",
        blank=True,
        verbose_name="root comments",
    )
    enabled = models.BooleanField(
        default=True,
        verbose_name="enabled",
    )

    def __str__(self):
        if self.name is None or len(self.name) == 0:
            return "CommentZone n°" + str(self.pk)
        return self.name
    


class Comment(models.Model):
    """Represent a comment."""
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='+',
        verbose_name="author",
    )
    replies = models.ManyToManyField(
        to="Comment",
        blank=True,
        verbose_name="replies to this comment",
    )
    body = models.TextField(
        verbose_name="body",
    )
    publication_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="publication date",
    )
    modification_date = models.DateTimeField(
        auto_now=True,
        verbose_name="lastest modification date",
    )
    user_liked = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        blank=True,
        verbose_name="users that have liked this comment",
    )

    @property
    def edited(self):
        """Indicates if the comment has been edited."""
        return self.publication_date != self.modification_date

    def __str__(self):
        """Display a part of the body."""
        return self.body[:150]
    
