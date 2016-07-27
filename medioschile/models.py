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
