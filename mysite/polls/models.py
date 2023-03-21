import datetime

from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    # 문자열은 해당 필드를 admin page 에서 나타내기 쉽게 해준다.
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    # 새로 추가한 부분 -> 최종 수정 시간을 나타낸다,
    modified_date = models.DateTimeField('date last modified', auto_now=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
