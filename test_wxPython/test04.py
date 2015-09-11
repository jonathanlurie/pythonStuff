import wx
import wx.html2

import time









# Frame specialized to display youtube content
class HtmlDisplay(wx.Frame):
    _browser = None

    _youtubeUrlPattern = r"""
    <iframe width="853" height="480" src="https://www.youtube-nocookie.com/embed/{ID}?autoplay=1" frameborder="0" allowfullscreen></iframe>
    """

    def __init__(self, *args, **kwds):

        wx.Frame.__init__(self, *args, **kwds)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self._browser = wx.html2.WebView.New(self)
        sizer.Add(self._browser, 1, wx.EXPAND, 10)
        self.SetSizer(sizer)
        self.SetSize((900, 700))



    def setHtmlFile(self, fileAddress):
        htmlContent = self._loadTextFile(fileAddress)

        self._browser.SetPage(htmlContent,"")



    # reads a text file and return a string of its content
    def _loadTextFile(self, fileAddress):
        strContent = ""

        try:
            with open(fileAddress) as f:
                content = f.readlines()

                strContent = "".join(content)
        except IOError as e:
            print("ERROR : file " + fileAddress + " not found.")

        return strContent



if __name__ == '__main__':
  app = wx.App()



  htmlD = HtmlDisplay(None, -1)


  htmlD.setHtmlFile("content.html")
  htmlD.Show()

  app.MainLoop()
