from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import pdb

# Create your models here.

class Category(models.Model):
	name=models.CharField(max_length=50)
	def __str__(self):
		return self.name

class Question(models.Model):
	question_text=models.CharField(max_length=50, unique=True)
	pub_date=models.DateTimeField(auto_now=True)
	thumbnail=models.ImageField(upload_to='polls/%Y/%m/%d')
	status=models.CharField(max_length=50, choices=(('Active', 'Active'), ('Completed', 'Completed')))
	feature=models.BooleanField(default=False)
	category=models.ForeignKey(Category)
	slug = models.SlugField(null=True, blank=True)
	description=models.TextField(null=True)
	user_that_has_vote=models.ManyToManyField(User,blank=True)

	def save(self, *args, **kwargs):
		if not self.id:
		    self.slug = slugify(self.question_text)

		return super(Question, self).save(*args, **kwargs)

class Profile(models.Model):
	user=models.OneToOneField(User)
	oauth_id=models.CharField(max_length=100, unique=True)
	gender=models.CharField(max_length=15)
	no_of_friends=models.IntegerField(null=True)

	def __str__(self):
		return self.user.first_name

	def saveFriend(self, count):
		self.no_of_friends=count
		self.save()
		return True

class State(models.Model):
	name=models.CharField(max_length=20)

	def __str__(self):
		return self.name


class Choice(models.Model):
	question=models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)
	location=models.ManyToManyField(State)
	color=models.CharField(max_length=50, null=True, choices=(('#08aae6','Blue'),
																('#00C851', 'Green'), 
																('#ff3547','Red'),
																('#880e4f','Purple') ,
																('#F80', 'Orange'),
							                                  )
	                       )

	
	def vote(self,user, state):
		question=self.question
		if user.profile.no_of_friends <= 100:
			self.votes+=1
			state=state.replace(' ','')
			try:
				location=State.objects.get(name__icontains=state)

			except ObjectDoesNotExist:
				location=State.objects.get(name__icontains='anoynymous')
			
			self.location.add(location)
			question.user_that_has_vote.add(user)
			self.save()
			return True
		else:
			return False




