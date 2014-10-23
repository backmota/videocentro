from django.db import models
from actor.models import *
from director.models import *
from productora.models import *

# Create your models here.
class pelicula(models.Model):
	nombrePelicula = models.CharField(max_length=45, primary_key=True)
	estreno = models.DateField()
	foto = models.ImageField(upload_to='static')
	precio = models.IntegerField(max_length=45)
	nombreActor = models.ForeignKey(actor)
	nombreDirector = models.ForeignKey(director)
	nombreProductora = models.ForeignKey(productora)

	def __unicode__(self):
		return self.nombrePelicula