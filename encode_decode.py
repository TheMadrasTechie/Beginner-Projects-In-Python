from tkinter import *
import base64

root = Tk()
root.geometry('500x300')
root.resizable(0,0)

root.title("Encoder and Decoder")
Label(root, text = 'Encode Decode', font = 'arial').pack()
Label(root, text=  'Welcome !!',font = 'arial').pack()

txt = StringVar()
p_key = StringVar()
mode = StringVar()
reslt = StringVar()

def Encode(key,msg):
    enc=[]
    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(msg[i]) + ord(key_c)) % 256))
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def Decode(key,msg):
	dec = []
	msg = base64.urlsafe_b64decode(msg).decode()
	for i in range(len(msg)):
		key_c = key[i%len(key)]
		dec.append(chr((256 +ord(msg[i])-ord(key_c))%256))
	return "".join(dec)


def rslt():
	if (mode.get() == 'e'):
		reslt.set(Encode(p_key.get(),txt.get()))
	elif (mode.get() == 'd'):
		reslt.set(Decode(p_key.get(),txt.get()))
	else:
		reslt.set("Invalid Mode")


def reset():
	txt.set("")
	p_key.set("")
	mode.set("")
	reslt.set("")

def ext():
	root.destroy()	

Label(root, text='Message').place(x=60,y=60)
Entry(root, textvariable = txt ).place(x=290,y=60)

Label(root, text='Key').place(x=60,y=90)
Entry(root, textvariable = p_key ).place(x=290,y=90)

Label(root, text='Mode(E-encode, D-decode)').place(x=60,y=120)
Entry(root, textvariable = mode ).place(x=290,y=120)

Entry(root, textvariable = reslt ).place(x=290,y=150)

Button(root, font='arial', text='RESULT',bg='green',command = rslt).place(x=60,y=180)
Button(root, font='arial', text='RESET',bg='yellow',command = reset).place(x=200,y=180)
Button(root, font='arial', text='EXIT',bg='red',command = ext).place(x=340,y=180)

root.mainloop()