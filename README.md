# LSystem
*L-system generator written in Python.*

[L-systems](https://en.wikipedia.org/wiki/L-system), a.k.a. Lindenmayer systems, are a type of abstract rewriting system whereby strings of symbols are rewritten according to given production rules to give states of a system. Their original motivation was in modeling biological systems, but they're applicable to modeling a range of systems including [finite truncations of fractals](https://en.wikipedia.org/wiki/L-system#Example_3:_Cantor_set).

As an example, Lindenmayer's original L-system, intended to model the growth of algae, is given by

  * *variables*: {A, B}
  
  * *constants*: {}
  
  * *axiom*: A
  
  * *rules*: {A --> AB, B --> A}
  
The 'axiom' is just the starting state of the system: the string we start with. 

The rules are those for rewriting. At each generation we replace each instance of A in the string with the string AB, and each instance of B with A. This is done in parallel so that conflicts are avoided and everything is well-defined.

Constants aren't used in this system, but they are used in others such as that for the [dragon curve](https://en.wikipedia.org/wiki/L-system#Example_6:_Dragon_curve) to indicate structural elements.

Variables are just substrings that get rewritten.

The first few generations of this system are

* n = 0 : A
* n = 1 : AB
* n = 2 : ABA
* n = 3 : ABAAB
* n = 4 : ABAABABA
* n = 5 : ABAABABAABAAB

(Coincidentally, the growth of the length of this system is exactly the Fibonacci sequence, and the proportion of this length made up of the character A goes to [phi](https://en.wikipedia.org/wiki/Golden_ratio) as n goes to infinity.)

## Using the program:

When the program is started (`python LSystem.py`), you will be in the main menu.

<b>In the main menu you can enter the following commands:</b>

`new`: create a new system which will open in the editor

`edit <filename>`: do the same with a saved system

`systems`: list saved system files in systemFiles

`delete <filename>`: delete system with name `<filename>`

`open <filename>`: open a saved system so that you can generate its states

`state x y z`: print system states with numbers x, y, and z. Can print as many as you want.

`state x...z`: print system states in range [x, z]

`exit`: exit application

<b>If you are in the editor creating a new system or editing an existing one, you can enter the following commands:</b>

`view`: view all current system settings

`view <attribute>`: view specific attribute settings. Ex: `view variables` prints just the current variables

`add <attribute>`: Ex: `add variable x`, `add rule a b`

`save <filename>`: Save current settings to file with name `<filename>`

`exit`: exit editor and return to main menu

## Files overview:

`LSystemObject.py` contains the class for L-system type objects. These include the attributes defining the system (variables, constants, rules, start state) and the methods for modifying those attributes and for generating states of the system.

All other files comprise the command line application through which the user can create, save, edit, and generate L-systems.

## Known issues:

The entire program works correctly if you know how to use it and always give correct input, but needs much better mechanisms for catching and responding to incorrect input. This is the main set of features currently being worked out.
