from apscheduler.scheduler import Scheduler
import time

def job_def1(var1):
    print('in job_def1=--'+str(var1))

def job_def2(var1):
    print('in job_def2---'+str(var1))



f=''

s = Scheduler()
s.start()

def stop():
	s.shutdown()
#stop()

def set_secdule(funname,minute,arg):
	global f
	

	f=s.add_cron_job(funname, args=[arg], day_of_week='mon,tue,wed,thu,fri,sat,sun',second='*/'+str(minute))
	

	print('f---'+str(f))
	

stop()
set_secdule(job_def1,4,'j1')
set_secdule(job_def2,8,'j2')
set_secdule(job_def2,10,'jj3')
set_secdule(job_def2,12,'jj4')
set_secdule(job_def2,14,'jj4t')
f=1
while True:
	f=f+1
	if f>5:
		print('jj')
		s.get_scheduled_jobs()
		#stop()
		#s.start()
	time.sleep(2)