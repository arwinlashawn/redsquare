from django.shortcuts import render
from django.contrib import messages
from django.db import models
from django.views.generic import ListView, CreateView
from .models import Post
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'notes/home.html', context)

def addPost(request):
	new_item = Post(content = request.POST['content'])
	new_item.save()
	return HttpResponseRedirect('')


class PostListView(ListView):
	model = Post
	template_name = 'notes/home.html' 
	context_object_name = 'posts'
	# notice that latest message is at the bottom, gotta change it
	ordering = ['-date_posted']





def about(request):
	return render(request, 'notes/about.html', {'title': 'About'})

# looking for notes/post_list.html
# app/model_viewtype.html