# LSystem
L-system generator written in Python.

## Using the program:

When the program is started (`python LSystem.py`), you will be in the main menu.

<b>In the main menu you can enter the following commands:</b>

`new`: create a new system which will open in the editor

`edit <filename>`: do the same with a saved system

`systems`: list saved system files in systemFiles

`delete <filename>`: delete system with name <filename>

`open <filename>`: open a saved system so that you can generate its states

`state x y z`: print system states with numbers x, y, and z. Can print as many as you want.

`state x...z`: print system states in range [x, z]

`exit`: exit application

<b>If you are in the editor creating a new system or editing an existing one, you can enter the following commands:</b>

`view`: view all current system settings

`view <attribute>`: view specific attribute settings. Ex: 'view variables' prints just the current variables

`add <attribute>`: Ex: `add variable x`, `add rule a b`

`save <filename>`: Save current settings to file with name <filename>

`exit`: exit editor and return to main menu

# Files overview:

`LSystemObject.py` contains the class for L-system type objects. These include the attributes defining the system (variables, constants, rules, start state) and the methods for modifying those attributes and for generating states of the system.

All other files comprise the command line application through which the user can create, save, edit, and generate L-systems.

# Known issues:

The entire program works correctly if you know how to use it and always give correct input, but needs much better mechanisms for catching and responding to incorrect input. This is the main set of features currently being worked out.
