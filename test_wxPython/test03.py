import wx
import wx.html2

import time


# Frame specialized to display youtube content
class YoutubeBrowser(wx.Frame):
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



    def setYoutubeID(self, id):
        definedYoutubeUrl = self._youtubeUrlPattern.replace('{ID}', id)

        self._browser.SetPage(definedYoutubeUrl,"")




if __name__ == '__main__':
  app = wx.App()



  ytb = YoutubeBrowser(None, -1)


  #ytb.setYoutubeID("otUK0hj_ySg")
  #ytb.Show()


  #time.sleep(5)

  ytb.setYoutubeID("6GL3qQa9kN0")
  ytb.Show()

  app.MainLoop()
