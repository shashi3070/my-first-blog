from apscheduler.schedulers.background import BackgroundScheduler
import requests

import time

def testfun(var1,var2):
	url1='http://172.31.12.129/rest/v1/group/name/Outbound_Process/project/name/Outbound_Process/version/name/default/job/name/testjob/run?environmentName=OutBound'
	print('url1--in call_mat------------'+str(url1))
	auth = ('Test_User3', 'admin123')
	r = requests.post(url1, auth=auth)

sched = BackgroundScheduler(daemon=True)


def add(fun,id,min):
	f=sched.add_job(fun, 'cron', hour='19',minute=min,id=id, args=['param1', 'param2'])
	print(f)
	
count=1
add(testfun,'s1',28)
add(testfun,'a1',29)
add(testfun,'e1',30)
while True:
	count=count+1
	print('count==='+str(count))
	time.sleep(1)
	if count>10:
		print('in if')
		print(sched.get_job('s1'))
		print(sched.get_job('a1'))
		sched.remove_job('a1')
		print(sched.get_job('e1'))

sched.start()