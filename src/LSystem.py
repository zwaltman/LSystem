"""
Main menu for application
"""

from message import help, invalidCommand
from edit import edit
from open import openSystem
from directory import deleteSystem, listSystems


head = ("\n    // LSystem Generator //\n\n" +
    "    'exit': exit program\n" +
    "    'new': create new L-system\n" +
    "    'edit': edit existing L-system\n" +
    "    'open': open existing L-system\n")


def main():
    """Main menu for application"""

    print head

    while True:
        input = raw_input('> ').split()
        if input:
            cmd = input[0]
            args = input[1:]

            if cmd == 'exit':
                return

            elif cmd == 'new':
                edit()
                print head

            elif cmd == 'edit':
                if args:
                    try:
                        edit(args[0])
                        print head
                    except:
                        print "Error: couldn't get system file"
                else:
                    print "Error: please provide the name of the system you want to edit"

            elif cmd == 'open':
                if args:
                    openSystem(args[0])
                    print head
                else:
                    print "Error: please provide the name of the system you want to open"

            elif cmd == 'delete':
                if args:
                    deleteSystem(args[0])
                else:
                    print "Error: please provide the name of the file you want to delete"

            elif cmd == 'systems':
                listSystems()

            elif cmd == 'help':
                help()

            else:
                invalidCommand()


if __name__ == "__main__":
    main()
