import traceback
from subprocess import call,PIPE, run
from django.conf import settings
import os
import logging
log = logging.getLogger(__name__)

def CallPythonJob(jobname):
	log.debug('-------------In     CallPythonJob-----------------')
	print('-------------In     CallPythonJob-----------------')

	try:
		#status=call(["python", os.path.join(settings.PYTHON_FILE_LOCATION,jobname)])
		command=["python", os.path.join(settings.PYTHON_FILE_LOCATION,jobname)]
		status = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
		
		#print(status.returncode, status.stdout, status.stderr)
		
		
		if status.returncode==0:
			return status.returncode
		else:
			log.error(status.stderr)
			raise Exception(status.stderr)

		
		
	except Exception as E:
		print('Error In PythonHelper  CallPythonJob  '+str(E))
		log.error('Error In PythonHelper  CallPythonJob  '+str(E))
		log.error(traceback.format_exc())
		raise Exception(str(E)+  "   Error "+str(jobname))

	

	




