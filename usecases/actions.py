import platform
import os
import json

from .mixer import mixer, settings
from .listener import Listener
from .printer import Printer

file = open(settings)
config = json.load(file)

class Actions(Listener):
 
    def play(self, song = None):
        if (song == None or not song or song == ""):
            self.initialPlay()
        
        elif song.isnumeric():
            musicId = int(song)
            songs = os.listdir(config["songs"])
            
            for index, song in enumerate(songs, start=1):
                if (musicId == index):
                    self.playSong(song)
        else:
            self.playSong(song)

    def pause(self):
        print("\n[+] was paused\n")
        mixer.music.pause()
    
    def resume(self):
        print("\n[+] listening\n")
        mixer.music.unpause()
    
    def stop(self):
        print("\n[+] stopped\n")
        mixer.music.stop()

    def clear(self): 
        os.system("cls") if platform.system() == "Windows" else os.system("clear")

        Printer.main()

    def listSongs(self, param = None):

        songs = os.listdir(config["songs"])

        if (param == None or not param or param == ""):

            for index, song in enumerate(songs, start=1):
                print(index, song)
            print("\n")
        
        elif (param != None and int(param)):
            
            for index, song in enumerate(songs, start=1):
                print(index, song)
                
                if (index == int(param)):
                    break
