#!/usr/bin/env python3

from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
from coreMT940 import ConverterMT940

window = Tk()

window.title("Simple MT940 to CSV Converter")
window.geometry('800x600')

# file to be converted
lbl_file= Label(window, text="MT940 File")
lbl_file.grid(column=0, row=0)
txt = Entry(window,width=50)
txt.grid(column=0, row=1)
txt.focus()

filetypes = (("Text files","*.txt"),("all files","*.*"))
initialdir="/"
file = ""

def clicked():
    txt.delete(0, END)
    file = filedialog.askopenfilename(title="Select a MT940 file", initialdir=initialdir, filetypes=filetypes)
    #initialdir=file
    txt.insert(0, file)

btn_file = Button(window, text="Choose File", command=clicked)
btn_file.grid(column=1, row=1)

# destination for the converted file
"""
lbl_dest= Label(window, text="Destination")
lbl_dest.grid(column=0, row=3)

txt_dest = Entry(window,width=50)
txt_dest.grid(column=0, row=4)
txt_dest.focus()

def clicked_dest():
    txt_dest.delete(0, END)
    destination = filedialog.askdirectory(title="Select Directory Destination", initialdir=initialdir)
    txt_dest.insert(0, destination)

btn_dest = Button(window, text="Choose Destination", command=clicked_dest)
btn_dest.grid(column=1, row=4)
"""

"""
# filename of the converted file
lbl_name= Label(window, text="File Name")
lbl_name.grid(column=0, row=5)

txt_name = Entry(window,width=50)
txt_name.grid(column=0, row=6)
txt_name.focus()
converted_name = ""
"""

# process conversion
def clicked_convert():
	converter = ConverterMT940(txt.get())
	result = converter.process_conversion()
	if(result):
		showinfo (title="Status", message="Conversion Success!\nThe converted file will be in the same folder")
	else:
		showinfo (title="Status", message="Conversion Failed!")

btn_convert = Button(window, text="Convert", command=clicked_convert)
btn_convert.grid(column=0, row=7)

window.mainloop()
