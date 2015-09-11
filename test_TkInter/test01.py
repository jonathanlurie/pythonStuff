# doc here https://wiki.python.org/moin/TkInter
# tuto there: http://effbot.org/tkinterbook/tkinter-application-windows.htm
# http://usingpython.com/using-tkinter/
# ref: http://effbot.org/tkinterbook/tkinter-index.htm#class-reference
# exemple of file dialog : http://tkinter.unpythonic.net/wiki/tkFileDialog

from Tkinter import *

root = Tk()

def callback():
    print "called the callback!"

# create a toolbar
toolbar = Frame(root)

b = Button(toolbar, text="new", width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)

b = Button(toolbar, text="open", width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

mainloop()
