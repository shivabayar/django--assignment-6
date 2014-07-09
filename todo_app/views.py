from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth.models import User
from todo_app.models import task
from django.contrib.auth.decorators import login_required


# Create your views here.

# @login_required(login_url='/')
def home(request):
	return render_to_response("home_page.html")

def get_all_public_tasks(request):
	all_task = task.objects.filter(visiblity=1)
	return render_to_response("tasks.html",{'all_task':all_task})		

def allTasksDisplay(request):
	all_task = task.objects.all()
	# print "dsaffffffffffffffff"
	return render_to_response("tasks.html",{'all_task':all_task})

def get_user_tasks(request,user_id):
	all_task = task.objects.filter(user_name_id=user_id)
	print "dsaffffffffffffffff"
	print all_task
	return render_to_response("tasks.html",{'all_task':all_task})