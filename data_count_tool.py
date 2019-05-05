# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 21:51:11 2018

@author: MAGESHWARI
"""
import os
from tkinter import * 
from tkinter import filedialog
import re
import csv


def center_window(w=200, h=500):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))


def browse():
    global directory
    global filename
    global string_lst
    global contents
    global total
    total = 0
    filepath =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("MDL files","*.mdl"),("all files","*.*")))
    select_file_field.insert(0,filepath) # insert the path in textbox
    directory = os.path.dirname(filepath)
    filename_ext=os.path.basename(filepath)
    #print (filename_ext)
    filename=os.path.splitext(filename_ext)[0]
    #print(filename)
    file = open(filepath,'r')  # open the selected file
    contents = file.read()
    string_lst = ['BusSelector','DiscretePulseGenerator','TransferFcn','SignalGenerator','Scope','Reference']
    for word in string_lst:
        count = sum(1 for match in re.findall(r"\s"+word+"\s",contents))
        total+=count
    print ("Total : "+str(total))
    
def submit():
    #total_block_field.set(total)
    total_block.configure(text="Total Blocks: "+str(total))
    txt_file= open(os.path.join(directory,filename+".txt"),'w')
    for word in string_lst:
        count = sum(1 for match in re.findall(r"\s"+word+"\s",contents))
        txt_file.write(word)
        txt_file.write(":")
        txt_file.write(str(count))
        txt_file.write("\n")
    txt_file.close()
    
    with open(os.path.join(directory,filename+".txt"),'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines=(line.split(":") for line in stripped if line)
        with open(os.path.join(directory,filename+".csv"),'w') as out_file:
            writer=csv.writer(out_file)
            writer.writerow(("WORD","COUNT"))
            writer.writerows(lines)
        
def reset():
    select_file_field.delete(0, END)
    total_block.destroy()
    make_label()
    
def make_label():
    global total_block
    total_block = Label(root,text=" ",font=("Times New Roman",12))
    total_block.grid(row=2,column=1,sticky='w')
    
if __name__=="__main__":
    
    root = Tk()
    root.resizable(0,0) # to disable the maximize button
    root.title("DATA COUNT TOOL")
    root.configure(pady=60)

    select_file = Label(root, text="Select the File : ",width=12)
    select_file.grid(column=0, row=0,sticky='w')
    
    select_file_field = Entry(root,width=50)
    select_file_field.grid(column=1, row=0)
    
    browse = Button(root, text="....",width=5, command=browse)
    browse.grid(column=2, row=0,sticky='w')
    submit = Button(root, text="Submit",width=16, command=submit)
    submit.grid(column=1, row=1,sticky='w',padx=5,pady=5)
    reset = Button(root, text="Reset",width=16, command=reset)
    reset.grid(column=1, row=1,sticky='e',padx=5,pady=5)    
    
    total_block = Label(root,text=" ",font=("Times New Roman",12))
    total_block.grid(row=2,column=1,sticky='w')
    
    #total_block_field = IntVar()
    #Label(root,textvariable=total_block_field)
    #total_block_field.grid(row=2,column=1,sticky='e')
    
    root.iconbitmap(r"C:\Users\MAGESHWARI\Desktop\images.ico")
    center_window(500,200)  # to make the application window centered
    root.mainloop()