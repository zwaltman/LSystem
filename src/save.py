"""
Save L-system settings to text file
"""
import LSystemObject

def save(system, systemName):
    """Save L-system settings to text file"""
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
