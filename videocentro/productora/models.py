from django.db import models

# Create your models here.
class productora(models.Model):
	nombreProductora = models.CharField(max_length=45, primary_key=True)
	direccion = models.CharField(max_length=45)
	foto = models.ImageField(upload_to='static')

	def __unicode__(self):
		return self.nombreProductora