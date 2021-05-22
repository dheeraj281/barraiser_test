from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.generic import CreateView
from .forms import submitForm
from .models import Quiz, QuizProfile, AppUser
from rest_framework.views import APIView

# Create your views here.

def index(request):
    return HttpResponse("Hello")

def seeAllQuestion(request):
    if request.method == "GET":
        allQuiz = Quiz.objects.all()
        quiznames = [{quiz.id : quiz.quizName} for quiz in allQuiz]
        return JsonResponse(quiznames,safe=False,status=200)

def submitQuiz(request):

    if request.method == "POST":
        username = request.POST["participant"]
        user = AppUser.object.get(name=username)
        quizName =  request.POST["quizname"]
        quiz = Quiz.objects.get(quizName=quizName)
        QuizProfile.objects.create(participant=user,Quizname=quiz)
        return HttpResponse("Submitted", status=201)




