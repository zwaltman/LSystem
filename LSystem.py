"""
MODULE FOR LSystem CLASS

Performs basic functions like modifying attributes of LSystem object,
as well as generating the state of an LSystem at a specific iteration.
"""

# Zach Waltman 
# z.waltman@gmail.com

class LSystem:
    """Create, modify, generate states of L-System"""
    def __init__(self):
        self.variables = []
        self.constants = []
        self.rules = {}
        self.start = ""

    # SYSTEM VARIABLES
    def addVar(self, var):
        if var not in self.variables:
            self.variables.append(var)

    def getVars(self):
        return self.variables

    def deleteVar(self, index=None):
        if index == None:
            self.variables = []
        else:
            del self.variables[index] 

    # SYSTEM CONSTANTS
    def addConst(self, const):
        if const not in self.constants:
            self.constants.append(const)

    def getConsts(self):
        return self.constants

    def deleteConst(self, index=None):
        if index == None:
            self.constants = []
        else:
            del self.constants[index]

    # SYSTEM RULES
    def addRule(self, a, b):
        self.rules[a] = b

    def getRules(self):
        return self.rules

    def deleteRule(self, char=None):
        if char == None:
            self.rules = {}
        else:
            del self.rules[char]

    # SYSTEM START STATE
    def addStart(self, start):
        self.start = start

    def getStart(self):
        return self.start

    def deleteStart(self):
        self.start = ""

    # OPERATIONS ON SYSTEM
    def applyRule(self, char):
        return self.rules[char]

    def iterate(self, state):
        return ''.join([self.applyRule(ch) for ch in state])

    def getState(self, num):
        state = self.start
        for i in range(num):
            state = self.iterate(state)

        return state
