from tkinter import *

root  = Tk()
root.geometry('300x300')
root.title("Mad Libs Generator")
Label(root,text='Enter Your Ideas').pack()
Label(root,text='Click Any One:').place(x=40,y=80)

def madlib_1():
    animals = input('enter an animals name : ')
    profession = input('enter a profession name : ')
    cloth = input('enter a cloth name : ')
    things = input('enter a thing name : ')
    name = input('enter a name : ')
    place = input('enter a place name : ')
    verb = input('enter a verb in ing form : ')
    food = input('enter a food name : ')

    print("say "+food+", the photographer said as the camera flashed! \n"+name+" and I had gone to "+place+" to get our photos taken today. The first phot we really wanted was a picture of us dressed as "+animals+" pretending to be a "+profession+". \n when we saw thw second photo, it was exactly what I wanted. We both looked like"+things+"wearing"+cloth+" and "+verb+" --exaclty what I had in my mind")


def madlib_2():
    adjactive = input('enter adjective : ')
    color = input('enter a color name : ')
    thing = input('enter a thing name :')
    place = input('enter a place name : ')
    person= input('enter a person name : ')
    adjactive1 = input('enter a adjactive : ')
    insect= input('enter a insect name : ')
    food = input('enter a food name : ')
    verb = input('enter a verb name : ')

    print('Last night I dreamed I was a ' +adjactive+ ' butterfly with ' + color+ ' splocthes that looked like '+thing+ ' .I flew to ' + place+ ' with my bestfriend and '+person+ ' who was a '+adjactive1+ ' ' +insect +' .We ate some ' +food+ ' when we got there and then decided to '+verb+ ' and the dream ended when I said-- lets ' +verb+ '.')

def madlib_3():
    person = input('enter person name: ')
    color = input('enter color : ')
    foods = input('enter food name : ')
    adjective = input('enter aa adjective name: ')
    thing = input('enter a thing name : ')
    place = input('enter place : ')
    verb = input('enter verb : ')
    adverb = input('enter adverb : ')
    food = input('enter food name: ')
    things = input('enter a thing name : ')

   
    print('Today we picked apple from '+person+ "'s Orchard. I had no idea there were so many different varieties of apples. I ate " +color+ ' apples straight off the tree that tested like '+foods+ '. Then there was a '+adjective+ ' apple that looked like a ' + thing + '.When our bag were full, we went on a free hay ride to '+place+ ' and back. It ended at a hay pile where we got to ' +verb+ ' ' +adverb+ '. I can hardly wait to get home and cook with the apples. We are going to make appple '+food+ ' and '+things+' pies!.')  

Button(root,text = 'The Photographer',bg='light green',command=madlib_1).place(x=60,y=120)
Button(root,text = 'Apple and apple',bg='light green',command=madlib_2).place(x=70,y=180)
Button(root,text = 'The Butterfly',bg='light green',command=madlib_3).place(x=80,y=240)

root.mainloop()