from django.db import models
from django.utils import timezone
import datetime
from django.utils.timezone import now
from pytz import timezone



# Create your models here.


class Contacts(models.Model):
	name		=models.TextField()
	email	    =models.TextField()
	subject		=models.TextField()
	message		=models.TextField()

class index_data(models.Model):
	subject=models.TextField()
	subsubject=models.TextField()
	descriptions=models.TextField()
	image=models.ImageField(upload_to ='pics')

class MatJobInformation(models.Model):
	IP=models.CharField(max_length=400,default='172.31.12.129')
	JobName=models.TextField(max_length=400)
	projectName=models.CharField(max_length=400)
	version=models.CharField(max_length=50,default='default')
	user=models.CharField(max_length=50,default='Test_User3')
	password=models.CharField(max_length=50,default='admin123')

	Environment=models.CharField(max_length=50,default='OutBound')
	Enable=models.BooleanField(default=True)
	Day_of_Week=models.CharField(max_length=50,default='mon,tue,wed,thu,fri,sat,sun')
	Hours=models.CharField(max_length=50,default='23:00')
	Minutes=models.CharField(max_length=50,default='46')
	EndDate=models.DateTimeField(default=now,editable=True)

class MatillionJobInformation(models.Model):
	IP=models.CharField(max_length=400,default='172.31.12.129')
	JobName=models.CharField(max_length=1000)
	projectName=models.CharField(max_length=400)
	version=models.CharField(max_length=50,default='default')
	user=models.CharField(max_length=50,default='Test_User3')
	password=models.CharField(max_length=50,default='admin123')
	MatGroup=models.CharField(max_length=1000,default='Outbound_Process')
	Environment=models.CharField(max_length=50,default='OutBound')
	Enable=models.BooleanField(default=True)
	Day_of_Week=models.CharField(max_length=50,default='mon,tue,wed,thu,fri,sat,sun')
	timezone=models.CharField(max_length=50,default='Asia/Kolkata')
	Hours=models.CharField(max_length=50,default='23:00')
	Minutes=models.CharField(max_length=50,default='46')
	EndDate=models.DateField(default=datetime.date.today)
	LastModified=models.DateTimeField(default=now,editable=False) 
	LastModifiedBy=models.CharField(max_length=400,default='User',editable=False) 


	def __str__(self):
		return str(self.projectName)+'_'+str(self.JobName)+'_'+'Hour:'+str(self.Hours)+'_Minutes:'+str(self.Minutes)
		
	def save(self, *args, **kwargs):
		self.LastModified = datetime.datetime.now()
		super(MatillionJobInformation, self).save(*args, **kwargs)


class Matilion_Run_JobHistory(models.Model):
	JobID=models.CharField(max_length=800)
	JobName=models.CharField(max_length=800)
	StartTime=models.CharField(max_length=500,default='default')
	EndTime=models.CharField(max_length=500,default='default')
	Status=models.CharField(max_length=500,default='Failed')
	RunDate=models.CharField(max_length=500,default='default')
	Sche_or_Manu=models.CharField(max_length=500,default='Schedule')
	description=models.CharField(max_length=500,default='Success')

class PythonJobInformations(models.Model):
	JobName=models.CharField(max_length=1000)
	Enable=models.BooleanField(default=True)
	Day_of_Week=models.CharField(max_length=50,default='mon,tue,wed,thu,fri,sat,sun')
	timezone=models.CharField(max_length=50,default='Asia/Kolkata')
	Hours=models.CharField(max_length=50,default='23:00')
	Minutes=models.CharField(max_length=50,default='46')
	EndDate=models.DateField(default=datetime.date.today)
	LastModified=models.DateTimeField(default=now,editable=False) 
	LastModifiedBy=models.CharField(max_length=400,default='User',editable=False) 


	def __str__(self):
		return str(self.JobName)+'_'+'Hour:'+str(self.Hours)+'_Minutes:'+str(self.Minutes)

	def save(self, *args, **kwargs):
		self.LastModified = datetime.datetime.now()
		super(PythonJobInformations, self).save(*args, **kwargs)


