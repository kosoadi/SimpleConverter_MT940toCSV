#!/usr/bin/env python3

from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
from coreMT940 import ConverterMT940
from tkinter import ttk
import time
from threading import Thread

window = Tk()

window.title("Simple MT940 to CSV Converter")
window.iconbitmap("icon.ico")
#window.geometry('800x600')

# file to be converted
lbl_file= Label(window, text="MT940 File")
#lbl_file.grid(column=0, row=0)
lbl_file.pack()
txt = Entry(window,width=50)
#txt.grid(column=0, row=1)
txt.pack()
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
#btn_file.grid(column=1, row=1)
btn_file.pack()

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

# thread for progress bar
def monitor(thread):
	if thread.is_alive():
		# check the thread every 100ms
		window.after(100, lambda: monitor(thread))
		progress_bar["value"] += 10
		if progress_bar["value"] == 100:
			progress_bar["value"] = 0
	else:
		progress_bar["value"] = 100
		showinfo (title="Status", message="Conversion Finished!\nThe converted file will be in the same folder")

# process conversion
def clicked_convert():
	progress_bar["value"] = 0
	converter = ConverterMT940(txt.get())
	result = converter.start()
	monitor(converter)
	#result = converter.process_conversion()

btn_convert = Button(window, text="Convert", command=clicked_convert)
#btn_convert.grid(column=0, row=7)
btn_convert.pack()

progress_bar = ttk.Progressbar(window, orient=HORIZONTAL, 
	length=300, mode="determinate")
progress_bar.pack(pady=20)

window.mainloop()
