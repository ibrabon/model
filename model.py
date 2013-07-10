from pylab import *
import numpy
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import wx
import ast
global proverka
proverka =1
z=0 


def revision(slid, ctrl):
	p=False
	for i in range (0,7):
		if(slid[i].Value !=int(ast.literal_eval(ctrl[i].GetLineText(0)))):
			p=True
			break
		
	return p
def myfunc(y,t,b,c,A,w,m):
	z = (float(-b)*float(y[1])-c*float(y[0])+A*cos(w*t))/m	
	return z

class ModelFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,parent=None,id=-1,title='Modelmaker',size =wx.DisplaySize())
		self.panel =wx.Panel(self,-1,pos=(20,20))
		parametersNames = ['Massa = ',' b = ','c = ','A = ','w = ','y0 = ','T = ']
		self.parametersLabels =[]
		self.parametersSliders = []
		self.parametersCtrl = []
		stroka = []
		stroka1=[]
		self.panel.Refresh()
		for r in parametersNames:
			stroka.append(wx.StaticText(self.panel, -1, " ", size=(5,5)))
			self.parametersLabels.append(wx.StaticText(self.panel, -1, r, size=(50,40)))
			self.parametersSliders.append(wx.Slider(self.panel,-1,1,0,100,size=(250,-1),style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS))
			self.parametersCtrl.append(wx.TextCtrl(self.panel,-1,"5",size=(100,-1)))
		i=0
		while i<4:
			stroka1.append(wx.StaticText(self.panel, -1, size=(40,40)))
			i=i+1
			
		self.count=0
		button=wx.Button(self.panel,label="Close",size=(50,50))
		button1=wx.Button(self.panel,label ="Solve",size=(50,50))
		self.proverka=1		
		sizer = wx.FlexGridSizer(cols=4,hgap=50,vgap=40)
#		
		i=0
		while i<7:
			
			sizer.AddMany([stroka[i],self.parametersLabels[i], self.parametersSliders[i], self.parametersCtrl[i]])
			self.parametersSliders[i].SetTickFreq(100)
			i=i+1		
		sizer.AddGrowableRow(6)
		sizer.AddSpacer(100)
		sizer.Add(button)
		sizer.AddSpacer(100)
		sizer.Add(button1)
		self.panel.SetSizer(sizer)

#		self.label1 = wx.StaticText(self.panel, -1, "Solution:",pos=(20,200))
#		self.label2= wx.StaticText(self.panel,-1,"asdasdasd",pos=(70,200))
		self.Bind(wx.EVT_BUTTON,self.Solution,button1)
		
		self.Bind(wx.EVT_BUTTON,self.OnCloseMe, button)
		self.Bind(wx.EVT_CLOSE,self.OnCloseWindow)
		self.Bind(wx.EVT_ACTIVATE,self.Bonding)
		self.Bind(wx.EVT_SLIDER, self.Bonding)
		self.Bind(wx.EVT_TEXT,self.Web)
		
		
	
	def Web(self, event):
		for i in range(0,7):
			s=(self.parametersCtrl[i].GetLineText(0))
#			self.label2.LabelText=self.parametersCtrl[0].GetLineText(0)
			d = ast.literal_eval(s)*10
			self.parametersSliders[i].SetValue(int(d))
				

				
	def OnCloseMe(self,event):
		self.Close(True)
	
	def Bonding(self,event):
		s=[]
		for i in range(0,7):
			s.append(self.parametersSliders[i].GetValue()/10)
		for j in range(0,7):	
			self.parametersCtrl[j].SetLabelText(str(s[j]))
					
	def Solution(self,event):

		m=ast.literal_eval(self.parametersCtrl[0].GetLineText(0))
		b=ast.literal_eval(self.parametersCtrl[1].GetLineText(0))
		c=ast.literal_eval(self.parametersCtrl[2].GetLineText(0))
		A=ast.literal_eval(self.parametersCtrl[3].GetLineText(0))
		w=ast.literal_eval(self.parametersCtrl[4].GetLineText(0))
		yi =(ast.literal_eval(self.parametersCtrl[5].GetLineText(0)))
		T=ast.literal_eval(self.parametersCtrl[6].GetLineText(0))
		zi=(float(0.0))
		y0=[yi,zi]
		t=numpy.linspace(0, T, 1000)
		yn = odeint(myfunc,y0,t,args = (b,c,A,w,m) )
		fig = figure("Window title", figsize=(7,5))
		plt.plot(t,yn)
		plt.title(unicode("Sample plot"), bbox={'facecolor':'1.0', 'pad':5})
		#show()
		plt.savefig('test.png')
		plt.close()
		i=0
		while (i<2):
			png = wx.Image('test.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
			wx.StaticBitmap(self, -1, png, (700, 5), (png.GetWidth(), png.GetHeight()))
			i=i+1
		self.panel.Refresh()
		
	def OnCloseWindow(self,event):
		self.Destroy()
		
if __name__ == '__main__':
	app=wx.App()
	frame=ModelFrame()
	frame.Show()
	app.MainLoop()

	
	