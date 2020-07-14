from tkinter import *
import tkinter as tk
import random

o=open('password.txt','a+')

up = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
low = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
num = ['1','2','3','4','5','6','7','8','9','0']
sign = ['!','@','#','$','%','&','*','~']

passw = []

i = 0 
while i <=2:
    passw.append(random.choice(up))
    passw.append(random.choice(low))
    passw.append(random.choice(num))
    passw.append(random.choice(sign))
    i += 1

random.shuffle(passw)

a = ''.join(passw)

def saved():
    leaf=Toplevel()
    leaf.title('alert window')
    leaf.geometry('200x200')
    leaf.resizable(0,0)

    lol=Label(leaf,text='the password was saved',bg='snow',fg='black')
    lol.grid(row=2,column=2,padx=10,pady=20)

root = Tk()
root.title('password creator and saver tool')
root.configure(background='red')
root.geometry('300x300')
root.resizable(0,0)

l1 = Label(root,text='enter your account',bg='snow',fg='black')
l2 = Label(root,text='generated password',bg='snow',fg='black')
l3 = Label(root,text='{}'.format(a),bg='snow',fg='black')
l1.grid(row=1,column=1,padx=20,pady=10)

def generate():
    l2.grid(row=3,column=1,pady=10)
    l3.grid(row=3,column=2,pady=10)
    b2.grid(row=4,column=1,pady=10)
    
var=StringVar()

entry = Entry(text=var,bg='snow',fg='black')
entry.grid(row=1,column=2)

def foraccount():
    i = entry.get()
    o.write(i+' : '+a+'\n')

    o.close()
    saved()

b1 = Button(root,text='generate',bg='snow',fg='black',activebackground='yellow',command=generate)
b2 = Button(root,text='save',bg='snow',fg='black',activebackground='yellow',command=foraccount)
b1.grid(row=2,column=1,pady=10)

root.mainloop
    
