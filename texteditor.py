#!/usr/bin/env python
import Tkinter
import os
top = Tkinter.Tk()
top.geometry('800x600')
#def saving(ev=None):
""" am trying to make a text editor
need to: - read file
- write to file
- get button working
- get textarea's contents to add to the file
- heaps more """
def saving():

    pathtofile = fileinput.get()
    if os.path.exists(pathtofile):

        writefilesrc =  open(pathtofile,'w')
        textcontents = entertext.get(1.0,Tkinter.END)
        writefilesrc.write(textcontents)
        print '\n' + textcontents + '\n'
    else:
        fileinput.insert(0, "error saving")
def opening():

    pathtofile = fileinput.get()
    if os.path.exists(pathtofile):
        filesrc =  open(pathtofile,'r')

        contents = filesrc.read()
        entertext.insert(1.0, contents)
    else:
        fileinput.insert(0,"error opening")
fileinput = Tkinter.Entry(top)
fileinput.pack()
openbutton = Tkinter.Button(top, text='open', command=opening)
openbutton.pack()
#print contents
#top = Tkinter.Tk()
#top.geometry('800x600')
#label = Tkinter.Message(top, text=contents)
#label.pack()
entertext = Tkinter.Text(top)
entertext.pack()
button = Tkinter.Button(top, text='save',command=saving)
quitbutton = Tkinter.Button(top, text='quit',command=top.quit)
button.pack()

quitbutton.pack()
Tkinter.mainloop()


