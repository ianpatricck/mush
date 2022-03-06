from dotenv import dotenv_values
from abc import abstractclassmethod
from .mixer import mixer

config = dotenv_values(".env")

class Listener:

    @abstractclassmethod
    def initialPlay(self):
        try:
            mixer.init()
            mixer.music.load(config["songs"] + config["initialSong"])
            mixer.music.play()

            print("\n[+] Listening {}\n".format(config["initialSong"]))
        except:
            print("\n[-] Music not placed in config.py or not found\n")

    def playSong(self, song):
        try:
            mixer.init()
            mixer.music.load(config["songs"] + song)
            mixer.music.play()

            print("\n[+] Listening {}\n".format(song))
        except:
            print("\n[-] Music not found\n")

