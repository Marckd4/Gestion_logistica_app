from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm # formato de extarer fprmulario
from django.contrib.auth.models import User


def usuario(request):
    
    if request.method == 'GET':
        return render (request, 'data_usuario.html',{
        'form':UserCreationForm
    })
        
    
    else:
        if request.POST['password1'] == request.POST['password2']:
            # registro user
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                return HttpResponse('Usuario creado')
            except:
                return HttpResponse ('Usuario existe')
        return HttpResponse('No conincide contraseña')
        
    
    
    
def home(request):
    return render(request, 'home.html')