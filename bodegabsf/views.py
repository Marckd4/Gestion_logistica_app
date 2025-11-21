
from django.http import HttpResponse
from django.shortcuts import render
from .models import Bsf  # importar el modelo

def data(request):
    bsfs = Bsf.objects.all()
    return render(request, 'index.html', {'bsfs': bsfs})
