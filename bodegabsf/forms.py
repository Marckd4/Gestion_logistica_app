from . import models
from django.forms import ModelForm

class BsfForm(ModelForm):
    class Meta:
        model = models.Bsf
        fields ='__all__' #Incluye todos los campos del modelo


