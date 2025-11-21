from django.http import HttpResponse
from django.shortcuts import render
from .models import Central # IMPORTAR EL MODEL 

def index(request):
    centrales = Central.objects.all()
   
    return render(request, 'central.html', {'centrales':centrales})

