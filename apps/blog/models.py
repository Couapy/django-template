from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title
    slug
    tags
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    body
    description
    posted_date = models.DateTimeField(auto_now_add=True)
    reading_time = models.IntegerField(default=5)
    # comments

    def __str__(self):
        return self.title
    

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.value