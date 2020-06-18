import requests
import subprocess
import urllib.request
import json
import logging
log = logging.getLogger(__name__)

class MatillionJobTest:
    
    def __init__(self):
        self.user='Test_User3'
        self.password='admin123'
        self.projectName='Outbound_Process'
        self.version='default'
        self.JobName='testjob'
        self.Environment='OutBound'

    def SetJobName(self,JobName):
        self.JobName=JobName

def call_mat_with_less_param(JobName,projectName,version,user,password,Environment,ip,groupname,):
    try:
        print('Calling call_mat_with_less_param for job '+str(JobName))
        log.debug('Calling call_mat_with_less_param for job '+str(JobName))
        MatObj=MatillionJobTest()
        MatObj.SetJobName(JobName.replace(' ','%20'))
        job=JobName.replace(' ','%20')
        a=None
        #return subprocess.call('curl -X POST -u '+MatObj.user+':'+MatObj.password+' http://172.31.12.129/rest/v1/group/name/Outbound_Process/project/name/'+MatObj.projectName+'/version/name/'+MatObj.version+'/job/name/'+MatObj.JobName+'/run?environmentName='+MatObj.Environment)
        url1='http://'+ip+'/rest/v1/group/name/'+groupname+'/project/name/'+projectName+'/version/name/'+version+'/job/name/'+job+'/run?environmentName='+Environment
        print('url1--in call_mat------------'+str(url1))
        log.debug('url1--in call_mat------------'+str(url1))
        auth = (user, password)
        r = requests.post(url1, auth=auth)
        print(r)
        print(json.loads(r.text)['id'])
        ID=json.loads(r.text)['id']
        return ID
    except Exception as E:
        print('Exception in call_mat_with_less_param JobName  '+str(JobName)+str(E))
        log.error('Exception in call_mat_with_less_param JobName  '+str(JobName)+str(E))
        raise Exception(str(E)+  "   Error "+str(JobName))

def call_mat(JobName,Ip,Group,projectName,version,user,password,Environment,):
    try:
        print('Calling call_mat for job '+str(JobName))
        log.debug('Calling call_mat for job '+str(JobName))
        MatObj=MatillionJobTest()
        MatObj.SetJobName(JobName.replace(' ','%20'))
        job=JobName.replace(' ','%20')
        a=None
        #return subprocess.call('curl -X POST -u '+MatObj.user+':'+MatObj.password+' http://172.31.12.129/rest/v1/group/name/Outbound_Process/project/name/'+MatObj.projectName+'/version/name/'+MatObj.version+'/job/name/'+MatObj.JobName+'/run?environmentName='+MatObj.Environment)
        url1='http://'+Ip+'/rest/v1/group/name/'+Group+'/project/name/'+projectName+'/version/name/'+version+'/job/name/'+job+'/run?environmentName='+Environment
        print('url1--in call_mat------------'+str(url1))
        log.debug('url1--in call_mat------------'+str(url1))
        auth = (user, password)
        r = requests.post(url1, auth=auth)
        print(r)
        print(json.loads(r.text)['id'])
        ID=json.loads(r.text)['id']
        print('------------------ID--------------------------'+str(ID))
        log.debug('------------------ID--------------------------'+str(ID))
        return ID
    except Exception as E:
         print('Exception in call_mat JobName  '+str(JobName)+str(E))
         debug.error('Exception in call_mat JobName  '+str(JobName)+str(E))
         raise Exception(str(E)+  "   Error "+str(JobName))


def checkStatus(ID,ip,user,password):
    try:
        print('Called for ID :'+str(ID))
        log.debug('Called for ID :'+str(ID))
        url = 'http://'+str(ip)+'/rest/v0/tasks/'+str(ID)
        auth = (user, password)
        r = requests.get(url, auth=auth)
        response_dict = json.loads(r.text)
        print('response_dict***************'+str(response_dict))
        log.debug('response_dict***************'+str(response_dict))
        d=response_dict['tasks']
        print(len(d))
        log.debug(len(d))
        print(d[len(d)-1]['state'])
        log.debug(d[len(d)-1]['state'])
        print('***************************end *************************')
        log.debug('***************************end *************************')
        return d[len(d)-1]['state']
    except Exception as e:
        print('Exception in checkStatus JobName  '+str(ID)+str(e))
        log.error('Exception in checkStatus JobName  '+str(ID)+str(e))
        raise Exception(str(e)+  "   Error "+str(ID))
    