#!/usr/bin/env python

'''
Author      : Jonathan Lurie
Email       : lurie.jo@gmail.com
Version     : 0.1
Licence     : MIT
description : Not writen yet

Some doc    : http://eastmanreference.com/complete-list-of-applescript-key-codes/

'''

from appscript import app, k

def main():

    #app('System Events').keystroke('n', using=[k.shift_down, k.command_down])
    #app('System Events').keystroke('n', using=[])

    # for keys without description, we use key code
    #app('System Events').key_code("107")

    # cmd + down arrow
    #app('System Events').key_code("126", using=[k.command_down])

    app('iTunes').output_volume("50")

if __name__ == '__main__':
    main()
