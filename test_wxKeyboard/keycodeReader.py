'''
idea from:
http://stackoverflow.com/questions/1716035/wxpython-wx-keyevent-getkeycode
'''


import wx

keyMap = {}
for varName in vars(wx):
    if varName.startswith("WXK_"):
        keyMap[varName] = getattr(wx, varName)

print keyMap
