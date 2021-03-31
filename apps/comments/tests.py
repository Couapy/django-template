from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse

from .models import Comment


class CommentTestCase(TestCase):
    """Tests for comment model."""

    def setUp(self):
        self.user = User.objects.create(username="usertest")

    def test_create_comment(self):
        """Create comment."""
        self.assertTrue(True)

    def test_edit_comment(self):
        """Edit comment."""
        self.assertTrue(True)

    def test_like_comment(self):
        """Like comment."""
        comment = Comment.objects.create(body="my super comment", author=self.user)
        self.assertTrue(comment.toggle_like(self.user))
        self.assertIn(self.user, comment.user_liked.all())
        self.assertFalse(comment.toggle_like(self.user))
        self.assertNotIn(self.user, comment.user_liked.all())

    def test_delete_comment(self):
        """Delete comment and his replies."""
        comment = Comment.objects.create(body="my super comment", author=self.user)
        reply = Comment.objects.create(body="yeahhh", author=self.user)
        comment.replies.add(reply)
        comment.delete()
        self.assertFalse(Comment.objects.filter(pk=comment.pk).exists())
        self.assertFalse(Comment.objects.filter(pk=reply.pk).exists())
