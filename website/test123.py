import schedule 
import time
# Functions setup 
def sudo_placement(): 
    print("Get ready for Sudo Placement at Geeksforgeeks") 

def testset():
	schedule.every(1).minutes.do(sudo_placement)

while True: 
  
    # Checks whether a scheduled task  
    # is pending to run or not 
    schedule.run_pending() 
    time.sleep(1)