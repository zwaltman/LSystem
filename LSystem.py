"""
MODULE FOR LSystem CLASS

Performs basic functions like modifying attributes of LSystem object,
as well as generating the state of an LSystem at a specific iteration.
"""

class LSystem:
    """Create, modify, generate states of L-System"""
    def __init__(self):
        self.variables = []
        self.constants = []
        self.rules = {}
        self.startState = ""

    # SYSTEM VARIABLES
    def addVar(self, var):
        self.variables.append(var)

    def getVars(self):
        return self.variables

    def deleteVar(self, index):
        del self.variables[index] 

    # SYSTEM CONSTANTS
    def addConst(self, const):
        self.constants.append(const)

    def getConsts(self):
        return self.constants

    def deleteConst(self, index):
        del self.constants[index]

    # SYSTEM RULES
    def addRule(self, a, b):
        self.rules[a] = b

    def getRules(self):
        return self.rules

    def deleteRule(self, char):
        del self.rules[char]

    # SYSTEM START STATE
    def setStartState(self, startState):
        self.startState = startState

    def getStartState(self):
        return self.startState

    def deleteStartState(self):
        self.startState = ""

    # OPERATIONS ON SYSTEM
    def applyRule(self, char):
        return self.rules[char]

    def iterate(self, state):
        return ''.join([self.applyRule(ch) for ch in state])

    def getState(self, num):
        state = self.startState
        for i in range(num):
            state = self.iterate(state)

        return state