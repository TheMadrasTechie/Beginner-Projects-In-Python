import random
import pyperclip
from tkinter import *
from tkinter.ttk import *

def pswd():
	entry.delete(0,END)
	length = var1.get()

	lower = "qwertyuioplkjhgfdsazxcvbnm"
	upper = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuioplkjhgfdsazxcvbnm"
	digits = "1234567890`~!@#$%^&*()_+-=,./;'[]QWERTYUIOPASDFGHJKLZXCVBNMqwertyuioplkjhgfdsazxcvbnm"
	password = ""

	if var.get() ==1:
		for i in range(0,length):
			password = password +random.choice(lower)
		return password
	elif var.get() ==2:
		for i in range(0,length):
			password = password +random.choice(upper)
		return password
	elif var.get() ==3:
		for i in range(0,length):
			password = password +random.choice(digits)
		return password
	else:
		print("Please Choose an Option!")








def copy_1():
	r_p = entry.get()
	pyperclip.copy(r_p)

def generate():
	pswd_1 = pswd()
	entry.insert(10,pswd_1)
root = Tk()
var = IntVar()
var1 = IntVar()

root.title("Random Password Generator")

r_p = Label(root, text="Password")
r_p.grid(row=0)
entry = Entry(root)
entry.grid(row=0,column=1)

c_label = Label(root,text="Length")
c_label.grid(row=1)

copy_button = Button(root, text="COPY",command=copy_1)
copy_button.grid(row = 0, column = 2)

generate_button = Button(root, text="GENERATE",command=generate)
generate_button.grid(row = 0, column = 3)

r_low = Radiobutton(root, text="Weak",variable=var,value=1)
r_low.grid(row=1,column=2,sticky="E")
r_med = Radiobutton(root, text="Medium",variable=var,value=2)
r_med.grid(row=1,column=3,sticky="E")
r_strng = Radiobutton(root, text="Strong",variable=var,value=3)
r_strng.grid(row=1,column=4,sticky="E")
combo = Combobox(root, textvariable=var1)

combo['values'] = (8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32)
combo.current(0)
combo.bind('<<COmbobos selected>>')
combo.grid(column=1,row=1)

root.mainloop()