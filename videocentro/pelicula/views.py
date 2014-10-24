from django.shortcuts import render, render_to_response,get_object_or_404
from django.http import HttpResponse, Http404
from django.core.context_processors import csrf
from .models import pelicula

# Create your views here.
def peliculas_view(request):
	peliculas = pelicula.objects.all()

	return render_to_response('peliculas.html', {'peliculas':peliculas})
