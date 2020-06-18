from django.shortcuts import render
from django.http import HttpResponse
from .models import Custom_Run_JobHistory,CustomJobInformations,TalendJobInformations,Talend_Run_JobHistory,Contacts,index_data,MatillionJobInformation,Matilion_Run_JobHistory,PythonJobInformations,Python_Run_JobHistory
from .MatilionHelper import call_mat,checkStatus,call_mat_with_less_param
import time
from .JobMapp import JobMapping,PythonJobMapping,TalendJobMapping,CustomJobMapping
import json
from datetime import datetime as dt
import time
from pytz import timezone
from .schedule import start_sch,start_sch_mat,start_sch_mat1
import threading
from .PythonHelper import CallPythonJob
from django.db.models.signals import post_save
from django.dispatch import receiver
from .Talend_Helper import CallTalendJob
import logging
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
def ok_to_load_in_a_frame(request):
    return HttpResponse("This page is safe to load in a frame on any site.")


log = logging.getLogger(__name__)

def index(request,*args,**kwargs):
	return render(request,"index.html",{})

def about(request,*args,**kwargs):
	return render(request,"about.html",{})


##################################################################################################################

def RunMatJobNowUtil(request):
	try:
		print('RunMatJobNowUtil Called ------'+str(request))
		log.debug('RunMatJobNowUtil Called ------'+str(request))

		print(request.GET.dict())
		log.debug(request.GET.dict())

		mapping=request.GET.dict()
		days=mapping['DayofWeek'].split(',')
		isfound=False
		for day in days:
			print('RunMatJobNowUtil day-----------'+str(day))
			log.debug('RunMatJobNowUtil day-----------'+str(day))
			if isfound==True:
				break

			key=str(day).lower()+'_'+str(mapping['Hour'])+'_'+str(mapping['Minute'])
			print('RunMatJobNowUtil key-----------'+str(key))
			log.debug('RunMatJobNowUtil key-----------'+str(key))
			print('JobMapping------------'+str(JobMapping))
			log.debug('JobMapping------------'+str(JobMapping))

			if key in JobMapping:
				ObjectList=JobMapping[key]
				print('RunMatJobNowUtil in if key-----------')
				log.debug('RunMatJobNowUtil in if key-----------')
				print('********************in RunMatJobNowUtil if************************************** '+str(ObjectList))
				log.debug('********************in RunMatJobNowUtil if************************************** '+str(ObjectList))
				print('ObjectList----RunMatJobNow--'+str(ObjectList))
				log.debug('ObjectList----RunMatJobNow--'+str(ObjectList))
				for ob in ObjectList:
					if isfound==True:
						break
					if ob.JobName==mapping['JobName']:
						print('RunMatJobNowUtil if ob.JobName==:-----------'+str(ob.JobName))
						log.debug('RunMatJobNowUtil if ob.JobName==:-----------'+str(ob.JobName))

						isfound=True
						History_Job_ID=''
						try:
							Id=call_mat_with_less_param(ob.JobName,ob.projectName,ob.version,ob.user,ob.password,ob.Environment,ob.IP,ob.MatGroup)
							History_Job_ID=str(ob.JobName)+'_'+str(key.split('_')[1])+'_'+str(key.split('_')[2])
							print('****************************'+str(History_Job_ID)+'*********************************')
							log.debug('****************************'+str(History_Job_ID)+'*********************************')
							t = threading.Thread(target=Insert_JobStatus,args=(Id,History_Job_ID,ob.JobName,ob,'Manual',))
							t.setDaemon(True)
							t.start()
						except Exception as e:
							print('Error while calling call_mat_with_less_param RunMatJobNowUtil')
							log.error('Error while calling call_mat_with_less_param RunMatJobNowUtil')
							insert_history_mat(History_Job_ID,ob.JobName,GetStartEndDateDate(),GetStartEndDateDate(),'Error '+str(e),GetRunDate())

		print('End Control (((((((((((((((((((((((((')
		log.debug('End Control (((((((((((((((((((((((((')
	except Exception as E:
		print('Exception RunMatJobNowUtil '+str(E))
		log.error('Exception RunMatJobNowUtil '+str(E))



def RunPythonJobNowUtil(request):
	try:
		print('RunPythonJobNowUtil Called ------'+str(request))
		print(request.GET.dict())
		log.debug('RunPythonJobNowUtil Called ------'+str(request))
		log.debug(request.GET.dict())
		mapping=request.GET.dict()
		days=mapping['DayofWeek'].split(',')
		isfound=False
		for day in days:
			print('RunPythonJobNowUtil day-----------'+str(day))
			log.debug('RunPythonJobNowUtil day-----------'+str(day))
			if isfound==True:
				break

			key=str(day).lower()+'_'+str(mapping['Hour'])+'_'+str(mapping['Minute'])
			print('RunPythonJobNowUtil key-----------'+str(key))
			print('PythonJobMapping------------'+str(PythonJobMapping))
			log.debug('RunPythonJobNowUtil key-----------'+str(key))
			log.debug('PythonJobMapping------------'+str(PythonJobMapping))
			if key in PythonJobMapping:
				ObjectList=PythonJobMapping[key]
				print('RunPythonJobNowUtil in if key-----------')
				print('********************in RunPythonJobNowUtil if************************************** '+str(ObjectList))
				print('ObjectList----RunMatJobNow--'+str(ObjectList))
				log.debug('RunPythonJobNowUtil in if key-----------')
				log.debug('********************in RunPythonJobNowUtil if************************************** '+str(ObjectList))
				log.debug('ObjectList----RunMatJobNow--'+str(ObjectList))
				for ob in ObjectList:
					if isfound==True:
						break
					if ob.JobName==mapping['JobName']:
						print('RunMatJobNowUtil if ob.JobName==:-----------'+str(ob.JobName))
						log.debug('RunMatJobNowUtil if ob.JobName==:-----------'+str(ob.JobName))

						isfound=True
						startTime=GetStartEndDateDate()
						RunDate=GetRunDate()
						History_Job_ID=''
						try:
							History_Job_ID=str(ob.JobName)+'_'+str(key.split('_')[1])+'_'+str(key.split('_')[2])
							t = threading.Thread(target=Insert_JobStatus_python,args=(History_Job_ID,ob.JobName,startTime,RunDate,'Manual',))
							t.setDaemon(True)
							t.start()
						except Exception as e:

							print('Error While Insert_JobStatus_python===='+str(e))
							log.error('Error While Insert_JobStatus_python===='+str(e))

	except Exception as E:
		print('Error While Calling RunPythonJobNowUtil')
		log.error('Error While Calling RunPythonJobNowUtil')

	



def RunTalendJobNowUtil(request):
	try:
		print('RunTalendJobNowUtil Called ------'+str(request))
		log.debug('RunTalendJobNowUtil Called ------'+str(request))
		print(request.GET.dict())
		log.debug(request.GET.dict())
		mapping=request.GET.dict()
		days=mapping['DayofWeek'].split(',')

		isfound=False
		for day in days:
			print('RunTalendJobNowUtil day-----------'+str(day))
			log.debug('RunTalendJobNowUtil day-----------'+str(day))
			if isfound==True:
				break

			key=str(day).lower()+'_'+str(int(mapping['Hour']))+'_'+str(int(mapping['Minute']))
			print('RunTalendJobNowUtil key-----------'+str(key))
			print('TalendJobMapping------------'+str(TalendJobMapping))
			log.debug('RunTalendJobNowUtil key-----------'+str(key))
			log.debug('TalendJobMapping------------'+str(TalendJobMapping))
			if key in TalendJobMapping:
				ObjectList=TalendJobMapping[key]
				print('RunTalendJobNowUtil in if key-----------')
				print('********************in RunTalendJobNowUtil if************************************** '+str(ObjectList))
				print('ObjectList----RunMatJobNow--'+str(ObjectList))
				log.debug('RunTalendJobNowUtil in if key-----------')
				log.debug('********************in RunTalendJobNowUtil if************************************** '+str(ObjectList))
				log.debug('ObjectList----RunMatJobNow--'+str(ObjectList))

				for ob in ObjectList:
					if isfound==True:
						break
					if ob.JobName==mapping['JobName']:
						print('RunMatJobNowUtil if ob.JobName==:-----------'+str(ob.JobName))
						log.debug('RunMatJobNowUtil if ob.JobName==:-----------'+str(ob.JobName))
						isfound=True
						try:
							startTime=GetStartEndDateDate()
							RunDate=GetRunDate()

							History_Job_ID=str(ob.JobName)+'_'+str(key.split('_')[1])+'_'+str(key.split('_')[2])
							log.debug('History_Job_ID -----------------'+str(History_Job_ID))
							t = threading.Thread(target=Insert_JobStatus_Talend,args=(History_Job_ID,ob.JobName,startTime,RunDate,ob.EndPoint,'Manual'))
							t.setDaemon(True)
							t.start()
						except Exception as E:
							print('Error in RunTalendJobNowUtil-----'+str(E))
							log.error('Error in RunTalendJobNowUtil-----'+str(E))
	except Exception as e:
		print('Exception in  calling RunTalendJobNowUtil ')
		log.error('Exception in  calling RunTalendJobNowUtil ')

	


