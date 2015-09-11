

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time



# type a string (dont use tab!)
def typeString(s):
    #m = PyMouse()
    k = PyKeyboard()

    #print args
    #k.press_keys(args)
    k.type_string(s)



# perform a combo like cmd + a or something
def combo(*arg):
    k = PyKeyboard()
    k.press_keys(arg)
