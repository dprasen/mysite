from django.db import models
	
class Project(models.Model):		
		name = models.CharField(max_length=200)
		started_on = models.DateTimeField('initiated on')
		client_name = models.CharField(max_length=200)
		description = models.CharField(max_length=1000)
		initiator = models.CharField(max_length=200)
		def __unicode__(self):
				return self.name
				
class Userstory(models.Model):
		project = models.ForeignKey(Project)
		name = models.CharField(max_length=200)
		def __unicode__(self):
				return self.name
				
class Usecase(models.Model):
		userstory = models.ForeignKey(Userstory)
		name = models.CharField(max_length=200)
		def __unicode__(self):
				return self.name

class Task(models.Model):
		usecase = models.ForeignKey(Usecase)
		name = models.CharField(max_length=200)
		def __unicode__(self):
				return self.name

