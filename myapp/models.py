from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    subscribers = models.ManyToManyField(User, related_name='subscribed_topics', blank=True)

    def __str__(self) -> str:
        return f"{self.name}"

class Article(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    topics = models.ManyToManyField(Topic, related_name='articles')

    def __str__(self) -> str:
        return f"{self.name} by {self.autor.username}"

class Comment(models.Model):
    text = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.DO_NOTHING, related_name='comments')
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    article =  models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments',)

    def __str__(self) -> str:
        return f"{self.text} by {self.autor.username}"