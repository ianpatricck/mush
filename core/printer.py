from abc import abstractclassmethod

class Printer:

    @abstractclassmethod
    def main(self):
        
        print("""
        ░█▀▀░█▀█░█▀█░█░█░█▀▀░█▀▀░█▀█░█▀█░█▀▀░█▀▀
        ░▀▀█░█░█░█▀█░█▀▄░█▀▀░▀▀█░█░█░█░█░█░█░▀▀█
        ░▀▀▀░▀░▀░▀░▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀▀▀
        """)

        print("Type 'pause' to pause, 'resume' to resume")
        print("Type 'stop' to stop")
        print("Type 'help' to show options")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    @abstractclassmethod
    def help(self):
        print("""

        Commands:

        - play                   | just play initial song
        - play [song]            | play a chosen song
        - play [id]              | play song by id
        - clear                  | clear screen
        - list                   | list all songs
        - list [id]              | list all songs until this id
        - search [something]     | Search music, artist and etc ...
        """)

