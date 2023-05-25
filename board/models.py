from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    modify_date = models.DateTimeField(null=True, blank=True)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    like_voter = models.ManyToManyField(User, related_name='like_voter_question') # 좋아요
    dislike_voter = models.ManyToManyField(User, related_name='dislike_voter_question') # 싫어요

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField()
    create_date = models.DateTimeField()
    like_voter = models.ManyToManyField(User, related_name='like_voter_answer')
    dislike_voter = models.ManyToManyField(User, related_name='dislike_voter_answer') # 싫어요

    def __str__(self):
        return self.content