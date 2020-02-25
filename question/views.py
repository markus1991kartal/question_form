from django.shortcuts import render, get_object_or_404, HttpResponse

from .models import Question


def index(request):
    questions_list = Question.objects.all()
    return render(request, 'question/index.html', {"questions_list": questions_list})


def detail(request, pk): #принимает запрос и объект первичного ключа
    question = get_object_or_404(Question, pk=pk) #выдает передает первичный ключ объекта в рендер или 404
    return render(request, 'question/detail.html', {"question": question}) # возвращает запрос в темплейт