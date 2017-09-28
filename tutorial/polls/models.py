from datetime import timedelta

from django.db import models

# Create your models here.
from django.utils import timezone

'''
class Question
    설문조사 질문
    title = 설문조사 제목
    published_date =

    __str__
    print(Question instance)
        설문좌 {{ 제목 }}

class Choice
    -> 선택
    question = 해당 설문조사
    title = 선택지 제목
    votes = 선택 횟수  = (IntegerField)

    __str__
    print(Choice instance)
        설문조사 {{설문조사의 제목}} - 선택지 {{제목}}
'''


class Question(models.Model):
    title = models.CharField(max_length=50)
    published_date = models.DateTimeField(blank=True, null=True)

    def is_recently(self):
        return bool(self.published_date) and timezone.now() - self.published_date <= timedelta(days=7)
# None은 None이므로 bool값을 반환받으려면 bool()로 감싸자...
    def __str__(self):
        return ('설문조사 : {}'.format(self.title))


class Choice(models.Model):
    question = models.ForeignKey(Question)  # Question 클래스가 여러 Choice와 연결 다대일 관계
    title = models.CharField(max_length=50)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return ('{} - 선택지 : {}'.format(self.question, self.title))
