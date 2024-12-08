from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import Student,Result,Exam,Question
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.utils import timezone
from datetime import timedelta,datetime
import math
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator

# Create your views here.

@login_required(login_url='login')
def home(request):
    user = request.user
    if Student.objects.filter(student=request.user,clas='JSS1'):
        exam = Exam.objects.filter(clas='JSS1')
        clas = 'JSS1'
    else:
        if Student.objects.filter(student=request.user,clas='JSS2'):
            exam = Exam.objects.filter(clas='JSS2')
            clas = 'JSS2'
        else:
            if Student.objects.filter(student=request.user,clas='JSS3'):
                exam = Exam.objects.filter(clas='JSS3')
                clas = 'JSS3'
            else:
                if Student.objects.filter(student=request.user,clas='SSS1'):
                    exam = Exam.objects.filter(clas='SSS1')
                    clas = 'SSS1'
                else:
                    if Student.objects.filter(student=user,clas='SSS2'):
                        exam = Exam.objects.filter(clas='SSS2')
                        clas = 'SSS2'
                    else:
                        if Student.objects.filter(student=request.user,clas='SSS3'):
                            exam = Exam.objects.filter(clas='SSS3')
                            clas = 'SSS3'
                        else:
                            return render(request, 'home.html',{'exam':exam,'clas':clas})
    return render(request, 'home.html',{'exam':exam,'clas':clas})

@login_required(login_url='login')
def preview(request,pk):
    exam = Exam.objects.filter(id=pk)
    for exam in exam:
        end = exam.duration / 60
    return render(request, 'preview.html',{'exam':exam,'end':end})

@login_required(login_url='login')
def examination(request,pk):
    exam = Exam.objects.get(id=pk)
    p = Paginator(Question.objects.filter(exam=exam), 1)
    page = request.GET.get('page')
    exam_p = p.get_page(page)
    
    current_time = timezone.now()
    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=exam.duration)
    if request.method == 'POST':
        score = request.POST.get('score')#.value()
        id = exam.id
        answer = Result(student=request.user,score=score,exam=exam)
        answer.save()
        return redirect('result',pk=id)
        
    else:
        return render(request, 'exam.html',{'exam':exam,'current_time':current_time,'end_time':end_time.isoformat(),'exam_p':exam_p})

@login_required(login_url='login')
def result(request,pk):
    exam = Exam.objects.get(id=pk)
    result = Result.objects.filter(exam=exam,student=request.user).last()
    total_question = exam.total_question
    percentage = result.score/total_question * 100
    percent = math.ceil(percentage)
    you_failed = total_question - result.score
    return render(request, 'result.html',{'result':result,'percentage':percent,'total_question':total_question,'you_failed':you_failed,'exam':exam})

def signup(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        clas = request.POST['class']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already used')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password)
                student = Student(clas=clas,student=user)
                user.save();
                student.save();
                return redirect('login')
        else:
            messages.info(request, 'password not the same')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
    
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')