from tkinter import *
import random

root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title("Rock Paper Scissors")
Label(root,text='Rock, Paper, Scissors',font='arial').pack()
user_input = StringVar()
rslt = StringVar()
Label(root,text='Choose Any One:\nRock, Paper, Scissors',font='arial').place(x=20,y=70)
Entry(root,font='arial',textvariabl=user_input).place(x=90,y=130)

def computer_pick():
   comp_pick = random.randint(1,3)
   if comp_pick == 1:
       comp_pick = 'rock'
   elif comp_pick == 2:
       comp_pick = 'paper'
   elif comp_pick == 3:
       comp_pick = 'scissors'
   return comp_pick

def gm():
    user_pick = user_input.get()
    comp_pick = computer_pick()
    if user_pick == comp_pick:
        rslt.set("Tie!!! You both select the same")
    elif user_pick == 'rock' and comp_pick == 'paper':
        rslt.set("You Loose!!! Computer Picked Paper")
    elif user_pick == 'paper' and comp_pick == 'scissors':
        rslt.set("You Loose!!! Computer Picked Scissors")
    elif user_pick == 'scissors' and comp_pick == 'rock':
        rslt.set("You Loose!!! Computer Picked Rock")
    elif user_pick == 'rock' and comp_pick == 'scissors':
        rslt.set("You WIN!!! Computer Picked Scissors")
    elif user_pick == 'scissors' and comp_pick == 'paper':
        rslt.set("You WIN!!! Computer Picked Paper")
    elif user_pick == 'paper' and comp_pick == 'rock':
        rslt.set("You WIN!!! Computer Picked Rock")
    else:
        rslt.set("Invalid Entry -- enter proper input")
def reset():
    rslt.set("")
    user_input.set("")

def ext():
    root.destroy()



Entry(root,font='arial',textvariabl=rslt,width=50).place(x=25,y=250)
Button(root,font='arial',text='PLAY',padx=5,bg='green',command=gm).place(x=70,y=300)
Button(root,font='arial',text='EXIT',padx=5,bg='red',command=ext).place(x=150,y=300)
Button(root,font='arial',text='RESET',padx=5,bg='yellow',command=reset).place(x=230,y=300)
root.mainloop()