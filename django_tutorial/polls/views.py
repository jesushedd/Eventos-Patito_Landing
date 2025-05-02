from django.shortcuts import render
from .models import Question, Choice
# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from . import views

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
    question_selected = get_object_or_404(Question, pk=question_id)
    response = Choice.objects.filter(question=question_selected)
    response_frmt =  "\n".join(f"{ch.choice_text} -->> {ch.votes}" for ch in response)
    #print(response_frmt)
    return HttpResponse(response_frmt)

def vote(request, question_id):
    if request.method != "POST":
        raise Http404("Invalid Method wasssa")
    question = get_object_or_404(Question,pk=question_id)
    #choice from detail.html
    try:

        id_choice_voted = request.POST['choice']
        selected_choice = Choice.objects.get(pk = id_choice_voted)
    except (KeyError, Choice.DoesNotExist):
        context = {
            "question":question,
            "error_message" : "You didn't seelcted a valid choice"
        }
        return render(request, "polls/detail.html",context)
    else: 
        selected_choice.votes += 1
        selected_choice.save()
        #Redirection returning httpREspones: cada vez en un post
        revers_ed = reverse("polls:results", args=(question_id,))
        return HttpResponseRedirect(revers_ed)