from django.db import models

from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Person(models.Model):
	def __str__(self):
		return self.firstName + '_' + self.lastName

	LABPOS = [
		('PI','PI'),
		('PH','Graduate student, PhD'),
		('MS','Graduate student, MS'),
		('UG','Undergraduate intern'),
		('VS','Visiting scholar'),
		('PD','Postdoctoral scholar'),
		('CO','Collaborator'),
	]

	firstName = models.CharField(max_length=200)
	lastName = models.CharField(max_length=200)
	personalWeb = models.CharField(max_length=200, default='', blank=True)
	labPosition = models.CharField(max_length=200, choices=LABPOS, blank='')
	email = models.CharField(max_length=200, default='', blank=True)
	shortBio = models.TextField()

	class Meta:
		ordering = ['labPosition']# Create your models here.
