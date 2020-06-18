import urllib.request

import logging
log = logging.getLogger(__name__)


def CallTalendJob(endpoint):
	print('************in CallTalendJob **************endpoint##############-----'+str(endpoint))
	log.debug('**************************endpoint##############-----'+str(endpoint))
	try:
		response =urllib.request.urlopen(endpoint).read().decode('UTF-8')
		status=response.split('<ns1:item xsi:type="xsd:string">')[1].split('</ns1:item>')[0]
		print('**************************status##############-----'+str(status))
		log.debug('**************************status##############-----'+str(status))

		return str(status)
	except Exception as E:
		print('Error in Talend_Helper CallTalendJob '+str(E))
		raise Exception(str(E)+  "   Error "+str(endpoint))