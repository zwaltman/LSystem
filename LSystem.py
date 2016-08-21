"""
Class for L-System objects.

Allows basic functions like creating L-system object and modifying its attributes,
as well as generating the state of the system at a specific iteration.
"""

class LSystem:
    """Create, modify, generate states of L-System"""
    def __init__(self):
        self.variables = []
        self.constants = []
        self.rules = {}
        self.start = ""

    # SYSTEM VARIABLES
    def addVar(self, var):
        """Add variable if it doens't already exist"""
        if var not in self.variables:
            self.variables.append(var)

    def getVars(self):
        return self.variables

    def deleteVar(self, index=None):
        """Deletes variable at index if index given, deletes all variables otherwise"""
        if index == None:
            self.variables = []
        else:
            del self.variables[index] 

    # SYSTEM CONSTANTS
    def addConst(self, const):
        """Add constant if it doesn't already exist"""
        if const not in self.constants:
            self.constants.append(const)

    def getConsts(self):
        return self.constants

    def deleteConst(self, index=None):
        """Deletes constant at index if index given, deletes all constants otherwise"""
        if index == None:
            self.constants = []
        else:
            del self.constants[index]

    # SYSTEM RULES
    def addRule(self, a, b):
        """Add rule if it doesn't already exist"""
        self.rules[a] = b

    def getRules(self):
        return self.rules

    def deleteRule(self, char=None):
        """Deletes rule for char if char given, deletes all rules otherwise"""
        if char == None:
            self.rules = {}
        else:
            del self.rules[char]

    # SYSTEM START STATE
    def addStart(self, start):
        """Add start state if it doesn't already exist"""
        self.start = start

    def getStart(self):
        return self.start

    def deleteStart(self):
        """Deletes start state"""
        self.start = ""

    # GENERATING SYSTEM STATES
    def applyRule(self, char):
        """Applies rule for char on char, returns result"""
        return self.rules[char]

    def iterate(self, state):
        """Iterates state of system by 1"""
        return ''.join([self.applyRule(ch) for ch in state])

    def getState(self, n):
        """Returns system's nth state"""
        state = self.start
        for i in range(n):
            state = self.iterate(state)

        return state