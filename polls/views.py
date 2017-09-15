from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.views import View
from .models import Question, Choice, Profile
from django.http import JsonResponse, Http404
from django.contrib.auth import (authenticate,login as auth_login, logout as auth_logout)
from django.contrib.auth.models import User
from django.db import IntegrityError
import pdb
# Create your views here.


class PollDetailView(DetailView):
	 model = Question
	 context_object_name='poll'
	 template_name='polls/detail.html'


class HomeView(ListView):
	model=Question
	context_object_name='polls'
	template_name='polls/index.html'
	queryset=Question.objects.filter(status='Active')


	def get_context_data(self, **kwargs):
		context=super(HomeView, self).get_context_data(**kwargs)
		context['dead_polls']=Question.objects.filter(status='completed')
		return context 


class VoteView(View):
	def get(self, request):
		status={'done':True,'login':True,'has_already_voted':False, 'cant_vote':False}
		if self.request.user.is_authenticated():
			if self.request.is_ajax():
				#pdb.set_trace()
				q_id=self.request.GET.get('id')
				chosen=self.request.GET.get('choice')
				users_that_has_voted=User.objects.filter(question__id=q_id)
				if self.request.user in users_that_has_voted:
					status['has_already_voted']=True
					return JsonResponse(status)
				else:	
					try:
						chosen_set=Choice.objects.filter(choice_text__icontains=chosen).filter(question__id=q_id)
						if chosen_set.count() == 1:
							chosen_object=chosen_set[0]
							can_vote=chosen_object.vote(self.request.user, self.request.GET.get('state'))
							if not can_vote:
								status['cant_vote']=True
								status['done']=False
						else:
							status['done']=False
					except:
						status['done']=False
					
					return JsonResponse(status)
			else:
				return Http404()
		else:
			status['login']=False
			status['done']=False
			return  JsonResponse(status)


class loginView(View):
	status=dict()
	status['login']=True
	status['friends']=False
	def get(self,request):
		if self.request.is_ajax():
			first_name=request.GET.get('first_name')
			last_name=request.GET.get('last_name')
			email=request.GET.get('email')
			gender=request.GET.get('gender')
			id=request.GET.get('id')
			try:
				User.objects.create(first_name=first_name, last_name=last_name,email=email,username=email).save()
				user=User.objects.get(username=email)	
				profile=Profile.objects.create(user=user, gender=gender,oauth_id=id)
				#pdb.set_trace()
				profile.save()
				self.status['friends']=True
			except IntegrityError :
				user=User.objects.get(username=email)
			auth_login(self.request, user)
			return JsonResponse(self.status)


class  updateFriendCount(View):
	def get(self, request):
		data=dict()
		no=self.request.GET.get('total_count')
		profile=Profile.objects.get(user=self.request.user)
		data['response']=profile.saveFriend(no)
		return JsonResponse(data)














