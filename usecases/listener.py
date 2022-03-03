from dotenv import load_dotenv, dotenv_values
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

