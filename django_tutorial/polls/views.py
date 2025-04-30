from django.shortcuts import render
from .models import Question, Choice
# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render

#for votes
from django.urls import reverse


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question" : question
    }
    
    return render(request, "polls/detail.html", context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    if request.method != "POST":
        raise Http404("Invalid Method")
    question = get_object_or_404(pk=question_id)
    #choice from detail.html
    try:

        id_choice_voted = request.POST['choice']
        selected_choice = Choice.objects.get(pk = id_choice_voted)
    except (KeyError, Choice.DoesNotExist):
        context = {
            "question":question,
            "error_mesage" : "You didn't seelcted a valid choice"
        }

    
    



    return HttpResponse("You're voting on question %s.  , choide id = %s" % (question_id, id_choice_voted))
