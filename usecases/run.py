from usecases.query import Query
from usecases.printer import Printer

class Run(Query):

    exitStatus = 0
    
    def __init__(self, arg):
        self.query = arg

    def run(self):

        commands = {
            "help": Printer.help,
            "play": self.play,
            "pause": self.pause,
            "resume": self.resume,
            "stop": self.stop,
            "clear": self.clear
        }

        if self.query in commands: commands[self.query]()
        if self.query == "exit": self.exitStatus += 1
 
