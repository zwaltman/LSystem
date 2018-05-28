"""
Load L-system settings from text file
"""
from modify import addVar, addConst, addRule, addStart


def loadSystem(system, systemName):
    """Load L-system settings from text file"""
    fileName = 'SystemFiles\\' + systemName + '.txt'
    systemFile = open(fileName, 'r')

    variables = systemFile.readline().split()
    constants = systemFile.readline().split()
    rules = systemFile.readline().split(',')[:-1]
    start = systemFile.readline()
    systemFile.close()

    for var in variables:
        addVar(system, var)

    for const in constants:
        addConst(system, const)

    for rule in rules:
        rule = rule.split()
        addRule(system, rule[0], rule[1])

    addStart(system, start)
