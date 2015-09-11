'''
le layout QWERTY est celui par default, mais il doit etre remplace par le
layout local, AZERTY.
On trouve un comparatif ici:
http://stackoverflow.com/questions/3202629/where-can-i-find-a-list-of-mac-virtual-key-codes
http://i.stack.imgur.com/LD8pT.png

'''



from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time


def callArray(ar = []):
    print ar

def callSequence(*args):
    m = PyMouse()
    k = PyKeyboard()

    print args
    #k.press_keys(args)
    #k.type_string(args[0])
    keys = ["cmd", "a"]

    #callArray(keys)

    k.press_keys(keys)

    #k.press_key("cmd")
    #k.press_key("a")








# wait a bit
print("wait 2 seconds...")
time.sleep(2)

print("click!")

# Mac example
#k.press_keys(['Command','n'])



callSequence('[|]?./+%./+*1234567890')
