from abc import abstractclassmethod

class Printer:

    @abstractclassmethod
    def main(self):
        
        print("""
 _   .-')                  .-')    ('-. .-. 
( '.( OO )_               ( OO ). ( OO )  / 
 ,--.   ,--.),--. ,--.   (_)---\_),--. ,--. 
 |   `.'   | |  | |  |   /    _ | |  | |  | 
 |         | |  | | .-') \  :` `. |   .|  | 
 |  |'.'|  | |  |_|( OO ) '..`''.)|       | 
 |  |   |  | |  | | `-' /.-._)   \|  .-.  | 
 |  |   |  |('  '-'(_.-' \       /|  | |  | 
 `--'   `--'  `-----'     `-----' `--' `--' 
        """)

        print("Type 'pause' to pause, 'resume' to resume")
        print("Type 'stop' to stop")
        print("Type 'help' to show options")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    @abstractclassmethod
    def help(self):
        print("""

        Commands:

        - play                   | Just play initial song
        - play [song]            | Play a chosen song
        - play [id]              | Play song by id
        - clear                  | Clear screen
        - list                   | List all songs
        - list [id]              | List all songs until this id
        - list [from-to]         | List all songs between IDs
        - search [something]     | Search music, artist and etc ...
        """)

