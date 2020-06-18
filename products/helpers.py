import requests
import subprocess
import urllib.request
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

def call_mat(jobname):
    MatObj=MatillionJobTest()
    MatObj.SetJobName(jobname.replace(' ','%20'))
    a=None
    return subprocess.call('curl -X POST -u '+MatObj.user+':'+MatObj.password+' http://172.31.12.129/rest/v1/group/name/Outbound_Process/project/name/'+MatObj.projectName+'/version/name/'+MatObj.version+'/job/name/'+MatObj.JobName+'/run?environmentName='+MatObj.Environment)


def CallUrl(url):
    url=url
    print(url)
    response =urllib.request.urlopen(url).read().decode('UTF-8')
    print(response)
    return response
