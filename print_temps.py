import temp
import time
import datetime
while True:

	time.sleep(5)
	print(datetime.datetime.now())
	print(temp.tempRead().read_temp())
	print('')
