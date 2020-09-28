from django.http import HttpResponse
from django.shortcuts import redirect
from apps.libro.models import Autor
from django.db.models import Q

def index(request):
    return redirect("http://google.com/")
    if request.method == 'GET':
        verify = request.GET.get('verification')
        if verify:
            return redirect("http://google.com/")
            
    return HttpResponse("Este es el Index")

def chatbot(request):
    
    if request.method == 'POST':
        queryset = request.GET.get('autor')


        return HttpResponse(queryset)

        

    