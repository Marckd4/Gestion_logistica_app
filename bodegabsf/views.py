
from django.http import HttpResponse
from django.shortcuts import render

from bodegabsf.forms import BsfForm
from .models import Bsf  # importar el modelo

def data(request):
    bsfs = Bsf.objects.all()
    return render(request, 'index.html', context={'bsfs': bsfs})

# area formulario 

def formulario(request):
    form = BsfForm()
    
    return render( request, 'bsf_form.html',{'form': form})
