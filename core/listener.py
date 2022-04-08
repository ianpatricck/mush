import os
import json

from abc import abstractclassmethod
from .mixer import mixer, settings

file = open(settings)
config = json.load(file)

class Listener:

    @abstractclassmethod
    def initialPlay(self):

        songs = os.listdir(config["songs"])

        initialSong = None

        for song in songs:
            initialSong = song
            break

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

