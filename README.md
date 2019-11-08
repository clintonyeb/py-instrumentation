# Python Instrumentation

This module is a proof of concept that python modules/files can be weaved.

The main file doing the heavy work is: `aspect.py`
It exports one function called weave with a module has to call with its name.

For example: To weave a Python module:

1. Import weave from the aspect module: `from aspect import weave`
2. Call the weave method providing the name of the module you want to weave, in this case the current module.
Example: `weave(sys.modules[__name__])`

How To Run:

1. The project includes a Test bed named `test.py`
2. You can simply run it by calling `python test.py`
3. It will produce a log file: `method-calls.log` which will contain the method calls during its execution.

Future Work:
1. Make the project pip installable. This way projects can easily use it.