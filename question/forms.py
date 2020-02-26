from django import forms
from .models import Answer, Question


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('question_text',) # здесь мы отмечаем необходимые поля из формы, чтобы передавать
                                    #их во вьюшку и там обрабатывать


