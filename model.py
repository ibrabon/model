
import wx

class ModelFrame(wx.Frame):

	def __init__(self):
		wx.Frame.__init__(self,parent=None,id=-1,title='Modelmaker',size =(400,400))
		panel =wx.Panel(self,-1)
		self.count=0
		self.button=wx.Button(panel,label="Close",pos=(220,210),size=(50,50))
		self.button1=wx.Button(panel,label ="Solve",pos=(20,100),size=(50,50))
		self.slider=wx.Slider(panel,100,0,0,100,pos=(10,10),size=(250,-1),style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS)
		self.label1 = wx.StaticText(panel, -1, "Solution:",pos=(20,200))
		self.label2= wx.StaticText(panel,-1,"",pos=(70,200))
		self.slider.SetTickFreq(5)
		self.Bind(wx.EVT_BUTTON,self.OnCloseMe, self.button)
		self.Bind(wx.EVT_CLOSE,self.OnCloseWindow)
		self.Bind(wx.EVT_BUTTON,self.Solving,self.button1)
		
		
		
	def OnCloseMe(self,event):
		self.Close(True)
	
	def Solving(self,event):
		s = self.slider.Value
		self.label2.SetLabelText(str(s))
	
	def OnCloseWindow(self,event):
		self.Destroy()
		
if __name__ == '__main__':
	app=wx.PySimpleApp()
	frame=ModelFrame()
	frame.Show()
	app.MainLoop()
