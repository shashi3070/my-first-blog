from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    name = 'website'
    def ready(self):
        
        
    	from .views import StartTalendJob,StartPythonJob,StartMatilionJob,StartCustomJob
    	print('h************************************************************fhskd  ')
    	StartTalendJob('')
    	StartPythonJob('')
    	StartMatilionJob('')
    	StartCustomJob('')

    		

    	
    	print('h************************************************************End*************************  ')

        

