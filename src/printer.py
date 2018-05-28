"""
Printers for displaying L-System settings
"""

import LSystemObject


def printVars(system):
    """Print system variables"""
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
    """Print system constants"""
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
    """Print system rules"""
    rules = system.getRules()

    print "    RULES:"
    if rules:
        for rule in rules:
            print ' '*4 + rule + ') ' + rule + '-->' + rules[rule]
    else:
        print "    None"


def printStart(system):
    """Print system start state"""
    start = system.getStart()

    print "    START:"
    if start:
        print ' '*4 + start
    else:
        print "    None"
