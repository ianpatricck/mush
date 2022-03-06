from dotenv import dotenv_values
from abc import abstractclassmethod
from .mixer import mixer

config = dotenv_values(".env")

class Listener:

    @abstractclassmethod
    def initialPlay(self):

        initialSong = config["initialSong"]

        try:
            mixer.init()
            mixer.music.load(config["songs"] + initialSong)
            mixer.music.play()

            print(f"\n[+] Listening {initialSong}\n")
        except:
            print("\n[-] Music not placed in config.py or not found\n")

    def playSong(self, song):
        try:
            mixer.init()
            mixer.music.load(config["songs"] + song)
            mixer.music.play()

            print(f"\n[+] Listening {song}\n")
        except:
            print("\n[-] Music not found\n")

