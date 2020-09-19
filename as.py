from tkinter import *

root = Tk()

# creating a label widget

showlabel = Label(root, text='this is tkinter')

# shoving in onto the screen

button = Button(root, text='Quit', width=25, command=root.destroy)

showlabel.pack()

button.pack()

# mainloop

root.mainloop()
