import os
from tkinter.filedialog import askdirectory
from mutagen.id3 import ID3
import pygame
from tkinter import *

notPaused = False
isPlaying = False
isMuted=False
root = Tk()
root.minsize(500, 500)

listOfSongs = []
real_nameOfSongs = []
index = 0
songNameString = StringVar()
songLable = Label(root, textvariable=songNameString, width=35)


next_icon = PhotoImage(file=r"images\next.png")
mute_icon=PhotoImage(file=r"images\mute.png")
volume_icon=PhotoImage(file=r"images\volume.png")
icon = PhotoImage(file=r"images\icon.png")
play_icon = PhotoImage(file=r"images\play.png")
previous_icon = PhotoImage(file=r"images\previous.png")
stop_icon = PhotoImage(file=r"images\stop.png")

def chooseDirectory():
    directory = askdirectory()
    # directory = "C:/Users/Srishti Vishnoi/Python Projects/musicplayer/song_folder/"
    os.chdir(directory)

    for file in os.listdir(directory):
        if file.endswith(".mp3"):
            listOfSongs.append(file)
            audio = ID3(os.path.realpath(file))
            real_nameOfSongs.append(audio['TIT2'].text[0])
    print("listOfSongs:::", listOfSongs)

    pygame.mixer.init()
    pygame.mixer.music.load(listOfSongs[index])
    updateSongLabel()

def playNextSong():
    global index
    index = (index + 1) % len(listOfSongs)
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()
    updateSongLabel()

def playPreviousSong():
    global index
    index = (index - 1)%len(listOfSongs)
    pygame.mixer.music.load(listOfSongs[index])
    pygame.mixer.music.play()
    updateSongLabel()

def playStopSong():
    global isPlaying
    if isPlaying:  # stop
        pygame.mixer.music.stop()
        playStopButton.configure(image=play_icon)
        isPlaying = FALSE
    else:
        pygame.mixer.music.play()
        playStopButton.configure(image=stop_icon)
        isPlaying = TRUE

def muteUnmute():
    global isMuted
    if isMuted:  # stop
        pygame.mixer.music.set_volume(10)
        muteUnmuteButton.configure(image=mute_icon)
        isMuted = FALSE
    else:
        pygame.mixer.music.set_volume(0)
        muteUnmuteButton.configure(image=volume_icon)
        isMuted = TRUE

def stopSong():
    pygame.mixer.music.stop()

def updateSongLabel():
    global index
    # global songName
    songNameString.set(real_nameOfSongs[index])
    # return songName


chooseDirectory()

label = Label(root, image=icon)
label.pack()

listbox = Listbox(root,height=12,width=30,selectmode=SINGLE)
listbox.pack()

for song in real_nameOfSongs[::-1]:
    listbox.insert(0, song)

buttonFrame = Frame(root)  # defining a frame that will contain the Widgets
buttonFrame.pack()
previousButtom = Button(buttonFrame, image=previous_icon,height = 40, width = 40, command=playPreviousSong)
previousButtom.pack(side=LEFT, padx=5, pady=20)

playStopButton = Button(buttonFrame, image=play_icon,height = 40, width = 40, command=playStopSong,)
playStopButton.pack(side=LEFT, padx=5, pady=20)

nextButton = Button(buttonFrame, image=next_icon,height = 40, width = 40 , command=playNextSong)
nextButton.pack(side=LEFT, padx=5, pady=20)

muteUnmuteButton = Button(buttonFrame, image=mute_icon,height = 40, width = 40, command=muteUnmute)
muteUnmuteButton.pack(side=LEFT, padx=5, pady=20)

songLable.pack()
root.mainloop()
