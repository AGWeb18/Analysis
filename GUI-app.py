import tkinter as Tk
root = Tk.Tk()
f = Tk.Frame(root)
f.grid(row=0,column=0)
#place buttons on the *frame*
b1 = Tk.Button(f,text="Button1")
b1.grid(row=0,column=0)
b2 = Tk.Button(f,text="Button2")
b2.grid(row=0,column=1)

big_widget = Tk.Canvas(root, create_text="Hello World")
big_widget.grid(row=1,column=0)  #don't need columnspan any more.
