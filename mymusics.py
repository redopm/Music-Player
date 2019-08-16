from tkinter import filedialog
import pygame
import os
 
def directorychooser():
 
    directory = filedialog.askdirectory()
    os.chdir(directory)
 
    listofsongs = []
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            listofsongs.append(files)
 
 
    pygame.mixer.init()
    pygame.mixer.music.load("path to music" + listofsongs[0])
    pygame.mixer.music.play()
 
    pygame.time.delay(2000)
 
directorychooser()