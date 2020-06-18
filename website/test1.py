
from apscheduler.scheduler import Scheduler
import time

def job_def1(var1):
    print('in job_def1=--'+str(var1))

def job_def2(var1):
    print('in job_def2---'+str(var1))



def set_secdule(funname,minute,arg):
	s = Scheduler()
	f=s.add_cron_job(funname, args=[arg], day_of_week='mon,tue,wed,thu,fri,sat,sun',second='*/'+str(minute))
	s.start()
	print('f---'+str(f))


set_secdule(job_def1,6,'j1')
set_secdule(job_def2,8,'j2')
set_secdule(job_def2,10,'jj3')
set_secdule(job_def2,12,'jj4')
f=1
while True:
	f=f+1
	if f>5:
		print('jj')
		
		print(Scheduler.get_jobs())
	time.sleep(2)


	#QA_Daily_EUSS_MDM21_ONEMD Job_22_58 QA_Daily_EUSS_MDM21_ONEMD Job  18-05-2020 22-58-26  18-05-2020 22-58-39 SUCCESS