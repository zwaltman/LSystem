"""
For adding and deleting settings from L-systems
"""

import LSystemObject


def addVar(system, var):
    """Add variable to system"""
    try: 
        system.addVar(var)
    except:
        print "Error: invalid variable"


def addConst(system, const):
    """Add constant to system"""
    try:
        system.addConst(const)
    except:
        print "Error: invalid constant"


def addRule(system, ruleFrom, ruleTo):
    """Add rule to system"""
    try:
        system.addRule(ruleFrom, ruleTo)
    except:
        print "Error: invalid rule"


def addStart(system, start):
    """Add start state to system"""
    try:
        system.addStart(start)
    except:
        print "Error: invalid start state"


def deleteVar(system, var=None):
    """Delete variable from system"""
    try:
        system.deleteVar(var)
    except:
        print "Error: invalid variable"


def deleteConst(system, const=None):
    """Delete constant from system"""
    try:
        system.deleteConst(const)
    except:
        print "Error: invalid constant"


def deleteRule(system, rule=None):
    """Delete rule from system"""
    try:
        system.deleteRule(rule)
    except:
        print "Error: invalid rule"


def deleteStart(system):
    """Delete start state from system"""
    system.deleteStart()
