import os
import pygame
from mutagen.id3 import ID3 
from tkinter.filedialog import askdirectory
from tkinter import *
from tkinter import filedialog

root=Tk()
root.minsize(300,300)

listofsong = []
realname = []

v = StringVar()
songlabel = Label(root,textvariable=v,width=40)

index = 0

def updatelabel():
    global index
    global songname
    v.set(realname[index])
    return songname

def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsong[index])
    pygame.mixer.music.play()
    updatelabel()


def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsong[index])
    pygame.mixer.music.play()
    updatelabel()

def stopsong(event):
    pygame.mixer.music.stop()
    v.set()

 
def directorychooser():
    directory = filedialog.askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):

            realdir=os.path.realpath(files)
            audio= ID3(realdir)
            realname.append(audio['TIT2'].text[0])

            listofsong.append(files)

pygame.mixer.init()
pygame.mixer.music.load(listofsong[0])
#pygame.mixer.music.play()


directorychooser()

label = Label(root, text= "Music Player")
label.pack()

listbox = Listbox(root)
listbox.pack()

realname.reverse()
for  items in realname:
    Listbox.insert(0,items)

realname.reverse()

nextbutton = Button(root, text = "Next song")
nextbutton.pack()

previousbutton = Button(root, text = "Previous song")
previousbutton.pack()

stopbutton = Button(root, text = "stop song")
stopbutton.pack()

nextbutton.bind("<Button-1>",nextsong())
previousbutton.bind("<Button-1>",prevsong())
stopbutton.bind("<Button-1>",stopsong())

songlabel.pack()

root.mainloop()