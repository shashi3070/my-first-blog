import time


def fun():
	cnt=0
	while True:
		if cnt>200:
			break
		cnt=cnt+1
		time.sleep(1)

	return 'Success'

fun()

