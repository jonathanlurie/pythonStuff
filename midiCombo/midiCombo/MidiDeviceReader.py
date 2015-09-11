"""

MidiDeviceReader give the material for reading MIDI device inputs.


"""

import sys
import os
import time

import pygame
import pygame.midi
from pygame.locals import *

class MidiDeviceReader:

    _deviceId = None
    _input = None

    _eventGet = None
    _eventPost = None

    # does the bridge to plugins
    _commanInterpreter = None



    # Constructor
    # deviceName is to look for a specific device
    # If None, MidiDeviceReader take the first MIDI device
    # available for input
    def __init__(self, deviceName = None):

        # initializing Pygame
        pygame.init()
        pygame.fastevent.init()
        self._eventGet = pygame.fastevent.get
        self._eventPost = pygame.fastevent.post

        # initializing Pygame.midi
        pygame.midi.init()


        # define device name or take a default name
        if(deviceName is None):
            self._deviceId = pygame.midi.get_default_input_id()
        else:
            self._deviceId = self._getdeviceIdFromName(deviceName)


        try:
            # input slection
            self._input = pygame.midi.Input( self._deviceId )
            #self.readFlow()
            #del self._input
        except pygame.midi.MidiException, e:

            print("ERROR: impossible to find the device named " + deviceName + "\n")
            self._printDeviceInfo()
            #print("(" + str(e) + ")" )
            self.close()
            exit()


    def setCommandInterpreter(self, ci):
        self._commanInterpreter = ci

    def _printDeviceInfo(self):
        print("INFO: here is the list of MIDI devices available for input:")

        for i in range( pygame.midi.get_count() ):
            r = pygame.midi.get_device_info(i)
            (interf, name, input, output, opened) = r

            in_out = ""
            if input:
                print("\t- Name: " + str(name) + "\tInterface: " + str(interf) )

    # PRIVATE
    # fetch all MIDI devices connected and look for the on named "deviceName"
    # in order to retrieve its ID
    def _getdeviceIdFromName(self, deviceName):
        for i in range( pygame.midi.get_count() ):
            r = pygame.midi.get_device_info(i)
            (interf, name, input, output, opened) = r


            if(input and name == deviceName):
                return i

            # if nothing was found...
            return -1



    # Reads te main flow from MIDI device and then calls _processData
    # to do something with it
    def readFlow(self):

        going = True

        # read the flow...
        while going:
            """
            events = event_get()
            for e in events:
                if e.type in [QUIT]:
                    going = False
                if e.type in [KEYDOWN]:
                    going = False
            """


            # avoid 100/100 CPU usage!
            time.sleep(0.01)

            if self._input.poll():
                midiEvents = self._input.read(10)

                numberOfEvents = len(midiEvents)

                # an event array is like that (2 events in this example)
                # [[[128, 52, 127, 0], 2964], [[128, 50, 127, 0], 2973]]

                #print(midiEvents)

                # we fetch all events data
                for ev in midiEvents:
                    # the timestamp since launch
                    timestamp = ev[1]

                    # P for press and R for release
                    pressOrRelease = None
                    print ev[0][0]
                    if(ev[0][0] == 128 ):
                        pressOrRelease = 'R'
                    else:
                        pressOrRelease = 'P'

                    # key index within the MIDI device
                    keyIndex = ev[0][1]

                    # velocity (1 to 127) the bigger, the fastest push
                    velocity = ev[0][2]

                    # exit sequence for TESTING
                    if(keyIndex == 0):
                        going = False

                    self._processData( timestamp, pressOrRelease, keyIndex, velocity)


        self.close()




    # PRIVATE
    # process the data taken from the MIDI device
    def _processData(self, timestamp, pressOrRelease, keyIndex, velocity):
        print("[" + str(timestamp) + "]\tKeyIndex: " + str(keyIndex) + " Press/Release: " + pressOrRelease + " Velocity: " + str(velocity))

        # convert the signal to a recognizable key (in a map point of view)
        key = str(keyIndex) + pressOrRelease

        # relay the instruction to the command interpreter
        self._commanInterpreter.executeCommandFromKey(key)

    # PRIVATE
    # calls at the end, to delete the input object
    def close(self):
        try:
            del self._input
        except AttributeError, e:
            print("WARNING: the MIDI device object has already been deleted.")

        pygame.midi.quit()
