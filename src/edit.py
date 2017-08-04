"""
Editor for L-systems objects

Used for creation of new systems and modifying previously saved ones
"""

import LSystemObject
from printer import printVars, printConsts, printRules, printStart
from modify import addVar, deleteVar, addConst, deleteConst, addRule, deleteRule, addStart, deleteStart
from load import loadSystem
from save import save

def edit(systemName=None):
    """
    Editor for L-systems
    """
    head = ("\n    // LSystem Generator // LSystem Editor //\n\n" +
        "    'exit': description\n" +
        "    'view': description\n" +
        "    'delete': description\n" +
        "    'add': description\n" +
        "    'save': description\n")
    print head

    # Initiate system
    system = LSystemObject.LSystemObject()

    # Import attributes from system file, if file name provided
    if systemName:
        loadSystem(system, systemName)

    # View, modify system settings
    while True:
        input = raw_input('> ').split()

        if input:
            cmd = input[0]
            args = input[1:]

            if cmd == 'exit':
                return

            elif cmd == 'view':

                if not args:
                    printVars(system)
                    printConsts(system)
                    printRules(system)
                    printStart(system)

                elif args[0] == 'variables':
                    printVars(system)
                elif args[0] == 'constants':
                    printConsts(system)
                elif args[0] == 'rules':
                    printRules(system)
                elif args[0] == 'start':
                    printStart(system)

                else:
                    print "    Error: %s is not a valid system attribute. See help for guidelines." % args[0]

            elif cmd == 'add':

                if not args:
                    print "Error: argument required. See help for guidelines."

                elif args[0] == 'variable':
                    addVar(system, args[1])
                elif args[0] == 'constant':
                    addConst(system, args[1])
                elif args[0] == 'rule':
                    addRule(system, args[1], args[2])
                elif args[0] == 'start':
                    addStart(system, args[1])

                else:
                    print "Error: %s is not a valid system attribute. See help for guidelines." % args[0]

            elif cmd == 'delete':

                if not args:
                    print "Error: two arguments required. See help for guidelines."

                elif args[0] == 'all':
                    # Wipe entire system by creating new instance of LSystem
                    system = LSystemObject.LSystemObject()

                elif args[0] == 'variable':
                    if args[1]:
                        deleteVar(system, int(args[1]) - 1)
                    else:
                        deleteVar(system)
                elif args[0] == 'constant':
                    if args[1]:
                        deleteConst(system, int(args[1]) - 1)
                    else:
                        deleteConst(system)
                elif args[0] == 'rule':
                    if args[1]:
                        deleteRule(system, args[1])
                    else:
                        deleteRule(system)
                elif args[0] == 'start':
                    deleteStart()

            elif cmd == 'save':

                if args:
                    save(system, args[0])
                else:
                    print "Error: please provide a file name"

            else:
                invalidCommand()
