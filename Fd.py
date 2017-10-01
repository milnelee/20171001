import wx


class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None, title='葛洲坝电厂发电分部')
        frame.Show()
        return True


app = MyApp()
app.MainLoop()