##################################################################################################################







##################################################################################################################


def RunMatJobNow(request,*args,**kwargs):
	print('RunMatJobNow Called ------'+str(request))
	t = threading.Thread(target=RunMatJobNowUtil,args=(request,))
	t.setDaemon(True)
	t.start()
	


	return HttpResponse('SUCCESS')

def RunPythonJobNow(request,*args,**kwargs):
	print('RunPythonJobNow Called ------'+str(request))
	t = threading.Thread(target=RunPythonJobNowUtil,args=(request,))
	t.setDaemon(True)
	t.start()
	


	return HttpResponse('SUCCESS')

def RunTalendJobNow(request,*args,**kwargs):
	print('RunTalendJobNow Called ------'+str(request))
	t = threading.Thread(target=RunTalendJobNowUtil,args=(request,))
	t.setDaemon(True)
	t.start()
	


	return HttpResponse('SUCCESS')




##################################################################################################################








##################################################################################################################

def insert_history_mat(History_Job_ID,job,startTime,ENDTIME,status,RunDate,Sche_or_Manu,description):
	try:
		Matilion_Run_JobHistory.objects.create(JobID=History_Job_ID,JobName=job,StartTime=startTime,EndTime=ENDTIME,Status=status,RunDate=RunDate,Sche_or_Manu=Sche_or_Manu,description=description)
	except Exception as E:
		print('Error in insert_history_mat')
		log.error('Error in insert_history_mat')

def GetStartEndDateDate():
	return dt.now(timezone('Asia/Kolkata')).strftime('%d-%m-%Y %H-%M-%S')

def GetRunDate():
	return dt.now(timezone('Asia/Kolkata')).strftime('%m-%d-%Y')

def GetDate_YMD():
	return dt.now(timezone('Asia/Kolkata')).strftime('%Y-%m-%d')

def Insert_JobStatus(id,History_Job_ID,job,ob,Sche_or_Manu):
	print('Called job Id ===='+str(id))
	log.debug('Called job Id ===='+str(id))
	print(GetStartEndDateDate())
	log.debug(GetStartEndDateDate())
	startTime=GetStartEndDateDate()
	RunDate=GetRunDate()
	try:
		status=checkStatus(id,ob.IP,ob.user,ob.password)
		while True:
			if status=='SUCCESS' or status=='FAILED':
				ENDTIME=GetStartEndDateDate()

				Matilion_Run_JobHistory.objects.create(JobID=History_Job_ID,JobName=job,StartTime=startTime,EndTime=ENDTIME,Status=status,RunDate=RunDate,Sche_or_Manu=Sche_or_Manu,description=status)
				break
			else:
				status=checkStatus(id,ob.IP,ob.user,ob.password)
			time.sleep(45)
	except Exception as E:
		ENDTIME=GetStartEndDateDate()
		print('Exception Occur in Insert_JobStatus matillionjobs '+str(E))
		log.error('Exception Occur in Insert_JobStatus matillionjobs '+str(E))
		insert_history_mat(History_Job_ID,job,startTime,ENDTIME,'FAILED',RunDate,Sche_or_Manu,'FAILED due to '+'Error '+str(E).replace('-','_'))
		#Matilion_Run_JobHistory.objects.create(JobID=History_Job_ID,JobName=job,StartTime=startTime,EndTime=ENDTIME,Status='FAILED due to '+str(E),RunDate=RunDate)

def insert_history_py(History_Job_ID,job,startTime,ENDTIME,status,RunDate,Sche_or_Manu,description):
	try:
		Python_Run_JobHistory.objects.create(JobID=History_Job_ID,JobName=job,StartTime=startTime,EndTime=ENDTIME,Status=status,RunDate=RunDate,Sche_or_Manu=Sche_or_Manu,description=description)
	except Exception as E:
		print('Error in insert_history_py '+str(E))
		log.error('Error in insert_history_py '+str(E))

def Insert_JobStatus_python(History_Job_ID,job,startTime,RunDate,Sche_or_Manu):
	print('Called job Id ===='+str(id))
	log.info('Called job Id ===='+str(id))

	print(GetStartEndDateDate())
	log.error(GetStartEndDateDate())
	try:
		status=CallPythonJob(job+'.py')
		final_status=''
		if str(status)==str(0) or str(status).upper()=='SUCCESS' or str(status).upper()=='PASS':
			print('Python Job SUCCESS')
			log.info('Python Job SUCCESS')
			final_status='SUCCESS'
		else:
			final_status='FAILED'
			print('Python Job FAILED')
			log.info('Python Job FAILED')
		ENDTIME=GetStartEndDateDate()
		insert_history_py(History_Job_ID,job,startTime,ENDTIME,final_status,RunDate,Sche_or_Manu,final_status)
		
	except Exception as E:
		print('Exception Occur in Insert_JobStatus_python  '+str(E))
		log.error('Exception Occur in Insert_JobStatus_python  '+str(E))
		
		insert_history_py(History_Job_ID,job,startTime,GetStartEndDateDate(),'FAILED',RunDate,Sche_or_Manu,'Exception Occur in Insert_JobStatus_python  '+' Error '+str(E).replace('-','_'))
		
def insert_history_tal(History_Job_ID,job,startTime,ENDTIME,status,RunDate,Sche_or_Manu,description):
	try:
		Talend_Run_JobHistory.objects.create(JobID=History_Job_ID,JobName=job,StartTime=startTime,EndTime=ENDTIME,Status=status,RunDate=RunDate,Sche_or_Manu=Sche_or_Manu,description=description)
	except Exception as e:
		print('Error in insert_history_tal '+str(e))
		log.error('Error in insert_history_tal '+str(e))
	


def Insert_JobStatus_Talend(History_Job_ID,job,startTime,RunDate,EndPoint,Sche_or_Manu):
	print('Called job Id ===='+str(id))
	print('Called job EndPoint   ===='+str(EndPoint))
	log.debug('Called job Id ===='+str(id))
	log.debug('Called job EndPoint   ===='+str(EndPoint))

	print(GetStartEndDateDate())
	try:
		status=CallTalendJob(EndPoint)
		final_status=''
		if str(status)==str(0):
			print('******************************Talend Job SUCCESS******************************************'+str(status))
			log.info('******************************Talend Job SUCCESS******************************************'+str(status))
			final_status='SUCCESS'
		else:
			final_status='FAILED'
			print('******************************Talend Job FAILED******************************************'+str(status))
			log.info('******************************Talend Job FAILED******************************************'+str(status))
		
		insert_history_tal(History_Job_ID,job,startTime,GetStartEndDateDate(),final_status,RunDate,Sche_or_Manu,final_status)
		#Talend_Run_JobHistory.objects.create(JobID=History_Job_ID,JobName=job,StartTime=startTime,EndTime=GetStartEndDateDate(),Status=final_status,RunDate=RunDate)
	except Exception as E:
		print('Exception Occur in Insert_JobStatus_Talend  '+str(E))
		log.error('Exception Occur in Insert_JobStatus_Talend  '+str(E))
		insert_history_tal(History_Job_ID,job,startTime,GetStartEndDateDate(),'FAILED',RunDate,Sche_or_Manu,str(E).replace('-','_'))




