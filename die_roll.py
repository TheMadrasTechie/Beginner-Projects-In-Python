import tkinter
from PIL import Image, ImageTk
import random

root = tkinter.Tk()
root.geometry('400x400')
root.title('Roll The Dice')

l0 = tkinter.Label(root, text="")
l0.pack()

l0 = tkinter.Label(root, text="Hello!!!\n Welcome To Dice Roller!!", font='arial', bg='red').pack()

dice = ['die1.png','die2.png','die3.png','die4.png','die5.png','die6.png']

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
label1 = tkinter.Label(root, image= image1)
label1.image = image1
label1.pack(expand = True)

def roll_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image = image1
    
btn = tkinter.Button(root, text="Roll The Dice",fg='light blue',command = roll_dice)
btn.pack(expand = True)
root.mainloop()
