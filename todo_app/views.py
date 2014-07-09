from django.shortcuts import render, render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from todo_app.models import task
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login ,logout
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# @login_required(login_url='/')
def home(request):
	return render_to_response("home_page.html")

def get_all_public_tasks(request):
	all_task = task.objects.filter(visiblity=1)
	return render_to_response("tasks.html",{'all_task':all_task})

def get_all_private_tasks(request):
	all_task = task.objects.filter(visiblity=0)
	return render_to_response("tasks.html",{'all_task':all_task})


def allTasksDisplay(request):
	all_task = task.objects.all()
	# print "dsaffffffffffffffff"
	return render_to_response("tasks.html",{'all_task':all_task})

# def get_user_tasks(request,user_id):
# 	all_task = task.objects.filter(user_name_id=user_id)
# 	print "dsaffffffffffffffff"
# 	print all_task
# 	return render_to_response("tasks.html",{'all_task':all_task})



@csrf_exempt
def validate_login(request):
	context = RequestContext(request)

	if request.method == 'POST':
		user_name = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=user_name,password=password)
		if user:
			login(request,user)
			return HttpResponseRedirect('/tasks')
		else:
			return HttpResponse("Invalid login details")
	else:
		render_to_response('home_page.html')


def view_user_tasks(request):
    all_task = task.objects.filter(user_name=request.user.id)
    print all_task
    # public_task = tasks.objects.filter(accessibility='public').values()
    userName = request.user.username
    return render_to_response('tasks.html', {'all_task':all_task})