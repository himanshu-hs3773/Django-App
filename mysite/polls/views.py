from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]			#-pub_date gives descending order
#     #template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     #return HttpResponse(template.render(context, request))
#     return render(request, 'polls/index.html', context)							# django shortcut to loader/httpresponse.loader

# def detail(request, question_id):
#     # try:
#     #    question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #    raise Http404("Question does not exist")

#     question = get_object_or_404(Question, pk=question_id)						# djando shortcut for try/catch / django.http Http404 module

#     # The get_list_or_404() function uses filter() instead of get() and raises Http404 if the list is empty
    
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     #response = "You're looking at the results of question %s."
#     question = get_object_or_404(Question, pk=question_id)
#     #return HttpResponse(response % question_id)
#     return render(request, 'polls/results.html', {'question': question})

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
# #     return HttpResponse("You're voting on question %s." % question_id)

#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])    # request.POST values are string
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
