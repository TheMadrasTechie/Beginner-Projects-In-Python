from tkinter import *
from playsound import playsound
import time
import os
from gtts import gTTS 

root = Tk()
root.geometry('500x400')
root.resizable(0,0)
root.config(bg = 'pink')
root.title("Text To Speech Convertor")

Label(root, text = 'Text To Speech',font='arial',bg='orange').pack()

Msg = StringVar()

entry_field = Entry(root,textvariable = Msg,width = '50')
entry_field.place(x=20,y=100)

def convertor():
	message = entry_field.get()
	speech = gTTS(text = message)
	speech.save('text.mp3')
	playsound('text.mp3')

def exit():
	root.destroy()

def reset():
	Msg.set("")
	os.remove('text.mp3')

Button(root,text="PLAY",font='arial',bg='green',command=convertor).place(x=25,y=140)
Button(root,text="RESET",font='arial',bg='yellow',command=reset).place(x=175,y=140)
Button(root,text="EXIT",font='arial',bg='red',command=exit).place(x=325,y=140)

root.mainloop()
