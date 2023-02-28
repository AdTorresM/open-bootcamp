from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404

def home(request):
    director = Director.objects.all()
    
    return render(request, 'index.html', {'director': director})

def peliculas(request, id):
    peliculas = Pelicula.objects.filter(director = id)
    print(peliculas)
    return render(request, 'peliculas.html', {'peliculas': peliculas})




