from django.db import models
from datetime import datetime,timedelta
from django.utils import timezone

# Create your models here.

class quiz(models.Model):
    name = models.CharField(max_length=100,blank=False)
    created_by = models.CharField(max_length=200)
    date_of_starting = models.DateField(default=timezone.now)
    date_of_ending = models.DateField(default=timezone.now)
    no_of_questions = models.IntegerField(blank=False)
    duration = models.IntegerField(default=180)
    time_of_starting = models.TimeField(default=datetime.now()+timedelta(hours=1))
    time_of_ending = models.TimeField(default=datetime.now()+timedelta(hours=4))

    class Meta:
        verbose_name = 'quiz'
        verbose_name_plural = 'quizzes'

    def __str__(self):
        return "{} by {}".format(self.name,self.created_by)
        

class question(models.Model):
    quiz = models.ForeignKey(quiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=200)
    a = models.CharField(max_length=200)
    b = models.CharField(max_length=200)
    c = models.CharField(max_length=200)
    d = models.CharField(max_length=200)

    def __str__(self):
           return "{} {}".format(self.quiz.name, self.question)
