from django.db import models
from datetime import datetime

# Create your models here.
class Sponsor(models.Model):
	pic = models.ImageField(upload_to='sponsors/' + str(datetime.now().year),help_text='300 x 200')
	name = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	link = models.CharField(max_length=50,blank=True,null=True) #URL
	details = models.TextField(max_length=1000,blank=True,null=True)
	main_homepage_display = models.BooleanField(help_text='Should this sponsor be displayed on the EDC homepage?')
	event_homepage_display = models.BooleanField(help_text= 'Should this sponsor be displayed on the event\'s homepage?')
	event = models.ForeignKey('events.Event',blank=True,null=True)

	def __unicode__(self):
		return self.name

	def get_event(self):
		return self.event

	def get_absolute_url(self):
		return ("%s/sponsors/#%s")%(self.event.get_absolute_url(),self.name)
