"""
Tests the class ThreadedPluginManager.
From a string that describes a plugin use, loads it, checks it
and launches it.


"""
import sys
from ThreadedPluginManager import *


# adding the plugin folder to PYTHONPATH
sys.path.append("plugins")


# a string calling a plugin as it is written in a mapping file
pluginString = "plugin|samplePlugin|helloWorld"
pluginString2 = "plugin|samplePlugin|methodWithArguments|9|10"

tpm = ThreadedPluginManager(pluginString2)


if(tpm.hasAValidFormat()):
    print("The format is valid.")

    # if it is valid, we load it
    tpm.loadPlugin()

    # once load, we launch it
    tpm.runPlugin()

else:
    print("The format is NOT valid.")
