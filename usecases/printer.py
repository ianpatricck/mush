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

