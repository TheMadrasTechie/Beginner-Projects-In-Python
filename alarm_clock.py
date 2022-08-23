from tkinter import *
import datetime
import time
import winsound

def st_alarm(set_alarm_time):
	while True:
		time.sleep(1)
		current_time = datetime.datetime.now()
		now = current_time.strftime("%H:%M:%S")
		date = current_time.strftime("%d/%m/%Y")
		print("The Set Date is: ",date)
		print(now)
		if now == set_alarm_time:
			print("Come ON!!!!!!!")
			winsound.PlaySound("alarm.wav",winsound.SND_ASYNC)
			break
			

def actual_time():
	alarm_timer = f"{hour.get()}:{minut.get()}:{sec.get()}"
	st_alarm(alarm_timer)

clock = Tk()
clock.title("Sundar's Alarm Clock")
clock.iconbitmap(r"file.png")
clock.geometry("400x300")
time_format = Label(clock,text = "Enter time in 24 hpur format!!!",fg= "green",bg="black",font="Arial").place(x=75,y=100)
addTime  =Label(clock,text="Hour Minute Second",font = 60).place(x=110)
set_alarm = Label(clock,text = "When You want the alrm??",fg = "blue",relief = "solid").place(x=0,y=50)

hour = StringVar()
minut = StringVar()
sec = StringVar()

hourTime = Entry(clock,textvariable = hour,bg = "red",width = 15).place(x=110,y=30)
minTime = Entry(clock,textvariable = minut,bg = "red",width = 15).place(x=160,y=30)
secTime = Entry(clock,textvariable = sec,bg = "red",width = 15).place(x=210,y=30)

submit = Button(clock,text = "Create Alarm",fg = "blue",width = 10,command = actual_time).place(x=110,y=70)
clock.mainloop()