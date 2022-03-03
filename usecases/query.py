from .mixer import mixer
from .listener import Listener

class Query(Listener):

    exitStatus = 0
    
    def __init__(self, arg):
        self.query = arg

    def run(self):
        
        if self.query == "help":
            self.help()

        elif self.query == "play":
            self.play()

        elif self.query == "pause":
            self.pause()

        elif self.query == "resume":
            self.resume()

        elif self.query == "stop":
            self.stop()

        elif self.query == "exit":
            self.exitStatus += 1

    def help(self):
        print("""

        Commands:

        - set [path]             | set a playlist folder
        - play                   | just play initial song
        - play [song]            | play a chosen song
        """)

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
    
