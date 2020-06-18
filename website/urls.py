from django.contrib import admin
from django.urls import path
from .views import GetHistoryLogs,SeeCustomHistory,StartCustomJob,RunCustomJobNow,CustomJobSee,GetCustomJobInfo,CustomJob,TalendScedule,RunTalendJobNow,StartTalendJob,SeeTalendHistory,index,about,SeePythonHistory,PythonScedule,StartPythonJob,MatillionScedule,SeeMatHistory,RunPythonJobNow,RunMatJobNow,StartMatilionJob


urlpatterns = [
    path('', index,name='index'),

    path('about/', about,name='about'),
   
    
    

    path('MatHistory/', SeeMatHistory,name='test'),
    path('SeePythonHistory/', SeePythonHistory,name='SeePythonHistory'),
    path('SeeTalendHistory/', SeeTalendHistory,name='SeeTalendHistory'),
     

    path('StartMatilionJob/', StartMatilionJob,name='test'),
    path('StartPythonJob/', StartPythonJob,name='StartPythonJob'),
    path('StartTalendJob/', StartTalendJob,name='StartTalendJob'),

    path('RunMatJobNow/', RunMatJobNow,name='test'),
    path('RunPythonJobNow/', RunPythonJobNow,name='RunPythonJobNow'),
    path('RunTalendJobNow/', RunTalendJobNow,name='RunTalendJobNow'),

    path('matillionjobs/', MatillionScedule,name='news'),#Matillion Schedule
    path('pythonjob/', PythonScedule,name='PythonScedule'),
    path('Talendjob/', TalendScedule,name='TalendScedule'),

    path('createcustomjob/', CustomJob,name='CustomJob'),
    path('GetCustomJobInfo/',GetCustomJobInfo,name='GetCustomJobInfo'),
    #path('DrawCustomJobInfo/',DrawCustomJobInfo,name='DrawCustomJobInfo'),
    path('CustomJobSee/',CustomJobSee,name='CustomJobSee'),
    #path('CustomJobDetails/',CustomJobDetails,name='CustomJobDetails'),
    path('RunCustomJobNow/',RunCustomJobNow,name='RunCustomJobNow'),
    path('StartCustomJob/',StartCustomJob,name='StartCustomJob'),
    path('SeeCustomHistory/',SeeCustomHistory,name='SeeCustomHistory'),

    #Get history Data from all 
    path('GetHistoryLogs/',GetHistoryLogs,name='GetHistoryLogs')





]