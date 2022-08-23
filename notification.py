import time
from win10toast import ToastNotifier

remTime = input("Time in 24 hour format(HH:MM:SS):")
remMsg = input("Enter Your Message:")
while True:
	current_time = time.strftime("%H:%M:%S")
	time.sleep(1)
	print(current_time)
	if (current_time == remTime):
		print("Reminder Time is Here!!!!!") 
		break

notify = ToastNotifier()
notify.show_toast("Reminder",remMsg)