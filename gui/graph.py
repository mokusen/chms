import wx
from . import mainGui

class Graph(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(500,500))

        # 閉じるイベント
        self.Bind(wx.EVT_CLOSE, self.frame_close)

        self.Centre()
        self.Show()

    def frame_close(self, event):
        self.Destroy()
        wx.Exit()
        mainGui.call_mainGui()

def call_graph():
    app = wx.App(True)
    Graph(None, wx.ID_ANY, title=u'BRS')
    app.MainLoop()