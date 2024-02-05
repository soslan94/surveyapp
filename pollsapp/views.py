from django.shortcuts import render
from django.views.generic import ListView

from .models import Question, Survey


class SurveyList(ListView):
    """List of surveys"""
    model = Survey
    context_object_name = 'surveys'
    template_name = 'pollsapp/index.html'


def vote(request, pk):
    """Answering a certain question"""
    question = Question.objects.get(id=pk)
    options = question.choices.all()

    return render(request, 'pollsapp/vote.html', {'question': question, 'options': options})


def result(request, pk):
    """Counts votes"""

    question = Question.objects.get(id=pk)
    options = question.choices.all()
    if request.method == 'POST':
        inputvalue = request.POST['choice']
        selection_option = options.get(id=inputvalue)
        selection_option.vote += 1
        selection_option.save()
    return render(request, 'pollsapp/result.html', {'question': question, 'options': options})