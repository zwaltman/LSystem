"""
Application help, error messages, etc.
"""

def invalidCommand(command):
    """Invalid command error message"""
    print "    Error: %s is not a valid command. See 'help' for guidelines." % command

def help():
    """Help doc"""
    print ("In the main menu you can enter the following commands:\n" +
        "'new': create a new system which will open in the editor\n" +
        "'edit ': do the same with a saved system\n" +
        "'systems': list saved system files in systemFiles\n" +
        "'delete ': delete system with name\n" +
        "'open ': open a saved system so that you can generate its states\n" +
        "'state x y z': print system states with numbers x, y, and z. Can print as many as you want.\n" +
        "'state x...z': print system states in range [x, z]\n" +
        "'exit': exit application\n\n" +
        "If you are in the editor creating a new system or editing an existing one,\n" +
        "you can enter the following commands:" +
        "'view': view all current system settings\n" +
        "'view ': view specific attribute settings. Ex: 'view variables' prints just the current variables\n" +
        "'add ': Ex: 'add variable x', 'add rule a b'\n" +
        "'save ': Save current settings to file with name\n" +
        "'exit': exit editor and return to main menu\n\n")
