# Program to demonstrate 
# # timer objects in python 
import time 
from tkinter import *
import threading 


color ='green'

def greenlight():
    global color
    rightc.itemconfig(green,fill="green")
    rightc.itemconfig(yellow,fill="#F9F5A6")
    rightc.itemconfig(red,fill="#F5413E")
    color = 'yellow' 
    
def yellowlight():
    global color
    rightc.itemconfig(green,fill="#CFFF5A")
    rightc.itemconfig(yellow,fill="yellow")
    rightc.itemconfig(red,fill="#F5413E")
    color='red'
def redlight():
    global color
    rightc.itemconfig(green,fill="#CFFF5A")
    rightc.itemconfig(yellow,fill="#F9F5A6")
    rightc.itemconfig(red,fill="red")
    color='green'

fenetre=Tk()
fenetre.title("Traffic lights")
fenetre.geometry('700x500')
fenetre.resizable(False,False)
fenetre.iconbitmap('./feu.ico')
title=Label(fenetre,text='Traffic lights',fg='yellow',bg='red')
title.config(font=('times',20,'bold'))
title.pack(fill=X)

#left canvas
leftc=Canvas(fenetre,width=345,height=660,bg='white')
filename=PhotoImage(file='./route.png')
bg=Label(fenetre,image=filename)
bg.place(x=0,y=35)
list_time=Listbox(fenetre,width=20,height=10)
times=['1','5','25','50','75','100','150','200','250','300']
for i in times:
    list_time.insert(END,i)
list_time.place(x=100,y=280)
leftc.place(x=0,y=35)

#right canvas
rightc=Canvas(fenetre,width=345,height=660,bg='#B6CDD1')
rightc.place(x=350,y=35)
green=rightc.create_oval(110,100,170,160,width=3,fill='#CFFF5A')
rightc.create_rectangle(100,90,180,170,width=3)
yellow=rightc.create_oval(110,190,170,250,width=3,fill='#F9F5A6')
rightc.create_rectangle(100,180,180,260,width=3)
red=rightc.create_oval(110,280,170,340,width=3,fill='#F5413E')
rightc.create_rectangle(100,270,180,350,width=3)


def tester():
    global color
    if color !='':
        if color=='green':
            greenlight()
        elif color=='yellow':
            yellowlight()
        elif color=='red' :
            redlight()
        timer = threading.Timer(int(list_time.get(ACTIVE)),tester)
        timer.start()
    else :
        color='green'
        
def quitter():
    global color
    color=''
    rightc.itemconfig(green,fill="#CFFF5A")
    rightc.itemconfig(yellow,fill="#F9F5A6")
    rightc.itemconfig(red,fill="#F5413E")
    
    


btn=Button(rightc,text='TESTER ',command=tester,fg='yellow',bg='red')
btn.config(font=('times',16,'bold'))
btn.place(x=200,y=100)

btn=Button(rightc,text='QUITTER',command=quitter,fg='yellow',bg='red')
btn.config(font=('times',16,'bold'))
btn.place(x=200,y=180)

timer = threading.Timer(5,tester)







fenetre.mainloop()
