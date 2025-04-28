from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Pregunta

def index(request):
    return render(request, "eventos_landing/index.html", {'preguntas_lista': Pregunta.objects.all()}) 