##################################################################################################################






##################################################################################################################

def GetDayName():
	return dt.now(timezone('Asia/Kolkata')).strftime('%A')[0:3].lower()
	

def GetHour():
	return dt.now(timezone('Asia/Kolkata')).strftime('%H')

def GetMin():
	return dt.now(timezone('Asia/Kolkata')).strftime('%M')

def SchedularDaemonProcess():
	StartMatilionJobUtil()

	while True :
		# Logic to find next date minutes 


		day_name=GetDayName()
		

		Hours_name=GetHour()
		Min_name=GetMin()

		
		key=str(day_name).lower()+'_'+str(int(Hours_name))+'_'+str(int(Min_name))
		print('SchedularDaemonProcess_Matillion key-----------'+key)
		log.debug('SchedularDaemonProcess_Matillion key-----------'+key)
		'''
		#start print Information comment it later
		for jobsprint in JobMapping:
			output=JobMapping[jobsprint]
			if type(output) is list:
				jlist=output
				for jobj in jlist:
					print("Print objects Information(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
					print(jobj)
					print(jobj.JobName)
					print(jobj.projectName)
					print(jobj.version)
					print(jobj.user)
					print(jobj.password)
					print(jobj.Environment)
					print(jobj.Enable)
					print(jobj.Day_of_Week)
					print(jobj.Hours)
					print(jobj.Minutes)
					print(jobj.EndDate)
					print(jobj.id)
					print('now date---------'+str(dt.now(timezone('Asia/Kolkata')).strftime('%Y-%m-%d')))
					if str(jobj.EndDate)==dt.now(timezone('Asia/Kolkata')).strftime('%Y-%m-%d'):
						print('match')
					else:
						print('do not match')
			else:
					print("èlse Print objects Information(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
					print(output)
					print(output.JobName)
					print(output.projectName)
					print(output.version)
					print(output.user)
					print(output.password)
					print(output.Environment)
					print(output.Enable)
					print(output.Day_of_Week)
					print(output.Hours)
					print(output.Minutes)
					print(output.EndDate)
					print(jobj.id)

		

			
			
		#End Print
		'''
		
		try:

			if key in JobMapping:
				ObjectList=JobMapping[key]
				print('********************in if************************************** '+str(ObjectList))
				print('ObjectList------'+str(ObjectList))
				log.debug('********************in if************************************** '+str(ObjectList))
				log.debug('ObjectList------'+str(ObjectList))
				for ob in ObjectList:
					try:
						if ob.Enable==True:
							if str(ob.EndDate)==GetDate_YMD():
								objid=ob.id
								print('objid********************************'+str(objid))
								log.debug('objid********************************'+str(objid))
								MatillionJobInformation.objects.filter(id=objid).update(Enable=False)
								StartMatilionJobUtil()
								#return render(request,"matillionjobs.html",{"obj":obj})
							
							else:
								try:
									Id=call_mat_with_less_param(ob.JobName,ob.projectName,ob.version,ob.user,ob.password,ob.Environment,ob.IP,ob.MatGroup)
								except Exception as E:
									log.error('Error While calling call_mat_with_less_param SchedularDaemonProcess_Matillion key-----------'+str(key)+'-----'+str(E))
									print('Error While calling call_mat_with_less_param SchedularDaemonProcess_Matillion key-----------'+str(key)+'-----'+str(E))
								History_Job_ID=str(ob.JobName)+'_'+str(key.split('_')[1])+'_'+str(key.split('_')[2])
								print('****************************'+str(History_Job_ID)+'*********************************')
								log.debug('****************************'+str(History_Job_ID)+'*********************************')
								t = threading.Thread(target=Insert_JobStatus,args=(Id,History_Job_ID,ob.JobName,ob,'Schedule',))
								t.setDaemon(True)
								t.start()
						else:
							print('Jobs are disable key '+str(key)+'____Job name -----'+str(ob.JobName))
							log.debug('Jobs are disable key '+str(key)+'____Job name -----'+str(ob.JobName))
					except Exception as er:
						print('Error in foor loop SchedularDaemonProcess matillion  '+str(er))
						log.debug('Error in foor loop SchedularDaemonProcess matillion  '+str(er))

		except Exception as E:
			print('Exception in SchedularDaemonProcess matillion '+str(E))
			log.debug('Exception in SchedularDaemonProcess matillion '+str(E))


		time.sleep(60)





def SchedularDaemonProcess_Python():
	StartPythonJobUtil()
	while True :
		# Logic to find next date minutes 


		day_name=GetDayName()
		

		Hours_name=GetHour()
		Min_name=GetMin()

		key=str(day_name).lower()+'_'+str(int(Hours_name))+'_'+str(int(Min_name))
		print('SchedularDaemonProcess_Python key-----------'+key)
		log.debug('SchedularDaemonProcess_Python key-----------'+key)
		'''
		#start print Information comment it later
		for jobsprint in JobMapping:
			output=JobMapping[jobsprint]
			if type(output) is list:
				jlist=output
				for jobj in jlist:
					print("Print objects Information(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
					print(jobj)
					print(jobj.JobName)
					print(jobj.projectName)
					print(jobj.version)
					print(jobj.user)
					print(jobj.password)
					print(jobj.Environment)
					print(jobj.Enable)
					print(jobj.Day_of_Week)
					print(jobj.Hours)
					print(jobj.Minutes)
					print(jobj.EndDate)
					print(jobj.id)
					print('now date---------'+str(dt.now(timezone('Asia/Kolkata')).strftime('%Y-%m-%d')))
					if str(jobj.EndDate)==dt.now(timezone('Asia/Kolkata')).strftime('%Y-%m-%d'):
						print('match')
					else:
						print('do not match')
			else:
					print("èlse Print objects Information(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
					print(output)
					print(output.JobName)
					print(output.projectName)
					print(output.version)
					print(output.user)
					print(output.password)
					print(output.Environment)
					print(output.Enable)
					print(output.Day_of_Week)
					print(output.Hours)
					print(output.Minutes)
					print(output.EndDate)
					print(jobj.id)

		

			
			
		#End Print
		'''
		
		try:

			if key in PythonJobMapping:
				ObjectList=PythonJobMapping[key]
				print('********************in if************************************** '+str(ObjectList))
				print('ObjectList------'+str(ObjectList))
				log.debug('********************in if************************************** '+str(ObjectList))
				log.debug('ObjectList------'+str(ObjectList))
				for ob in ObjectList:

					try:
						if ob.Enable==True:
							if str(ob.EndDate)==GetDate_YMD():
								objid=ob.id
								print('objid********************************'+str(objid))
								log.debug('objid********************************'+str(objid))
								PythonJobInformations.objects.filter(id=objid).update(Enable=False)
								StartPythonJobUtil()
								#return render(request,"matillionjobs.html",{"obj":obj})
							
							else:
								print('Else In SchedularDaemonProcess_Python')
								print('Calling CallPythonJob forob.JobName '+str(ob.JobName))
								log.debug('Else In SchedularDaemonProcess_Python')
								log.debug('Calling CallPythonJob forob.JobName '+str(ob.JobName))
								History_Job_ID=str(ob.JobName)+'_'+str(key.split('_')[1])+'_'+str(key.split('_')[2])

								print('****************************'+str(History_Job_ID)+'*********************************')
								log.debug('****************************'+str(History_Job_ID)+'*********************************')
								startTime=GetStartEndDateDate()
								RunDate=GetRunDate()

								t = threading.Thread(target=Insert_JobStatus_python,args=(History_Job_ID,ob.JobName,startTime,RunDate,'Schedule',))
								t.setDaemon(True)
								t.start()
								
						else:
							print('Jobs are disable key '+str(key)+'____Job name -----'+str(ob.JobName))
							log.error('Jobs are disable key '+str(key)+'____Job name -----'+str(ob.JobName))
					except Exception as e:
						print('Error in For loop SchedularDaemonProcess_Python '+str(e))
						log.error('Error in For loop SchedularDaemonProcess_Python '+str(e))

		except Exception as E:
			print('Error in SchedularDaemonProcess_Python '+str(E))
			log.error('Error in SchedularDaemonProcess_Python '+str(E))



		time.sleep(60)




