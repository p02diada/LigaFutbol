from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Equipo(models.Model):
	nombre = models.CharField(max_length = 100)
	ciudad = models.CharField(max_length = 100)
	historia = models.TextField(null=True, blank=True)
	nombreEntrenador = models.CharField(max_length = 100)
	anyoCreacion = models.IntegerField()

	def __unicode__(self):
		return self.nombre

	#def print_details(self):
	#	return "Nombre: %s. AnyoCreacion: %d. Pais: %s" %(self.nombre, self.anyoCreacion, self.pais)     

class Jugador(models.Model):
	nombre = models.CharField(max_length = 100)
	fechaNacimiento= models.DateField()
	lugarNacimiento =models.CharField(max_length = 100)
	edad=models.IntegerField()
	equipo = models.ForeignKey(Equipo)
	posicion =models.CharField(max_length = 100)
	historia = models.TextField(null=True, blank=True)
	

	def __unicode__(self):
		return self.nombre

class Usuario(User):
	horas= models.IntegerField(null=True, blank=True)


