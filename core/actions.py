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

    def search(self, song = None):

        songs = os.listdir(config["songs"])

        output = []

        for item in songs:
            if (song in item.lower()):
                output.append(item)

        if (len(output) < 1):
            print("Song not found :c")
        else: 
            for song in output:
                print(song)