def SchedularDaemonProcess_Talend():
	StartTalendJobUtil()
	while True :
		# Logic to find next date minutes 


		day_name=GetDayName()
		

		Hours_name=GetHour()
		Min_name=GetMin()

		key=str(day_name).lower()+'_'+str(int(Hours_name))+'_'+str(int(Min_name))
		print('SchedularDaemonProcess_Talend key-----------'+key)
		log.debug('SchedularDaemonProcess_Talend key-----------'+key)
		'''
		#start print Information comment it later
		for jobsprint in JobMapping:
			output=JobMapping[jobsprint]
			if type(output) is list:
				jlist=output
				for jobj in jlist:
					print("Print objects Information(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
					print(jobj)
					print(jobj.JobName)
					print(jobj.projectName)
					print(jobj.version)
					print(jobj.user)
					print(jobj.password)
					print(jobj.Environment)
					print(jobj.Enable)
					print(jobj.Day_of_Week)
					print(jobj.Hours)
					print(jobj.Minutes)
					print(jobj.EndDate)
					print(jobj.id)
					print('now date---------'+str(dt.now(timezone('Asia/Kolkata')).strftime('%Y-%m-%d')))
					if str(jobj.EndDate)==dt.now(timezone('Asia/Kolkata')).strftime('%Y-%m-%d'):
						print('match')
					else:
						print('do not match')
			else:
					print("èlse Print objects Information(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
					print(output)
					print(output.JobName)
					print(output.projectName)
					print(output.version)
					print(output.user)
					print(output.password)
					print(output.Environment)
					print(output.Enable)
					print(output.Day_of_Week)
					print(output.Hours)
					print(output.Minutes)
					print(output.EndDate)
					print(jobj.id)

		

			
			
		#End Print
		'''
		
		try:


			if key in TalendJobMapping:
				ObjectList=TalendJobMapping[key]
				print('********************in if************************************** '+str(ObjectList))
				print('ObjectList------'+str(ObjectList))
				log.debug('********************in if************************************** '+str(ObjectList))
				log.debug('ObjectList------'+str(ObjectList))
				for ob in ObjectList:
					try:
						if ob.Enable==True:
							if str(ob.EndDate)==GetDate_YMD():
								objid=ob.id
								print('objid********************************'+str(objid))
								log.debug('objid********************************'+str(objid))
								TalendJobInformations.objects.filter(id=objid).update(Enable=False)
								StartTalendJobUtil()
								#return render(request,"matillionjobs.html",{"obj":obj})
							
							else:
								print('Else In SchedularDaemonProcess_Talend')
								print('Calling CallTalend forob.JobName '+str(ob.JobName))
								log.debug('Else In SchedularDaemonProcess_Talend')
								log.debug('Calling CallTalend forob.JobName '+str(ob.JobName))
								History_Job_ID=str(ob.JobName)+'_'+str(key.split('_')[1])+'_'+str(key.split('_')[2])

								print('****************************'+str(History_Job_ID)+'*********************************')
								log.debug('****************************'+str(History_Job_ID)+'*********************************')
								startTime=GetStartEndDateDate()
								RunDate=GetRunDate()
								try:
									t = threading.Thread(target=Insert_JobStatus_Talend,args=(History_Job_ID,ob.JobName,startTime,RunDate,ob.EndPoint,'Schedule'))
									t.setDaemon(True)
									t.start()
								except Exception as Et:
									log.error('Error in SchedularDaemonProcess_Talend in Thread ' +str(Et))
									print('Error in SchedularDaemonProcess_Talend in Thread ' +str(Et))
								
						else:
							print('Jobs are disable key '+str(key)+'____Job name -----'+str(ob.JobName))
							log.error('Jobs are disable key '+str(key)+'____Job name -----'+str(ob.JobName))
					except Exception as Ee:
						print('Error in loop SchedularDaemonProcess_Talend '+str(Ee))
						log.error('Error in loop SchedularDaemonProcess_Talend '+str(Ee))
		except Exception as Err:
			print('Exception in SchedularDaemonProcess_Talend '+str(Err))
			log.error('Exception in SchedularDaemonProcess_Talend '+str(Err))

		time.sleep(60)


#######################################################################################################################


#####################################################################################################################

flag=False
Python_flag=False
Talend_flag=False
Custom_flag=False

##########################################################################################################################






####################################################################################################


def StartMatilionJobUtil():
	try:
		JobMapping.clear()

		obj=MatillionJobInformation.objects.all().order_by('-id')#JobMapping={}
		print('JobMapping=-----'+str(JobMapping))
		log.debug('JobMapping=-----'+str(JobMapping))

		for i in obj:
			print(i.JobName)
			print(i.projectName)
			print(i.version)
			print(i.user)
			print(i.password)
			print(i.Environment)
			print(i.Enable)
			print(i.Day_of_Week)
			print(int(i.Hours))
			print(int(i.Minutes))
			if i.Enable==True or i.Enable==False:
				print('calling StartMatilionJobUtil for '+str(i.JobName))
				log.debug('calling StartMatilionJobUtil for '+str(i.JobName))
				days=i.Day_of_Week.split(',')
				print('days---'+str(days))
				log.debug('days---'+str(days))
				for day_val in days:
					day_val=str(day_val).lower()
					if str(day_val)+'_'+str(int(i.Hours))+'_'+str(int(i.Minutes)) in JobMapping:

						li=JobMapping[str(day_val)+'_'+str(int(i.Hours))+'_'+str(int(i.Minutes))]
						i.Day_of_Week=day_val
						for kk in li:
							if kk.JobName !=i.JobName:
								li.append(i)
								JobMapping[str(day_val)+'_'+str(int(i.Hours))+'_'+str(int(i.Minutes))]=li
						print('if after append JobMapping----'+str(JobMapping))
						log.debug('if after append JobMapping----'+str(JobMapping))
					else:
						i.Day_of_Week=day_val
						JobMapping[str(day_val)+'_'+str(int(i.Hours))+'_'+str(int(i.Minutes))]=[i]
						print('else after append JobMapping----'+str(JobMapping))
						log.debug('else after append JobMapping----'+str(JobMapping))
	except Exception as E:
		print('Error in StartMatilionJobUtil  '+str(E))
		log.error('Error in StartMatilionJobUtil  '+str(E))

def StartPythonJobUtil():
	try:
		PythonJobMapping.clear()

		obj=PythonJobInformations.objects.all().order_by('-id')#JobMapping={}
		print('PythonJobMapping=-----'+str(PythonJobMapping))
		log.debug('PythonJobMapping=-----'+str(PythonJobMapping))

		for i in obj:
			print(i.JobName)
			
			
			
			
			
			print(i.Enable)
			print(i.Day_of_Week)
			print(int(i.Hours))
			print(int(i.Minutes))
			if i.Enable==True or i.Enable==False:
				print('calling StartPythonJobUtil for '+str(i.JobName))
				log.debug('calling StartPythonJobUtil for '+str(i.JobName))
				days=i.Day_of_Week.split(',')
				print('days---'+str(days))
				log.debug('days---'+str(days))
				for day_val in days:
					day_val=str(day_val).lower()
					if str(day_val)+'_'+str(int(i.Hours))+'_'+str(int(i.Minutes)) in PythonJobMapping:

						li=PythonJobMapping[str(day_val)+'_'+str(int(i.Hours))+'_'+str(int(i.Minutes))]
						i.Day_of_Week=day_val
						for kk in li:
							if kk.JobName !=i.JobName:
								li.append(i)
								PythonJobMapping[str(day_val)+'_'+str(int(i.Hours))+'_'+str(int(i.Minutes))]=li
						print('if after append PythonJobMapping----'+str(PythonJobMapping))
						log.debug('if after append PythonJobMapping----'+str(PythonJobMapping))
					else:
						i.Day_of_Week=day_val
						PythonJobMapping[str(day_val)+'_'+str(int(i.Hours))+'_'+str(int(i.Minutes))]=[i]
						print('else after append PythonJobMapping----'+str(PythonJobMapping))
						log.debug('else after append PythonJobMapping----'+str(PythonJobMapping))
	except Exception as E:
		print('Error in StartPythonJobUtil '+str(E))
		log.debug('Error in StartPythonJobUtil '+str(E))



