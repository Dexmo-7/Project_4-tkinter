from tkinter import *
import tkinter as tk

root = Tk()

window = tk.Frame(root)
#window.title("Chinese zodiac signs")

frame_top = tk.Frame(window, borderwidth=4, relief="flat", width=800, height=200)
frame_middle = tk.Frame(window, borderwidth=4, relief="flat", width=800, height=200)

#chineseSigns = tk.StringVar()
#v.set(OPTIONS[0])
myDaysBase = tk.Entry(frame_middle)
myMonthsBase = tk.Entry(frame_middle)
myYearsBase = tk.Entry(frame_middle)


window.grid(column=0, row=0)
frame_top.grid(column=0, row=0, columnspan=3, rowspan=2)
frame_middle.grid(column=0, row=1, columnspan=3, rowspan=2)
myDaysBase.grid(column=0, row=1)
myMonthsBase.grid(column=1, row=1)
myYearsBase.grid(column=2, row=1)

print(str(myDaysBase))

root.mainloop()
