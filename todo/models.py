from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=20)


class Task(models.Model):
    content = models.TextField(max_length=100)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, none=True)
    done = models.BooleanField(default=False, null=True)
    tags = models.ManyToManyField(Tag)