def StartTalendJobUtil():
	try:
		TalendJobMapping.clear()

		obj=TalendJobInformations.objects.all().order_by('-id')#JobMapping={}
		print('TalendJobMapping=-----'+str(TalendJobMapping))
		log.debug('TalendJobMapping=-----'+str(TalendJobMapping))

		for i in obj:
			print(i.JobName)
			
			
			
			
			
			print(i.Enable)
			print(i.Day_of_Week)
			print(int(i.Hours))
			print(int(i.Minutes))
			if i.Enable==True or i.Enable==False:
				print('calling StartTalendJobUtil for '+str(i.JobName))
				log.debug('calling StartTalendJobUtil for '+str(i.JobName))
				days=i.Day_of_Week.split(',')
				print('days---'+str(days))
				log.debug('days---'+str(days))
				for day_val in days:
					day_val=str(day_val).lower()

					if str(day_val)+'_'+str(int(i.Hours))+'_'+str(int(i.Minutes)) in TalendJobMapping:

						li=TalendJobMapping[str(day_val)+'_'+str(int(i.Hours))+'_'+str(int(i.Minutes))]
						i.Day_of_Week=day_val
						for kk in li:
							if kk.JobName !=i.JobName:
								li.append(i)
								TalendJobMapping[str(day_val)+'_'+str(int(i.Hours))+'_'+str(int(i.Minutes))]=li
						print('if after append TalendJobMapping----'+str(TalendJobMapping))
						log.debug('if after append TalendJobMapping----'+str(TalendJobMapping))
					else:
						i.Day_of_Week=day_val
						TalendJobMapping[str(day_val)+'_'+str(int(i.Hours))+'_'+str(int(i.Minutes))]=[i]
						print('else after append TalendJobMapping----'+str(TalendJobMapping))
						log.debug('else after append TalendJobMapping----'+str(TalendJobMapping))

	except Exception as E:
		print('Error in StartTalendJobUtil '+str(E))
		log.debug('Error in StartTalendJobUtil '+str(E))

####################################################################################################


