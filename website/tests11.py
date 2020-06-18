import threading
import time
def fun1():
	a=[]
	try:
		print('fun(v):')
		print(a[0])
	except Exception as E:
		print('Exception fun1 '+str(E))
		raise Exception(str(E)+ "Error ")


def fun(v):
	try:
		s=1
		if s=='1j dkjsd':
			print('jj')
		else:
			print('ss')
		fun1()
		
	
		
	except Exception as E:
			print('Exception-iiii----'+str(E))
			


	
fun('1')