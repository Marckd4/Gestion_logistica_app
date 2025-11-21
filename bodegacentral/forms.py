from . import models
from django.forms import ModelForm

class CentralForm(ModelForm):
    class Meta:
        model = models.Central
        fields ='__all__' #Incluye todos los campos del modelo


