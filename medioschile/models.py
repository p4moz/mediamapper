 # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Estos modelos están desarrollados tomando como fuente 
# la industria de medios de Chile en el año 2016.
# Deben ser adaptados en este archivo para realizar un mapa 
# de los medios de otro país.

class Periodicidad(models.Model):
	"""
	Periodicidad de medios en papel.
	"""
	class Meta:
		verbose_name = 'Periodicidad'
		verbose_name_plural = 'Periodicidades'
	periodicidad = models.CharField("Periodicidad", max_length=300)
	def __str__(self):
		return self.periodicidad

class Persona(models.Model):
	"""
	Persona puede ser un propietario o un ejecutivo de un medio -director, editor-. 
	Todas las personas deben ser ingresadas en el modelo Persona, para luego ser subclasificadas.
	"""
	class Meta:
		verbose_name = 'Persona'
		verbose_name_plural = 'Personas'
	nombre = models.CharField("Nombre/Apellido", max_length=250)
	nombres = models.CharField("Nombres", max_length=250, null=True, blank=True)
	apellidos = models.CharField("Apellidos", max_length=250, null=True, blank=True)
	rut = models.CharField("R.U.T.", max_length=250, null=True, blank=True)
	email = models.EmailField("Email", max_length=250, null=True, blank=True)
	def __str__(self):
		return self.nombre

class Empresa(models.Model):
	"""
	La empresa periodística detrás del medio, ej. La Tercera SAP, no COPESA -que es un grupo-.
	"""
	class Meta:
		verbose_name = 'Empresa'
		verbose_name_plural = 'Empresas'
	nombre = models.CharField("Nombre", max_length=250)
	rut = models.CharField("R.U.T.", max_length=250, null=True, blank=True)
	empresa_sociedad_propietaria = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Empresa o Sociedad Propietaria')
	def __str__(self):
		return self.nombre