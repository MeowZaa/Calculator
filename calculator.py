from tkinter import *
from tkinter import messagebox

GUI = Tk()
GUI.title('Hello World')
GUI.geometry('500x500')

L = Label(GUI,text='Loong Wissawakorn',font=(None,20))
L.pack()
L = Label(GUI,text='Uncle Engineer',font=(None,20))
L.pack()
L = Label(GUI,text='tardev35',font=(None,20))
L.pack()
L = Label(GUI,text='MeowZaa1',font=(None,20))
L.pack()


def popup():
    messagebox.showinfo('Show popup','สวัสดีจ้าาา')


B1 = Button(GUI,text='Click me!',command=popup)
B1.pack()

GUI.mainloop()