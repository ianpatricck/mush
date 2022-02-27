from config import config

from os import environ
import sys

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

from pygame import mixer

print("""
░█▀▀░█▀█░█▀█░█░█░█▀▀░█▀▀░█▀█░█▀█░█▀▀░█▀▀
░▀▀█░█░█░█▀█░█▀▄░█▀▀░▀▀█░█░█░█░█░█░█░▀▀█
░▀▀▀░▀░▀░▀░▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀▀▀
""")

print("Type 'pause' to pause, 'resume' to resume")
print("Type 'stop' to stop")
print("Type 'help' to show options")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

if len(sys.argv) < 2:
    mixer.init()
    mixer.music.load(config["songs"] + config["initialSong"])
    mixer.music.play()

    print("\nListening {}\n".format(config["initialSong"]))

while True:

    query = input("=> ")
    query = query.lower()

    if query == "pause":
        print("[-] was paused")
        mixer.music.pause()
    
    elif query == "resume":
        print("[-] listening")
        mixer.music.unpause()
    
    elif query == "stop":
        print("[-] stopped, goodbye :D")
        mixer.music.stop()
        break

