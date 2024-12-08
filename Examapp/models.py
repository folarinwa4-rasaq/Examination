from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

SUBJEECT_CHOICES = [
    ('mathematics','mathematics'),
    ('english','english'),
    ('physics','physics'),
    ('chemistry','chemistry'),
    ('biology','biology'),
    ('geography','geography'),
    ('further-mathematics','further-mathematics'),
    ('economics','economics'),
    ('agric','agric'),
    ('civic','civic'),
    ('marketing','marketing'),
    ('crs','crs'),
    ('government','government'),
    ('account','account'),
    ('commerce','commerce'),
    ('literature','literature'),
    ('yoruba','yoruba'),
    ('business-studies','business-studies'),
    ('basic-science','basic-science'),
    ('basic-technology','basic-technology'),
    ('p.h.e','p.h.e'),
    ('music','music'),
    ('french','french'),
    ('home-economics','home-economics'),
    ('c.c.a','c.c.a'),
    ('social-studies','social-studies'),
    ('security-education','security-education'),
    ('history','history'),
]

CLASS_CHIOCE = [
    ('JSS1','JSS1'),
    ('JSS2','JSS2'),
    ('JSS3','JSS3'),
    ('SSS1','SSS1'),
    ('SSS2','SSS2'),
    ('SSS3','SSS3')
]

class Student(models.Model):
    clas = models.CharField(max_length=50,choices=CLASS_CHIOCE)
    student = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.student.username + ' ' + self.clas

class Exam(models.Model):
    subject = models.CharField(max_length=50,choices=SUBJEECT_CHOICES)
    description = models.TextField(max_length=125)
    title = models.CharField(max_length=50)
    duration = models.FloatField(default=120)
    total_question = models.IntegerField(default=60)
    clas = models.CharField(max_length=200,choices=CLASS_CHIOCE)

    def __str__(self):
        return self.clas + ' ' + self.title

class Question(models.Model):
    question = models.TextField()
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()
    solution = models.TextField()
    subject = models.CharField(max_length=1000000,choices=SUBJEECT_CHOICES)
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)

    def __str__(self):
        return self.exam.clas + ' ' +  self.exam.title

class Result(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.student.username #+ ' ' , self.score