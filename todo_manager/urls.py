from django.conf.urls import patterns, include, url
from django.contrib import admin
from todo_app import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todo_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^$',views.home),  #home page
	# url(r'^index/signup$',views.signup) #sign up for creating new user
	# url(r'^index/login$',views.login) #log in for existing user
	# url(r'^index/login/tasks/[1-9]{1,}/$',views.tasksDisplay) #display page after login
	url(r'^tasks/',views.allTasksDisplay) ,
	url(r'^publictasks/',views.get_all_public_tasks) ,
	url(r'^tasks/(?P<user_id>\w+)$',views.get_user_tasks)

)
