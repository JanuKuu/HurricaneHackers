from django.shortcuts import render

from .models import Question, Answer

#Get questions and display them
def index(request):
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'hurricanedonate/index.html')
