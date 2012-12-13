#!/usr/bin/env python
import Tkinter
import os
import listdir
top = Tkinter.Tk()
top.geometry('800x600')
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
    
    
    
    #fileinput.insert(0,str(object=listdir.dirlist().doLS()))
    pathtofile = fileinput.get()
    
    if os.path.exists(pathtofile):
        filesrc =  open(pathtofile,'r')

        contents = filesrc.read()
        entertext.insert(1.0, contents)
    else:
        fileinput.insert(0,"error opening")
        
def browsing():
    filepath = listdir.dirlist().doLS()
    return filepath
    
def createfile():
    nameoffile = createfilename.get()
    pathofcreatefile = fileinput.get()
    dog = nameoffile
    f = open(dog,'w')
    f.close()
    fileinput.insert(Tkinter.END, dog)
    
   
    
enterfile = Tkinter.Label(top,text='enter file path:')
enterfile.pack()
fileinput = Tkinter.Entry(top,width='200')
fileinput.pack()
browsebutton = Tkinter.Button(top, text='browse', command=browsing)
browsebutton.pack()

createfilename = Tkinter.Entry(top,width='100')
createfilename.pack()
createfilebutton = Tkinter.Button(top,text='create file',command=createfile)
createfilebutton.pack()

openbutton = Tkinter.Button(top, text='open', command=opening)
openbutton.pack()

#print contents
#top = Tkinter.Tk()
#top.geometry('800x600')
#label = Tkinter.Message(top, text=contents)
#label.pack()
labelforentertext = Tkinter.Label(top,text='enter text:')
labelforentertext.pack()
entertext = Tkinter.Text(top, bg='gray', )
entertext.pack()
button = Tkinter.Button(top, text='save',command=saving)
quitbutton = Tkinter.Button(top, text='quit',command=top.quit)
button.pack()

quitbutton.pack()
Tkinter.mainloop()


