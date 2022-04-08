from core import Printer, Run

Printer.main()

while True:

    args = input("=> ")

    run = Run(args)
    run.run()

    if (run.exitStatus != 0):
        print("\nGood bye :D\n")
        break
