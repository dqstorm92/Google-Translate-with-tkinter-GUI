from tkinter import *
from PIL import Image, ImageTk
from googletrans import Translator

root=Tk()
root.title("Google Translate")
root.geometry("500x630")
root.iconbitmap('logo.ico')

load=Image.open('background.png')
render=ImageTk.PhotoImage(load)
img=Label(root, image=render)
img.place(x=0, y=0)

name=Label(root, text="Translator", fg='#FFFFFF', bd=0, bg="#031520", font=("Transformers Movie", 30))
name.pack(pady=10)
box=Text(root, width=28, height=8, font=("Arial", 16))
box.pack(pady=20)

button=Frame(root).pack(side=BOTTOM)
def clear():
    box.delete(1.0, END)
    box1.delete(1.0, END)
def translate():
    try:
        box1.delete(1.0, END)
        IN=box.get(1.0, END)
        print(IN)
        t=Translator()
        a=t.translate(IN,src="vi",dest="en")
        b=a.text
        box1.insert(END, b)
    except:
        print("No")


clearB=Button(button, text="Clear text", font=("Arial", 10, 'bold'), bg='#303030', fg='#FFFFFF', command=clear)
clearB.place(x=150, y=310)
clearB=Button(button, text="Translate", font=("Arial", 10, 'bold'), bg='#303030', fg='#FFFFFF', command=translate)
clearB.place(x=290, y=310)

box1=Text(root, width=28, height=8, font=("Arial", 16))
box1.pack(pady=50)



root.mainloop()
