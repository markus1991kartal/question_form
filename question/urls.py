from django.urls import path
from . import views

app_name = 'question'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'), #в этой фунции первый показатель - имя в строке в браузере
                                                   # вторая - название представления, которое обрабатывает
                                                    #имя по которомы к пути обращаются
    #path('answers/<int:pk>/', views.answer, name='answers'),
]