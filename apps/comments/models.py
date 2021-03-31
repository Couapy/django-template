from django.conf import settings
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver


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

    def reply(self, comment):
        """Reply to this comment."""
        self.replies.add(comment)

    def toggle_like(self, user):
        """
        Toggle like of user on this comment.
        Return True if the user is currently liking the comment.
        """
        if user is None:
            return False

        if user in self.user_liked.all():
            self.user_liked.remove(user)
            return False
        else:
            self.user_liked.add(user)
            return True

    def delete(self, *args, **kwargs):
        models.Model.delete(self, *args, **kwargs)
        for reply in self.replies.all():
            reply.delete()

    def __str__(self):
        """Display a part of the body."""
        return self.body[:150]
    

@receiver(pre_delete, sender=Comment)
def pre_delete_story(sender, instance, **kwargs):
    for reply in instance.replies.all():
        reply.delete()
