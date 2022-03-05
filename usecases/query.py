import platform
import os

from .mixer import mixer
from .listener import Listener
from .printer import Printer

class Query(Listener):
 
    def play(self, song = None):
        if (song == None):
            self.initialPlay()  

    def pause(self):
        print("\n[-] was paused\n")
        mixer.music.pause()
    
    def resume(self):
        print("\n[-] listening\n")
        mixer.music.unpause()
    
    def stop(self):
        print("\n[-] stopped\n")
        mixer.music.stop()

    def clear(self):
        
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

        Printer.main()
