from django.shortcuts import render, render_to_response,get_object_or_404
from django.http import HttpResponse, Http404
from django.core.context_processors import csrf
from .models import pelicula


# Create your views here.

def pelicula_view(request, nombrePelicula):

	nombrePelicula = get_object_or_404(pelicula, nombrePelicula=nombrePelicula)

	return render_to_response('pelicula.html', {'nombrePelicula':nombrePelicula})

def peliculas(request):
	peliculas = pelicula.objects.all()

	return render_to_response('peliculas.html', {'peliculas':peliculas})
