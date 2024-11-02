from django.contrib import admin
from .models import Student,Exam,Result,Question

# Register your models here.

admin.site.register(Student)
admin.site.register(Question)
admin.site.register(Exam)
admin.site.register(Result)