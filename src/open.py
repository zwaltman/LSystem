"""
Open previously saved L-system
"""
import LSystemObject
from message import invalidCommand
from load import loadSystem
from printer import printVars, printConsts, printRules, printStart

def openSystem(systemName):
    """Open previously saved L-system"""
    # Create new system, blank slate
    system = LSystemObject.LSystemObject()
    # Load system settings from file
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
                        # Split into start index and stop index, if range
                        stateNum = stateNum.split('...')

                        # If single state, get state
                        if len(stateNum) == 1:
                            currentState = system.getState(int(stateNum[0]))
                            states.append(currentState)

                        # If range of states, get all states in range
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
