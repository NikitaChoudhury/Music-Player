from pygame import *
from tkinter import filedialog #load(select multiple songs) playlist

playList=[]      #Create Playlist(list coz Multiple songs)
songIndex=-1     #Index of each Song in the Playlist 
                 #For prev. and next.

#C:\Users\nikit\PYTHON PROGRAMMING\MINI PROJECT\TALENT BATTLE\Music Player\songs\Hanuman Chalisa Hanuman 320 Kbps.mp3

def load_single():

    global songIndex
    path = filedialog.askopenfilename();     
    playList.append(path) #add path of the req. song into the playList
    songIndex = songIndex + 1
    mixer.init()
    mixer.music.load(playList[songIndex]) #mixer is a class
                                          #Load song of songIndex=x from Playlist
    print(songIndex)                                          
    print(playList[songIndex]) #print song from playlist with songIndex=x


def play():
    if mixer.music.get_pos()>0: #If song played for the first time  #C:\Users\nikit\PYTHON PROGRAMMING\MINI PROJECT\TALENT BATTLE\Music Player\songs\Miley_Cyrus_-_Flowers_Demo__(NaijaMusic.Ng).mp3
        mixer.music.unpause()
    else:
        mixer.music.play()
#from pause to unpause

def pause():
    mixer.music.pause()
def stop():
    mixer.music.stop()

def load_playlist():
    global songIndex
    playList.clear()
    songIndex=0
    filePaths=filedialog.askopenfilenames() #open filedialog
    #print(filePaths) #to see which song have been included
    for fileName in filePaths:
        playList.append(fileName)
    mixer.init()
    mixer.music.load(playList[songIndex])
    mixer.music.play()
    print(playList)

def next():
    global songIndex              #to increment song index
    songIndex=songIndex+1
    if songIndex>=len(playList):  #If song index reach to last song
        songIndex=0     #go to start
    mixer.music.load(playList[songIndex])
    mixer.music.play()
def prev():
    global songIndex              #to increment song index
    songIndex=songIndex-1
    if songIndex<0:  #If song index reach to last song
        songIndex=len(playList)     #go to start-1
    mixer.music.load(playList[songIndex])
    mixer.music.play()
""" if __name__ == '__main__':
    while True:
        print("1. Load Single 2. Play 3. Pause 4. Stop 5. Load Playlist 6. Next 7. Prev")
        print("Enter your Choice:")
        ch=int(input(""))
        if ch==1:
            load_single()
        elif ch==2:
            play()
        elif ch==3:
            pause()
        elif ch==4:
            stop()
        elif ch==5:
            load_playlist()
        elif ch==6:
            next()
        elif ch==7:
            prev() """


