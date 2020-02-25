from django.shortcuts import render, get_object_or_404, HttpResponse, redirect

from .models import Question, Answer
from .forms import QuestionForm


def index(request):
    questions_list = Question.objects.all()
    if request.method == 'POST':            #здесь мы задаем API метод
        form = QuestionForm(request.POST)   #здесь создаем объект в который передается запрос из формы
        question = form.save(commit=False)  #здесь объект question получает содержимое заполненной формы
        question.save()                     # ORM сохраняет в базу данных
        return redirect('question:index')   # ссыла на страницу где идет возвращение функции questio_list
    else:
        form = QuestionForm()               # пустая форма
    return render(request, 'question/index.html', {"questions_list": questions_list,
                                                   "form": form}) #передаем объект формы в шаблон(template)



def detail(request, pk): #принимает запрос и объект первичного ключа
    question = get_object_or_404(Question, pk=pk) #выдает передает первичный ключ объекта в рендер или 404
    return render(request, 'question/detail.html', {"question": question}) # возвращает запрос в темплейт


#def answer(request, pk):
#
#    if request.method == 'POST':
#        form = AnswerForm(request.POST)
#        answer = form.save(commit=False)
#        return redirect('question:answers', pk=answer.pk)
#    else:
#        form=AnswerForm()
#    return render(request, 'question/answer.html', {'form': form})