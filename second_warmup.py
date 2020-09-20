from tkinter import *

def client_exit():
    exit()

root = Tk()
menubar = Menu(root)
#creating the file button with scroll list
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save as...")
filemenu.add_command(label="Close")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=client_exit)
#adding the button to menu
menubar.add_cascade(label="File", menu=filemenu)
#creating the edit button with scroll list
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo")
editmenu.add_separator()
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Delete")
editmenu.add_command(label="Select All")
#adding the edit button to menu
menubar.add_cascade(label="Edit", menu=editmenu)
#creating help button with scroll list
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="About...")
#adding the help button to menu
helpmenu.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()