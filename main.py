from core import Printer, Run

Printer.main()

exitMessage = "\nGood bye :D\n"

try:

    while True:

        args = input("=> ")

        run = Run(args)
        run.run()

        if (run.exitStatus != 0):
            print(exitMessage)
            break
except:
    print(exitMessage)
