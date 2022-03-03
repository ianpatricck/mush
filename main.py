import sys
from usecases import Printer, Listener, Query

Printer.main()
Listener.initialPlay() if len(sys.argv) < 2 else None

while True:

    args = input("=> ").lower()

    query = Query(args) 
    query.run()

    if (query.exitStatus != 0):
        print("\nGood bye :D\n")
        break
