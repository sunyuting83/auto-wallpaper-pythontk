import wx

class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=-1,
                          title="Hello World", size=(300, 300))

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)

        txt = wx.StaticText(panel, -1, "Hello World!")
        sizer.Add(txt, 0, wx.TOP | wx.LEFT, 100)

        self.Center()


app = wx.App()
