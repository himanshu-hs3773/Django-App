from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]			#-pub_date gives descending order
    #template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)							# django shortcut to loader/httpresponse.loader

def detail(request, question_id):
    # try:
    #    question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #    raise Http404("Question does not exist")

    question = get_object_or_404(Question, pk=question_id)						# djando shortcut for try/catch

    # The get_list_or_404() function uses filter() instead of get() and raises Http404 if the list is empty
    
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    question = get_object_or_404(Question, pk=question_id)
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return HttpResponse("You're voting on question %s." % question_id)