class Python_Run_JobHistory(models.Model):
	JobID=models.CharField(max_length=800)
	JobName=models.CharField(max_length=800)
	StartTime=models.CharField(max_length=500,default='default')
	EndTime=models.CharField(max_length=500,default='default')
	Status=models.CharField(max_length=500,default='Failed')
	RunDate=models.CharField(max_length=500,default='default')
	Sche_or_Manu=models.CharField(max_length=500,default='Schedule')
	description=models.CharField(max_length=500,default='Success')
	 
class TalendJobInformations(models.Model):
	JobName=models.CharField(max_length=1000)
	EndPoint=models.CharField(max_length=3000)
	Enable=models.BooleanField(default=True)
	Day_of_Week=models.CharField(max_length=50,default='mon,tue,wed,thu,fri,sat,sun')
	timezone=models.CharField(max_length=50,default='Asia/Kolkata')
	Hours=models.CharField(max_length=50,default='23:00')
	Minutes=models.CharField(max_length=50,default='46')
	EndDate=models.DateField(default=datetime.date.today)
	
	LastModified=models.DateTimeField(default=now,editable=False) 
	LastModifiedBy=models.CharField(max_length=400,default='User',editable=False) 
	

	def __str__(self):
		return str(self.JobName)+'_'+'Hour:'+str(self.Hours)+'_Minutes:'+str(self.Minutes)

	def save(self, *args, **kwargs):
		self.LastModified = datetime.datetime.now()
		super(TalendJobInformations, self).save(*args, **kwargs)



class Talend_Run_JobHistory(models.Model):
	JobID=models.CharField(max_length=800)
	JobName=models.CharField(max_length=800)
	StartTime=models.CharField(max_length=500,default='default')
	EndTime=models.CharField(max_length=500,default='default')
	Status=models.CharField(max_length=500,default='Failed')
	RunDate=models.CharField(max_length=500,default='default')
	Sche_or_Manu=models.CharField(max_length=500,default='Schedule')
	description=models.CharField(max_length=500,default='Success')



class CustomJobInformations(models.Model):
	JobName=models.CharField(max_length=1000)
	HtmlData=models.TextField()
	Comp_Seq=models.CharField(max_length=1000)
	Comp_Data=models.CharField(max_length=1000)
	Enable=models.BooleanField(default=True)
	Day_of_Week=models.CharField(max_length=50,default='mon,tue,wed,thu,fri,sat,sun')
	timezone=models.CharField(max_length=50,default='Asia/Kolkata')
	Hours=models.CharField(max_length=50,default='23:00')
	Minutes=models.CharField(max_length=50,default='46')
	EndDate=models.DateField(default=datetime.date.today)
	MatIP=models.CharField(max_length=100,default='172.31.12.129')
	MatGroup=models.CharField(max_length=1000,default='Outbound_Process')
	MatProject=models.CharField(max_length=1000,default='Outbound_Process')
	MatVersion=models.CharField(max_length=1000,default='default')
	MatEnvironment=models.CharField(max_length=1000,default='OutBound')
	user=models.CharField(max_length=50,default='Test_User3')
	password=models.CharField(max_length=50,default='admin123')
	LastModified=models.DateTimeField(default=now,editable=False) 
	LastModifiedBy=models.CharField(max_length=400,default='User',editable=False) 
	


	def __str__(self):
		return str(self.JobName)+'_'+'Hour:'+str(self.Hours)+'_Minutes:'+str(self.Minutes)

	def save(self, *args, **kwargs):
		self.LastModified = datetime.datetime.now()
		super(CustomJobInformations, self).save(*args, **kwargs)



class Custom_Run_JobHistory(models.Model):
	JobID=models.CharField(max_length=800)
	JobName=models.CharField(max_length=800)
	StartTime=models.CharField(max_length=500,default='default')
	EndTime=models.CharField(max_length=500,default='default')
	Status=models.CharField(max_length=500,default='Failed')
	RunDate=models.CharField(max_length=500,default='default')
	Sche_or_Manu=models.CharField(max_length=500,default='Schedule')
	description=models.CharField(max_length=500,default='Success')