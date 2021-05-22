import datetime

from django.db import models



class AppUser(models.Model):
    name = models.CharField(max_length=30)


class Quiz(models.Model):
    quizName = models.CharField(max_length=30)


class Questions(models.Model):
    toQuiz = models.ManyToManyField(Quiz)
    question_name = models.TextField()

class Options(models.Model):
    forQuestion = models.ForeignKey(Questions,on_delete=models.CASCADE)
    option = models.TextField()
    is_Right = models.BooleanField()


class QuizProfile(models.Model):
    participant = models.ForeignKey(AppUser,on_delete=models.SET_NULL, null=True)
    Quizname = models.ForeignKey(Quiz, on_delete=models.SET_NULL, null=True)
    submitted_at = models.DateTimeField(datetime.datetime.now())

