import platform
import os

from .mixer import mixer
from .listener import Listener
from .printer import Printer
from dotenv import dotenv_values

config = dotenv_values(".env")

class Query(Listener):
 
    def play(self, song = None):
        self.initialPlay() if (song == None or not song or "") else self.playSong(song)

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

    def listSongs(self):
        songs = os.listdir(config["songs"])

        for index, song in enumerate(songs, start=1):
            print(index, song)
        print("\n")

