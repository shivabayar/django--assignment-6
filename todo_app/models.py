from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

PRIORITY = (
		(0,"Show stopper"),
		(1,"High"),
		(2,"Medium"),
		(3,"Low")
	)

VISIBILITY = (
		(0,"Private"),
		(1,"Public")
	)

STATUS = (
		(0,"Pending"),
		(1,"Completed")
	)


# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')

        
class task(models.Model):
	user_name  =models.ForeignKey(User)
	# task_name = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	created_date = models.CharField(max_length=200)
	# created_date = models.DateField(_("Date"), default=datetime.date.today)
	priority = models.IntegerField(choices=PRIORITY,default=0)
	status = models.IntegerField(choices=STATUS,default=0)
	visiblity = models.IntegerField(choices=VISIBILITY,default=0)
	dead_line = models.CharField(max_length=200)

	# def __unicode__(self):
	# 	# return unicode(self.task_name,self.user_name,self.title,self.created_date,self.priority,self.status,self.visiblity,self.dead_line).encode('utf-8')
	# 	return unicode(self.task_name).encode('utf-8')