###################################################################################################################################
@receiver(post_save, sender=MatillionJobInformation)
def my_handler(sender, **kwargs):
    print('$$$$$$$$$$$$$$$$$$$$$$$$$post save callback$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    log.debug('my_handler--> post_save --->MatillionJobInformation ')
    StartMatilionJobUtil()

@receiver(post_save, sender=PythonJobInformations)
def my_handler_receiver(sender, **kwargs):
    print('$$$$$$$$$$$$$$$$$$$$$$$$$post save callback for PythonJobInformations $$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    log.debug('my_handler--> post_save --->PythonJobInformations ')
    StartPythonJobUtil()

@receiver(post_save, sender=TalendJobInformations)
def my_handler_receiver_talend(sender, **kwargs):
    print('$$$$$$$$$$$$$$$$$$$$$$$$$post save callback for TalendJobInformations $$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    log.debug('my_handler--> post_save --->TalendJobInformations ')
    print(str(sender.id)+'*************************************')
    print(TalendJobInformations.id)
    StartTalendJobUtil()

@receiver(post_save, sender=CustomJobInformations)
def my_handler_receiver_custom(sender, **kwargs):
    print('$$$$$$$$$$$$$$$$$$$$$$$$$post save callback for CustomJobInformations $$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    log.debug('my_handler--> post_save --->CustomJobInformations ')
    StartCustomJobUtil()



###################################################################################################################################




################################################################################
def StartMatilionJob(request,*args,**kwargs):
	
	
	global flag
	obj=MatillionJobInformation.objects.all().order_by('-id')
	print(obj[0].JobName)
	if flag==False:
		flag=True
		try:
			t = threading.Thread(target=SchedularDaemonProcess)
			t.setDaemon(True)
			t.start()
		except Exception as E:
			log.error('Error in StartMatilionJob  While calling SchedularDaemonProcess '+str(E))
			print('Error in StartMatilionJob  While calling SchedularDaemonProcess '+str(E))
	return HttpResponse("data")

def StartPythonJob(request,*args,**kwargs):
	
	
	global Python_flag
	obj=PythonJobInformations.objects.all().order_by('-id')
	print(obj[0].JobName)
	if Python_flag==False:
		Python_flag=True
		try:
			t = threading.Thread(target=SchedularDaemonProcess_Python)
			t.setDaemon(True)
			t.start()
		except Exception as E:
			print('Error in StartPythonJob  While calling SchedularDaemonProcess_Python '+str(E))
			log.error('Error in StartPythonJob  While calling SchedularDaemonProcess_Python '+str(E))
	return HttpResponse("data")




def StartTalendJob(request,*args,**kwargs):
	
	
	
	log.debug('Starting........  StartTalendJob')
	global Talend_flag
	obj=TalendJobInformations.objects.all().order_by('-id')
	print(obj[0].JobName)
	if Talend_flag==False:
		Talend_flag=True
		try:
			t = threading.Thread(target=SchedularDaemonProcess_Talend)
			t.setDaemon(True)
			t.start()
		except Exception as E:
			print('Error in StartTalendJob  While calling SchedularDaemonProcess_Talend '+str(E))
			log.error('Error in StartTalendJob  While calling SchedularDaemonProcess_Talend '+str(E))
	return HttpResponse("data")

	################################################################################








##################################################################################################
def MatillionScedule(request,*args,**kwargs):
	print('*********************************in PythonScedule************************************')
	log.debug('*********************************in PythonScedule************************************')
	try:
		obj=MatillionJobInformation.objects.all().order_by('-id')
		print(obj[0].JobName)
		#StartMatilionJobUtil()
		return render(request,"matillionjobs.html",{"obj":obj})
	except Exception as e:
		print('Error in MatillionScedule '+str(e))
		log.error('Error in MatillionScedule '+str(e))
	

def PythonScedule(request,*args,**kwargs):
	print('*********************************in PythonScedule************************************')
	log.debug('*********************************in PythonScedule************************************')
	try:
		obj=PythonJobInformations.objects.all().order_by('-id')
		print('obj************************'+str(obj))
		print(obj[0].JobName)
		#StartPythonJobUtil()
		return render(request,"PythonJob.html",{"obj":obj})

	except Exception as e:
		print('Error in PythonScedule '+str(e))
		log.error('Error in PythonScedule '+str(e))


def TalendScedule(request,*args,**kwargs):
	print('*********************************in PythonScedule************************************')
	log.debug('*********************************in PythonScedule************************************')
	try:
		obj=TalendJobInformations.objects.all().order_by('-id')
		print('obj************************'+str(obj))
		print(obj[0].JobName)
		#StartTalendJobUtil()
		return render(request,"TalendJobs.html",{"obj":obj})
	except Exception as e:
		print('Error in TalendScedule '+str(e))
		log.error('Error in TalendScedule '+str(e))
	

#################################################################################################


def SeeMatHistory(request,*args,**kwargs):
	print('Called ------'+str(request))
	print(request.GET.dict())
	log.debug('Called ------'+str(request))
	log.debug(request.GET.dict())
	history_data=''
	d=request.GET.dict()
	if 'JobID' in d:
		JobID_for_History=d['JobID']
		print('JobID_for_History  ****************'+str(JobID_for_History))
		log.debug('JobID_for_History  ****************'+str(JobID_for_History))
		history_data=Matilion_Run_JobHistory.objects.filter(JobID=JobID_for_History).order_by('-id')
		print('history_data*********************'+str(history_data))
		log.debug('history_data*********************'+str(history_data))
		l=[]

		for i in history_data:
			data1={'JobID':i.JobID,'JobName':i.JobName,'StartTime':i.StartTime,'EndTime':i.EndTime,'Status':i.Status,'Sche_or_Manu':i.Sche_or_Manu,'description':i.description}
			l.append(data1)
	return HttpResponse(json.dumps({'history_data': l}), content_type="application/json")



def SeePythonHistory(request,*args,**kwargs):
	print('SeePythonHistory Called ------'+str(request))
	print(request.GET.dict())
	log.debug('SeePythonHistory Called ------'+str(request))
	log.debug(request.GET.dict())
	history_data=''
	d=request.GET.dict()
	if 'JobID' in d:
		JobID_for_History=d['JobID']
		print('JobID_for_History  SeePythonHistory  ****************'+str(JobID_for_History))
		log.debug('JobID_for_History  SeePythonHistory  ****************'+str(JobID_for_History))
		history_data=Python_Run_JobHistory.objects.filter(JobID=JobID_for_History).order_by('-id')
		print('SeePythonHistory history_data*********************'+str(history_data))
		log.debug('SeePythonHistory history_data*********************'+str(history_data))
		l=[]

		for i in history_data:
			data1={'JobID':i.JobID,'JobName':i.JobName,'StartTime':i.StartTime,'EndTime':i.EndTime,'Status':i.Status,'Sche_or_Manu':i.Sche_or_Manu,'description':i.description}
			l.append(data1)
	return HttpResponse(json.dumps({'history_data': l}), content_type="application/json")



def SeeTalendHistory(request,*args,**kwargs):
	print('SeePythonHistory Called ------'+str(request))
	print(request.GET.dict())
	log.debug('SeePythonHistory Called ------'+str(request))
	log.debug(request.GET.dict())
	history_data=''
	d=request.GET.dict()
	if 'JobID' in d:
		JobID_for_History=d['JobID']
		print('JobID_for_History  SeePythonHistory  ****************'+str(JobID_for_History))
		log.debug('JobID_for_History  SeePythonHistory  ****************'+str(JobID_for_History))
		history_data=Talend_Run_JobHistory.objects.filter(JobID=JobID_for_History).order_by('-id')
		print('SeePythonHistory history_data*********************'+str(history_data))
		log.debug('SeePythonHistory history_data*********************'+str(history_data))
		l=[]

		for i in history_data:
			data1={'JobID':i.JobID,'JobName':i.JobName,'StartTime':i.StartTime,'EndTime':i.EndTime,'Status':i.Status,'Sche_or_Manu':i.Sche_or_Manu,'description':i.description}
			l.append(data1)
	return HttpResponse(json.dumps({'history_data': l}), content_type="application/json")


	###########################################################################################################################



def CustomJob(request,*args,**kwargs):
	print(request.GET.dict())
	dic=request.GET.dict()
	if 'ID' in dic:
		ID=dic['ID']
		obj=CustomJobInformations.objects.filter(id=ID)
		data=''
		JobName=''
		Day_of_Week=''
		Hours=''
		Minutes=''
		Enable=''
		for i in obj:
			data=i.HtmlData
			JobName=i.JobName
			Day_of_Week=i.Day_of_Week
			Hours=i.Hours
			Minutes=i.Minutes
			Enable=i.Enable
			MatIP=i.MatIP
			MatGroup=i.MatGroup
			MatProject=i.MatProject
			MatVersion=i.MatVersion
			MatEnvironment=i.MatEnvironment


		#print('MatIP----'+str(MatIP))

		#print(data)
		log.debug(data)
		return render(request,"create_custom.html",{"data":data,"JobName_P":JobName,"Day_of_Week":Day_of_Week,"Hours_p":Hours,"Minutes_P":Minutes,"Enable_P":Enable,"MatIP":MatIP,"MatGroup":MatGroup,"MatProject":MatProject,"MatVersion":MatVersion,"MatEnvironment":MatEnvironment})
	else:
		return render(request,"create_custom.html",{"data":''})

def GetCustomJobInfo(request,*args,**kwargs):
	dic=request.GET.dict()
	print(dic)
	log.debug(dic)
	Com_Seq=dic['Com_Seq']
	Com_Seq=Com_Seq.replace('[','').replace(']','').replace('"','').split(',')
	print('Com_Seq  '+str(Com_Seq))
	log.debug('Com_Seq  '+str(Com_Seq))
	Com_info=json.loads(dic['Com_info'])
	print('Com_info  '+str(Com_info))
	log.debug('Com_info  '+str(Com_info))

	count=0
	Final_data=''
	for typeofcomp in Com_Seq:
		if typeofcomp=='python':
			print(Com_info[str(count)][0])
			log.debug(Com_info[str(count)][0])
			Final_data=Final_data+Com_info[str(count)][0]+'%^*'
		elif typeofcomp=='talend':
			print(Com_info[str(count)][0])
			log.debug(Com_info[str(count)][0])
			Final_data=Final_data+Com_info[str(count)][0]+'%^*'
		elif typeofcomp=='matillion':
			print(Com_info[str(count)]['server'])
			print(Com_info[str(count)]['GroupName'])
			print(Com_info[str(count)]['ProjectName'])
			print(Com_info[str(count)]['Version'])
			print(Com_info[str(count)]['JobName'])
			log.debug(Com_info[str(count)]['JobName'])
			print(Com_info[str(count)]['Environment'])
			Final_data=Final_data+str(Com_info[str(count)])+'%^*'
		count =count+1

	JobName_P=dic['JobName']
	days_P=dic['days']
	#days_P=days_P.split(',')
	Hours_P=dic['Hours']
	Minutes_P=dic['Minutes']
	Enable_P=dic['Enable']
	MatIP=dic['MatIP']
	MatGroup=dic['MatGroup']
	MatProject=dic['MatProject']
	MatVersion=dic['MatVersion']
	MatEnvironment=dic['MatEnvironment']




	final_comp=''
	for comp in Com_Seq:
		if comp=='':
			continue
		final_comp=final_comp+comp+'$*'

	if 'IDURL' in dic:
		IDURL=dic['IDURL']
		print(IDURL)
		log.debug(IDURL)
		if IDURL:
			print('In IF IDURL')
			log.debug('In IF IDURL')
			CustomJobInformations.objects.filter(id=int(IDURL)).update(JobName=JobName_P,Enable=Enable_P,Day_of_Week=days_P,Hours=Hours_P,Minutes=Minutes_P,HtmlData=dic['output'],Comp_Seq=final_comp,Comp_Data=Final_data
					,MatIP=MatIP,MatGroup=MatGroup,MatProject=MatProject,MatVersion=MatVersion,MatEnvironment=MatEnvironment
					)
				
		else:
			print('In else IDURL')
			log.debug('In else IDURL')
			CustomJobInformations.objects.create(JobName=JobName_P,HtmlData=dic['output'],Comp_Seq=final_comp,Comp_Data=Final_data,Enable=Enable_P,Day_of_Week=days_P,Hours=Hours_P,Minutes=Minutes_P,MatIP=MatIP,MatGroup=MatGroup,MatProject=MatProject,MatVersion=MatVersion,MatEnvironment=MatEnvironment)
	else:
		print('In else 2 IDURL')
		log.debug('In else 2 IDURL')
		CustomJobInformations.objects.create(JobName=JobName_P,HtmlData=dic['output'],Comp_Seq=final_comp,Comp_Data=Final_data,Enable=Enable_P,Day_of_Week=days_P,Hours=Hours_P,Minutes=Minutes_P,MatIP=MatIP,MatGroup=MatGroup,MatProject=MatProject,MatVersion=MatVersion,MatEnvironment=MatEnvironment)

	


	StartCustomJobUtil()
	return HttpResponse('hey')





def CustomJobSee(request,*args,**kwargs):
	obj=CustomJobInformations.objects.all().order_by('-id')
	return render(request,"CustomJobSee.html",{"obj":obj})


def insert_history_custom(row,status,startTime,Sche_or_Manu,description):
	Custom_Run_JobHistory.objects.create(JobID=row.id,JobName=row.JobName,StartTime=startTime,EndTime=GetStartEndDateDate(),Status=status,RunDate=GetRunDate(),Sche_or_Manu=Sche_or_Manu,description=description)


def RunCustomJobNow_util(JobName,Comp_Seq,Comp_Data,row,Sche_or_Manu):

	try:
		print('RunCustomJobNow_util   JobName'+str(JobName))
		log.debug('RunCustomJobNow_util   JobName'+str(JobName))
		print('Comp_Seq-------'+str(Comp_Seq))
		log.debug('Comp_Seq-------'+str(Comp_Seq))
		Comp_Seq=Comp_Seq.split('$*')
		Comp_Data=Comp_Data.split('%^*')
		cnt=0
		final_status='FAILED'
		startTime=GetStartEndDateDate()
		RunDate=GetRunDate()
		for type_comp in Comp_Seq:
			if type_comp=='':
				cnt=cnt+1
				continue

			print('&&&&&&&&&&&&&&&&&&&    type_comp '+str(type_comp))
			log.debug('&&&&&&&&&&&&&&&&&&&    type_comp '+str(type_comp))
			if type_comp=='python':
				PythonFileName=Comp_Data[cnt]
				try:
					status=CallPythonJob(PythonFileName+'.py')
					print(status)
					if status==0:

						print('*****************There Is SUCCESS in python Job ********************** '+str(status))
						log.debug('*****************There Is SUCCESS in python Job ********************** '+str(status))
						cnt=cnt+1
						final_status='SUCCESS'
						continue
					else:
						print('*****************There Is Error in python Job ********************** '+str(status))
						log.error('*****************There Is Error in python Job ********************** '+str(status))
						#Update the Job Status Here By Inserting Status in Table
						#####################################################
						#####################################################
						
						final_status='Failed at python Component Number : '+str(cnt+1)+'  '+str(status)
						insert_history_custom(row,'FAILED',startTime,Sche_or_Manu,final_status)
						return

				except Exception as err:
					print('Exception in python Component '+str(err))
					log.error('Exception in python Component '+str(err))
					final_status='Exception at talend Component Number : '+str(cnt+1)+'    '+str(err)
					insert_history_custom(row,'FAILED',startTime,Sche_or_Manu,final_status)
					return

					#return final_status

			elif type_comp=='talend':
				try:
					TalendEndPoint=Comp_Data[cnt]
					status=CallTalendJob(TalendEndPoint)
					if status=='0':
						print('*****************There Is SUCCESS in Talend Job ********************** '+str(status))
						log.debug('*****************There Is SUCCESS in Talend Job ********************** '+str(status))
						cnt=cnt+1
						final_status='SUCCESS'
						continue
					else:
						print('*****************There Is Error in Talend Job ********************** '+str(status))
						log.error('*****************There Is Error in Talend Job ********************** '+str(status))
						#Update the Job Status Here By Inserting Status in Table
						#####################################################
						#####################################################
						
						final_status='Failed  Talend Component at '+str(cnt+1)+' '+str(status)
						insert_history_custom(row,'FAILED',startTime,Sche_or_Manu,final_status)
						return
						
				except Exception as E:
					print('Exception in talend Component '+str(E))
					log.error('Exception in talend Component '+str(E))
					final_status='Exception  in talend Component at '+str(cnt+1)+'  '+str(E)
					insert_history_custom(row,'FAILED',startTime,Sche_or_Manu,final_status)
					return


			elif type_comp=='matillion':
				MatObj=Comp_Data[cnt]
				MatObj=MatObj.replace('\'','\"')
				MatObj=json.loads(MatObj)
				print(MatObj)
				server=MatObj['server']
				GroupName=MatObj['GroupName']
				ProjectName=MatObj['ProjectName']
				Version=MatObj['Version']
				JobName=MatObj['JobName']
				Environment=MatObj['Environment']
				print('server---GroupName---ProjectName---Version---JobName---Environment    '+str(server)+str('----')+str(GroupName)+str('----')+str(ProjectName)+str('----')+str(Version)+str('----')+str(JobName)+str('----')+str(Environment))
				#log.debug('server---GroupName---ProjectName---Version---JobName---Environment    '+str(server)+str('----')+str(GroupName)+str('----')+str(ProjectName)+str('----')+str(Version)+str('----')+str(JobName)+str('----')+str(Environment))
				#Add Remove Hardcoded IP and Group Name from call_mat(JobName,projectName,version,user,password,Environment,)
				try:
					id=call_mat(JobName,row.MatIP,row.MatGroup,row.MatProject,row.MatVersion,row.user,row.password,row.MatEnvironment)
					status=checkStatus(id,row.MatIP,row.user,row.password)
				except Exception as matexcep:
					print('Error Occur in matillion Component '+str(matexcep))
					log.error('Error Occur in matillion Component '+str(matexcep))
					final_status='Error Occur in matillion Component at '+str(cnt+1)+' '+str(matexcep)
					insert_history_custom(row,'FAILED',startTime,Sche_or_Manu,final_status)
					return


				while True:
					try:
						if status=='SUCCESS' or status=='FAILED':
							if status=='SUCCESS':
								cnt=cnt+1
								final_status='SUCCESS'
								break
								print('*****************There Is SUCCESS in matillion Job ********************** '+str(status))
								log.info('*****************There Is SUCCESS in matillion Job ********************** '+str(status))
							elif status=='FAILED':
								print('*****************There Is FAILED in matillion Job ********************** '+str(status))
								log.error('*****************There Is FAILED in matillion Job ********************** '+str(status))

								#Update the Job Status Here By Inserting Status in Table
								#####################################################
								#####################################################
								final_status='Error In matillion Component at '+str(cnt+1)
								
								insert_history_custom(row,'FAILED',startTime,Sche_or_Manu,final_status)
								return
								#return 'FAILED'
						else:
							status=checkStatus(id,row.MatIP,row.user,row.password)
					except Exception as errfor:
						print('Error in While loop errfor '+str(errfor))
						log.error('Error in While loop errfor '+str(errfor))
						final_status='Error In matillion Component at '+str(cnt+1)
						insert_history_custom(row,'FAILED',startTime,Sche_or_Manu,final_status)
						return

					time.sleep(30)
			else:
				print('Invalid Component ******************** '+str(type_comp))
				log.error('Invalid Component ******************** '+str(type_comp))
				return

		if final_status=='SUCCESS':
			
			insert_history_custom(row,'SUCCESS',startTime,Sche_or_Manu,final_status)
			return
			
		else:
			insert_history_custom(row,'FAILED',startTime,Sche_or_Manu,'--')
			return
			
	except Exception as e:
		print('Error in RunCustomJobNow_util '+str(e))
		log.error('Error in RunCustomJobNow_util '+str(e))
		final_status='Exception In Job : '+str(e)
		insert_history_custom(row,'FAILED',startTime,Sche_or_Manu,final_status)
		return
		
		



def RunCustomJobNow(request,*args,**kwargs):
	dic=request.GET.dict()
	print(dic)
	try:
		if 'ID' in dic:
			ID=dic['ID']
			obj=CustomJobInformations.objects.filter(id=ID)
			for row in obj:
				print(row.JobName)
				print(row.Comp_Seq)
				print(row.Comp_Data)
				print(row.Day_of_Week)
				print(row.Hours)
				print(row.Minutes)
				t = threading.Thread(target=RunCustomJobNow_util,args=(row.JobName,row.Comp_Seq,row.Comp_Data,row,'Manual',))
				t.setDaemon(True)
				t.start()

		else:
			print('ID Not found')
			log.error('ID Not found')
	except Exception as E:
		print('Error in RunCustomJobNow '+str(E))
		log.error('Error in RunCustomJobNow '+str(E))

	return HttpResponse('data from RunCustomJobNow')



def StartCustomJobUtil():
	try:
		CustomJobMapping.clear()

		obj=CustomJobInformations.objects.all().order_by('-id')#JobMapping={}
		print('CustomJobMapping=-----'+str(CustomJobMapping))
		log.debug('CustomJobMapping=-----'+str(CustomJobMapping))

		for i in obj:
			
			print(i.id)
			
			if i.Enable==True:
				print('calling StartCustomJobUtil for '+str(i.JobName))
				log.debug('calling StartCustomJobUtil for '+str(i.JobName))
				days=i.Day_of_Week.split(',')
				print('days---'+str(days))
				log.debug('days---'+str(days))
				for day_val in days:
					day_val=str(day_val).lower()
					if str(day_val)+'_'+str(i.Hours)+'_'+str(i.Minutes) in CustomJobMapping:

						li=CustomJobMapping[str(day_val)+'_'+str(i.Hours)+'_'+str(i.Minutes)]
						i.Day_of_Week=day_val
						li.append(i.id)
						CustomJobMapping[str(day_val)+'_'+str(i.Hours)+'_'+str(i.Minutes)]=li
						print('if after append CustomJobMapping----'+str(CustomJobMapping))
						log.debug('if after append CustomJobMapping----'+str(CustomJobMapping))
					else:
						i.Day_of_Week=day_val
						CustomJobMapping[str(day_val)+'_'+str(i.Hours)+'_'+str(i.Minutes)]=[i.id]
						print('else after append CustomJobMapping----'+str(CustomJobMapping))
						log.debug('else after append CustomJobMapping----'+str(CustomJobMapping))
	except Exception as E:
		print('Error in StartCustomJobUtil '+str(E))
		log.error('Error in StartCustomJobUtil '+str(E))



def StartCustomJob(request,*args,**kwargs):
	
	
	global Custom_flag
	try:
		obj=CustomJobInformations.objects.all().order_by('-id')
		print(obj[0].JobName)
		if Custom_flag==False:
			Custom_flag=True
			t = threading.Thread(target=SchedularDaemonProcess_Custom)
			t.setDaemon(True)
			t.start()
	except Exception as E:
		print('Error in StartCustomJob '+str(E))
		log.error('Error in StartCustomJob '+str(E))
	return HttpResponse("data")




def SchedularDaemonProcess_Custom():
	try:
		StartCustomJobUtil()
	except Exception as E:
		print('Error in SchedularDaemonProcess_Custom ---> StartCustomJobUtil '+str(E) )
		log.error('Error in SchedularDaemonProcess_Custom ---> StartCustomJobUtil '+str(E) )
	
	while True :
		# Logic to find next date minutes 
		try:

			day_name=GetDayName()
			

			Hours_name=GetHour()
			Min_name=GetMin()

			key=day_name+'_'+Hours_name+'_'+str(int(Min_name))
			print('SchedularDaemonProcess_Custom key-----------'+key)
			log.debug('SchedularDaemonProcess_Custom key-----------'+key)
					


			if key in CustomJobMapping:
				ObjectList=CustomJobMapping[key]
				print('********************in if************************************** '+str(ObjectList))
				log.debug('********************in if************************************** '+str(ObjectList))
				print('ObjectList------'+str(ObjectList))
				log.debug('ObjectList------'+str(ObjectList))
				for ob in ObjectList:
					obj=CustomJobInformations.objects.filter(id=ob)
					for i in obj:
						if str(i.EndDate)==GetDate_YMD():
							CustomJobInformations.objects.filter(id=i.id).update(Enable=False)
							print(' if i.EndDate)==dt.now(timezone    ')
							log.debug(' if i.EndDate)==dt.now(timezone    ')
							StartCustomJobUtil()
							#return render(request,"matillionjobs.html",{"obj":obj})
						else:
							print('Else In SchedularDaemonProcess_Custom')
							log.debug('Else In SchedularDaemonProcess_Custom')
							print('Calling SchedularDaemonProcess_Custom forob.JobName '+str(i))
							log.debug('Calling SchedularDaemonProcess_Custom forob.JobName '+str(i))
							#History_Job_ID=str(ob.JobName)+'_'+str(key.split('_')[1])+'_'+str(key.split('_')[2])
							ID=i.id
							try:
								obj=CustomJobInformations.objects.filter(id=ID)
								for row in obj:
									print(row.JobName)
									print(row.Comp_Seq)
									print(row.Comp_Data)
									print(row.Day_of_Week)
									print(row.Hours)
									print(row.Minutes)
								t = threading.Thread(target=RunCustomJobNow_util,args=(row.JobName,row.Comp_Seq,row.Comp_Data,row,'Schedule',))
								t.setDaemon(True)
								t.start()
							except Exception as errr:
								print('Error in SchedularDaemonProcess_Custom errr '+str(errr))
								log.error('Error in SchedularDaemonProcess_Custom errr '+str(errr))
		except Exception as E:
			print('Error in SchedularDaemonProcess_Custom '+str(E))
			log.error('Error in SchedularDaemonProcess_Custom '+str(E))
				
		time.sleep(60)




def SeeCustomHistory(request,*args,**kwargs):
	print('SeeCustomHistory Called ------'+str(request))
	log.debug('Starting........  SeeCustomHistory')
	log.debug('SeeCustomHistory Called ------'+str(request))
	
	try:
		print(request.GET.dict())
		history_data=''
		d=request.GET.dict()
		if 'JobID' in d:
			JobID_for_History=d['JobID']
			print('JobID_for_History  SeeCustomHistory  ****************'+str(JobID_for_History))
			log.debug('JobID_for_History  SeeCustomHistory  ****************'+str(JobID_for_History))
			history_data=Custom_Run_JobHistory.objects.filter(JobID=JobID_for_History).order_by('-id')
			print('SeeCustomHistory history_data*********************'+str(history_data))
			log.debug('SeeCustomHistory history_data*********************'+str(history_data))
			l=[]

			for i in history_data:
				data1={'JobID':i.JobID,'JobName':i.JobName,'StartTime':i.StartTime,'EndTime':i.EndTime,'Status':i.Status,'Sche_or_Manu':i.Sche_or_Manu,'description':i.description}
				l.append(data1)

			return HttpResponse(json.dumps({'history_data': l}), content_type="application/json")
	except Exception as E:
		print('Error in  SeeCustomHistory '+str(E))
		log.error('Error in  SeeCustomHistory '+str(E))
		l=[]
		return HttpResponse(json.dumps({'history_data': l}), content_type="application/json")
	



#Get all history  data 
def GetHistoryLogs(request,*args,**kwargs):
	obj=Python_Run_JobHistory.objects.all().order_by('-id')
	l=[]

	for i in obj:
		d={'JobType':'PythonJobs','JobID':i.JobID,'JobName':i.JobName,'StartTime':i.StartTime,'EndTime':i.EndTime,'Status':i.Status,'Sche_or_Manu':i.Sche_or_Manu,'description':i.description}
		l.append(d)

	obj=Talend_Run_JobHistory.objects.all().order_by('-id')
	for i in obj:
		d={'JobType':'TalendJobs','JobID':i.JobID,'JobName':i.JobName,'StartTime':i.StartTime,'EndTime':i.EndTime,'Status':i.Status,'Sche_or_Manu':i.Sche_or_Manu,'description':i.description}
		l.append(d)

	obj=Matilion_Run_JobHistory.objects.all().order_by('-id')
	
	for i in obj:
		d={'JobType':'Matillionjobs','JobID':i.JobID,'JobName':i.JobName,'StartTime':i.StartTime,'EndTime':i.EndTime,'Status':i.Status,'Sche_or_Manu':i.Sche_or_Manu,'description':i.description}
		l.append(d)
		
	obj=Custom_Run_JobHistory.objects.all().order_by('-id')
	for i in obj:
		d={'JobType':'CustomJobs','JobID':i.JobID,'JobName':i.JobName,'StartTime':i.StartTime,'EndTime':i.EndTime,'Status':i.Status,'Sche_or_Manu':i.Sche_or_Manu,'description':i.description}
		l.append(d)
	
	return HttpResponse(json.dumps({'history_data': l}), content_type="application/json")
