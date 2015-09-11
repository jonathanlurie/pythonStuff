import Tkinter as tkinter
import tkFileDialog
import Tkconstants


class DuskrView:
    _mainWindow = None
    _backgroundImageLabel = None
    _logo = None
    _step1Label = None
    _fileSelectionButton = None
    _step2Label = None
    _goProcessButton = None
    _firstRawFilename = None

    def __init__(self):
        # create a new window
        self._mainWindow = tkinter.Tk()

        # give a title to the window
        self._mainWindow.title("Duskr")

        # set window size
        self._mainWindow.geometry("320x500")

        # display image on the backfroung
        self._logo = tkinter.PhotoImage(file="images/logo.gif")
        self._backgroundImageLabel = tkinter.Label(self._mainWindow, image=self._logo)
        self._backgroundImageLabel.pack()

        # display step 1
        self._step1Label = tkinter.Label(self._mainWindow, text="\nStep 1 :\nOpen the first raw file of your sequence\n", font=("Helvetica", 14), fg="gray")
        self._step1Label.pack()

        self._fileSelectionButton = tkinter.Button(self._mainWindow, command=self.openFile, text="Open file")
        self._fileSelectionButton.pack()

        self._mainWindow.mainloop()


    def openFile(self):


        self._firstRawFilename = tkFileDialog.askopenfilename()

        print self._firstRawFilename

        # can be restricted to some files
        #filename = tkFileDialog.askopenfilename(filetypes=[("Text files","*.txt"), ("Gif Images", "*.gif")])

        #print(self._firstRawFilename)

        self._fileSelectionButton.pack_forget()
        self._step1Label.pack_forget()

        self.displayStep2()



    def displayStep2(self):
        print "here is step 2"
        #fileExtension = self._firstRawFilename

        # label
        self._step2Label = tkinter.Label(self._mainWindow, text="\nStep 2 :\nClick on the GO! button to\nstart the interpolation process\n", font=("Helvetica", 14), fg="gray")
        self._step2Label.pack()

        # button
        self._goProcessButton = tkinter.Button(self._mainWindow, command=self.startInterpolation, text="Go!")
        self._goProcessButton.pack()

    def startInterpolation(self):
        print("Let's Rock!")






def openFile():

    filename = tkFileDialog.askopenfilename(filetypes=[("Text files","*.txt"), ("Gif Images", "*.gif")])
    print(filename)


if __name__=='__main__':

    dskv = DuskrView()


    exit()
    # ** main window Creation **

    # create a new window
    window = tkinter.Tk()

    # give a title to the window
    window.title("Duskr")

    # set window size
    window.geometry("320x500")





    # ** Labels Creation **

    #topLabel = tkinter.Label(window, text="this is the top label")
    #topLabel.pack()


    logo = tkinter.PhotoImage(file="logo2.gif")
    #logo2 = logo.subsample(2, 2)
    imgLabel = tkinter.Label(window, image=logo)#.grid()
    imgLabel.pack()


    midLabel = tkinter.Label(window, text="Step 1 :\nOpen the first raw file of your sequence\n", font=("Helvetica", 14), fg="gray")
    midLabel.pack()




    # ** text field Creation **
    #txtFieldValue = tkinter.StringVar()
    #txtFieldValue.set("a default value")
    #txtField = tkinter.Entry(window, textvariable=txtFieldValue, fg="#FF00FF")
    #txtField.pack()



    # ** button Creation **
    btnSelect = tkinter.Button(window, command=openFile, text="Open file")
    btnSelect.pack()


    #TkFileDialogExample(window).pack()

    # draw the window and start application
    window.mainloop()
