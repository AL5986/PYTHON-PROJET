from tkinter import *

rai=Tk()

miframe=Frame(rai,width=580,height=400)


miframe.pack()

miimagen=PhotoImage(file="kepy.gif")

milabel2=Label(miframe,text="Kepi Confederado",fg="red",font=("Arial",18))
milabel2.place(x=100,y=10)

milabel=Label(miframe,image=miimagen)
milabel.place(x=20,y=80)


rai.mainloop()