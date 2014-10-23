from django.db import models

# Create your models here.
class director(models.Model):
	nombre = models.CharField(max_length=45, primary_key=True)
	apellidoP = models.CharField(max_length=45)
	apellidoM = models.CharField(max_length=45, blank=True)
	fecha_nacimiento = models.DateField()
	foto = models.ImageField(upload_to='static')

	def __unicode__(self):
		return self.nombre