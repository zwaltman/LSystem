"""
For viewing and deleting L-system files from main menu
"""
from os import listdir, remove

def listSystems():
    """List all existing saved L-system files in directory 'systemFiles' """
    systemList = listdir("SystemFiles")
    for fileName in systemList:
        print fileName

def deleteSystem(systemName):
    """Delete saved L-system file in directory 'systemFiles' with given name"""
    fileName = "SystemFiles\\" + systemName + '.txt'
    try:
        remove(fileName)
        print "%s successfully deleted" % systemName
    except:
        print "Error: could not delete system"