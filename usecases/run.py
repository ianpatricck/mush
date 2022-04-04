from usecases.actions import Actions
from usecases.printer import Printer

class Run(Actions):

    exitStatus = 0
    
    def __init__(self, arg):
        self.query = arg

    def run(self):

        commands = {
            "help": Printer.help,
            "pause": self.pause,
            "resume": self.resume,
            "stop": self.stop,
            "clear": self.clear,
        }

        commandsWithArgs = {
            "play": self.play,
            "list": self.listSongs
        }

        queryArgs = self.query.split(" ")

        if queryArgs[0] in commandsWithArgs:
            try:
                commandsWithArgs[queryArgs[0]](queryArgs[1])
            except:
                commandsWithArgs[queryArgs[0]]()

        if self.query in commands: commands[self.query]()
        if self.query == "exit": self.exitStatus += 1
 
