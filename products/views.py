from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .helpers import call_mat,CallUrl
# Create your views here.
import pyodbc
def sql():
	connection_data=pyodbc.connect('driver={%s};server=%s;database=%s;uid=%s;pwd=%s' % 
		('SQL Server', '172.31.23.171', 'salesiq_IC_processing_DEV', 'salesiq_IC_processing_dev', 'salesiq@123' ) )
	cursor_data = connection_data.cursor()
	query='select top 1 * from  abcd'
	cursor_data.execute(query)
	print('s')
	d={}
	for i in cursor_data:
		d["data"]=i[6]
	return d


def index(request,*args,**kwargs):
	return HttpResponse('<h1>Hello</h1>')



def home(request,*args,**kwargs):
	d={
		"key":12,
		"key1":"hello"
	}
	#d=sql()
	print(request)
	return render(request,"show.html",d)

def callpythonfun(request,*args,**kwargs):
	return render(request,"callpython_page.html",{})

def actionUrl(request,*args,**kwargs):
	return HttpResponse('<h1>actionUrl</h1>')

def secondcall(request,*args,**kwargs):
	print(request.GET['name'])
	jobname=request.GET['name']
	res=call_mat('testjob')
	return HttpResponse('<h1>Done</h1>')

def PythonRequest(request,*args,**kwargs):
	d={}
	d["Response"]=CallUrl('http://172.31.23.171/outboundzip/')
	return render(request,"Python_Request.html",d)
