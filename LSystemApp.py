"""
LSystem main program
"""

# Zach Waltman
# z.waltman@gmail.com

import os
import LSystem

# -------------
# MAIN MENU
# -------------
def main():
    """
    Main menu for application.
    """
    head = ("\n    // LSystem Generator //\n\n" +
        "    'exit': exit program\n" +
        "    'new': create new L-system\n" +
        "    'edit': edit existing L-system\n" +
        "    'open': open existing L-system\n")
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

# --------------------------------------------
# FUNCTIONS FOR USE FROM MAIN MENU
# --------------------------------------------
def listSystems():
    systemList = os.listdir("SystemFiles")
    for fileName in systemList:
        print fileName

def edit(systemName=None):
    """
    Editor for LSystems.
    """
    head = ("\n    // LSystem Generator // LSystem Editor //\n\n" +
        "    'exit': description\n" +
        "    'view': description\n" +
        "    'delete': description\n" +
        "    'add': description\n" +
        "    'save': description\n")
    print head

    # INITIATE SYSTEM
    system = LSystem.LSystem()
    # Import attributes from system file, if file name provided
    if systemName:
        loadSystem(system, systemName)

    # VIEW, MODIFY SYSTEM SETTINGS
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
                    system = LSystem.LSystem()

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

def openSystem(systemName):
    system = LSystem.LSystem()
    loadSystem(system, systemName)
    print "%s successfully loaded" % systemName

    while True:
        input = raw_input('> ').split()
        if input:
            cmd = input[0]
            args = input[1:]

            if cmd == 'exit':
                return
            elif cmd == 'settings':
                printVars(system)
                printConsts(system)
                printRules(system)
                printStart(system)
            elif cmd == 'state':

                if not args:
                    print "Error: please specify which states you want to generate"
                else:
                    states = []
                    stateNums = args

                    for stateNum in stateNums:
                        stateNum = stateNum.split('...')
                        if len(stateNum) == 1:
                            currentState = system.getState(int(stateNum[0]))
                            states.append(currentState)
                        else:
                            firstToGet = int(stateNum[0])
                            numToGet = int(stateNum[1]) - int(stateNum[0])
                            currentState = system.getState(firstToGet)
                            states.append(currentState)
                            for _ in range(numToGet):
                                currentState = system.iterate(currentState)
                                states.append(currentState)
                    for state in states:
                        print state

            else:
                invalidCommand()

def deleteSystem(systemName):
    fileName = "SystemFiles\\" + systemName + '.txt'
    try:
        os.remove(fileName)
        print "%s successfully deleted" % systemName
    except:
        print "Error: could not delete system"

# ---------------------------------------
# FUNCTIONS FOR edit() AND open()
# ---------------------------------------

# PRINTERS
def printVars(system):
    variables = system.getVars()
    
    print "    VARIABLES:"
    if variables:
        index = 1
        for var in variables:
            print ' '*4 + str(index) + ') ' + var
            index += 1
    else:
        print "    None"

def printConsts(system):
    constants = system.getConsts()
    
    print "    CONSTANTS:"
    if constants:
        index = 1
        for const in constants:
            print ' '*4 + str(index) + ') ' + const
            index += 1
    else:
        print "    None"

def printRules(system):
    rules = system.getRules()

    print "    RULES:"
    if rules:
        for rule in rules:
            print ' '*4 + rule + ') ' + rule + '-->' + rules[rule]
    else:
        print "    None"

def printStart(system):
    start = system.getStart()

    print "    START:"
    if start:
        print ' '*4 + start
    else:
        print "    None"

# FUNCTIONS FOR ADDING VARIABLES, CONSTANTS, ETC. TO SYSTEM
def addVar(system, var):
    try: 
        system.addVar(var)
    except:
        print "Error: invalid variable"

def addConst(system, const):
    try:
        system.addConst(const)
    except:
        print "Error: invalid constant"

def addRule(system, ruleFrom, ruleTo):
    try:
        system.addRule(ruleFrom, ruleTo)
    except:
        print "Error: invalid rule"

def addStart(system, start):
    try:
        system.addStart(start)
    except:
        print "Error: invalid start state"

# FUNCTIONS FOR DELETING VARIABLES, CONSTANTS, ETC. FROM SYSTEM
def deleteVar(system, var=None):
    try:
        system.deleteVar(var)
    except:
        print "Error: invalid variable"

def deleteConst(system, const=None):
    try:
        system.deleteConst(const)
    except:
        print "Error: invalid constant"

def deleteRule(system, rule=None):
    try:
        system.deleteRule(rule)
    except:
        print "Error: invalid rule"

def deleteStart(system):
    system.deleteStart()

# MISC
def save(system, systemName):
    try:
        fileName = 'SystemFiles\\' + systemName + '.txt'
        systemFile = open(fileName, 'w')

        variables = ' '.join(system.getVars())
        constants = ' '.join(system.getConsts())
        rules = ""
        for variable in system.getRules():
            rules = rules + variable + ' ' + system.getRules()[variable] + ','
        start = system.getStart()

        systemFile.write(variables)
        systemFile.write(' \n' + constants)
        systemFile.write(' \n' + rules)
        systemFile.write(' \n' + start)

        systemFile.close()

        print "%s saved successfully" % systemName

    except:
        print "Error: couldn't save system to file."

def loadSystem(system, systemName):
    fileName = 'SystemFiles\\' + systemName + '.txt'
    systemFile = open(fileName, 'r')
    
    variables = systemFile.readline().split()
    constants = systemFile.readline().split()
    rules = systemFile.readline().split(',')[:-1]
    start = systemFile.readline()

    systemFile.close()

    for var in variables:
        system.addVar(var)
    for const in constants:
        system.addConst(const)
    for rule in rules:
        rule = rule.split()
        system.addRule(rule[0], rule[1])
    system.addStart(start)

# --------------------------------------------
# INFORMATIONAL MESSAGE FUNCTIONS
# --------------------------------------------
def invalidCommand(command):
    print "    Error: %s is not a valid command. See 'help' for guidelines." % command

def help():
    print "HALP"

if __name__ == "__main__":
    main()