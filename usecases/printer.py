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
        - clear                  | clear screen
        - list                   | list all songs
        """)

