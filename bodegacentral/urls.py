from django.urls import path
from . import views

#/bodegacentral/.....

urlpatterns = [
    path('', views.index,name='index'),
    path('formulariocentral',views.formulario, name='formulariocentral'),
]
