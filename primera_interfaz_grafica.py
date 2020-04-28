from tkinter import *

# Ver en (https://docs.python.org/3/library/tk.html)

raiz=Tk()

raiz.title("Mi ventana")
raiz.iconbitmap("API.ico")

raiz.resizable(1,1)

# raiz.geometry("1200x750")

# Color
raiz.config(bg="grey")

# Contruimo un Frame
miframe=Frame()

# Al Frame hay que empaquetarlo dentro de la raiz
miframe.pack(side="left",anchor="n") 
# side puede ser tambien "bottom" "rigth", si no se pone nada () queda en la parte "top" - anchor si no se pone nada va al medio, 
# puede ser "n"=Norte, "s"=Sur

miframe.config(bg="green")

miframe.config(width="650",height="350")

# El mailoop siempre va despues de todas las intrucciones que estan en la raiz
raiz.mainloop()
