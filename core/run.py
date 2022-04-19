from core.actions import Actions
from core.printer import Printer
from .mixer import mixer

class Run(Actions):

    exitStatus = 0
    
    def __init__(self, arg):
        self.query = arg

    def run(self):

        commands = {
            "help": Printer.help,
            "pause": mixer.music.pause,
            "resume": mixer.music.unpause,
            "stop": mixer.music.stop,
            "clear": self.clear,
        }

        commandsWithArgs = {
            "play": self.play,
            "list": self.listSongs,
            "search": self.search
        }

        queryArgs = self.query.split(" ")

        if queryArgs[0] in commandsWithArgs:
            try:
                commandsWithArgs[queryArgs[0]](queryArgs[1])
            except:
                commandsWithArgs[queryArgs[0]]()

        if self.query in commands: commands[self.query]()
        if self.query == "exit": self.exitStatus += 1
 
