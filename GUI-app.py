import tkinter
root = tkinter.Tk()
for r in range(3):
    for c in range(4):
        tkinter.Label(root, text="test").grid(row=r, column=c)

root.mainloop()
