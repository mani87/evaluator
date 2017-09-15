from django.db import models

# Create your models here.

class Question(models.Model):
	statement = models.CharField(blank=False, max_length=1000)
	answer = models.CharField(blank=False, max_length=1000)
	marks = models.IntegerField(blank=False)
	
	def __str__(self):
		return self.statement

class Answer(models.Model):
	unanswered = models.BooleanField(default=False)
	question = models.ForeignKey(Question, related_name="answer_related")
	marks_awarded = models.IntegerField(blank=False)
	your_response = models.CharField(blank=False, max_length=1000)
