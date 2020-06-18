from apscheduler.scheduler import Scheduler
from .MatilionHelper import checkStatus,call_mat


#s.shutdown()
def job_def(var1):
    print(str(var1))


def start_sch(JobName,projectName,version,user,password,Environment,Day_of_Week,Hours,Minutes):
	s = Scheduler()
	s.add_cron_job(call_mat, args=[JobName,projectName,version,user,password,Environment], day_of_week=Day_of_Week,hour=Hours,minute=Minutes)

	s.start()

def start_sch_mat():
	s.add_cron_job(call_mat, args=['1188802'], second='*/58')

	s.start()

def start_sch_mat1():
	s.add_cron_job(call_mat, args=['1188802'], second='*/58')

	s.start()
