
import wx
import ast
global proverka
proverka =1 

def revision(slid, ctrl):
	p=False
	for i in range (0,7):
		if(slid[i].Value !=int(ast.literal_eval(ctrl[i].GetLineText(0)))):
			p=True
			break
		
	return p

class ModelFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,parent=None,id=-1,title='Modelmaker',size =(1000,1000))
		panel =wx.Panel(self,-1,pos=(20,20))
		parametersNames = ['Massa = ',' b = ','c = ','A = ','w = ','y0 = ','T = ']
		self.parametersLabels =[]
		self.parametersSliders = []
		self.parametersCtrl = []
		stroka = []
		stroka1=[]
		for r in parametersNames:
			stroka.append(wx.StaticText(panel, -1, " ", size=(90,40)))
			self.parametersLabels.append(wx.StaticText(panel, -1, r, size=(90,40)))
			self.parametersSliders.append(wx.Slider(panel,100,0,0,100,size=(250,-1),style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS))
			self.parametersCtrl.append(wx.TextCtrl(panel,-1,"5",size=(175,-1)))
		i=0
		while i<4:
			stroka1.append(wx.StaticText(panel, -1, size=(40,40)))
			i=i+1
			
		self.count=0
		button=wx.Button(panel,label="Close",size=(50,50))
		button1=wx.Button(panel,label ="Solve",size=(50,50))
		self.proverka=1		
		sizer = wx.FlexGridSizer(cols=4,hgap=50,vgap=40)
#		sizer1=wx.FlexGridSizer(rows=4,cols=4,hgap=50,vgap=40)
		i=0
		while i<7:
			
			sizer.AddMany([stroka[i],self.parametersLabels[i], self.parametersSliders[i], self.parametersCtrl[i]])
			self.parametersSliders[i].SetTickFreq(100)
			i=i+1		
		sizer.AddGrowableRow(6)
		sizer.AddSpacer(100)
		#panel.Fit()
		sizer.Add(button)
		sizer.AddSpacer(100)
		sizer.Add(button1)
		panel.SetSizer(sizer)

#		self.slider=wx.Slider(panel,100,0,0,100,pos=(10,10),size=(250,-1),style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS)
		self.label1 = wx.StaticText(panel, -1, "Solution:",pos=(20,200))
		self.label2= wx.StaticText(panel,-1,"asdasdasd",pos=(70,200))
# 		#self.slider.SetTickFreq(5)
		
		self.Bind(wx.EVT_BUTTON,self.OnCloseMe, button)
		self.Bind(wx.EVT_CLOSE,self.OnCloseWindow)
		self.Bind(wx.EVT_ACTIVATE,self.Bonding)
#		if((revision(self.parametersSliders,self.parametersCtrl))):
		self.Bind(wx.EVT_SLIDER, self.Bonding)
#		if(revision(self.parametersSliders,self.parametersCtrl)):
			#if(revision(self.parametersSliders,self.parametersCtrl)):
		self.Bind(wx.EVT_TEXT,self.Web)
#		self.label2.LabelText = str(revision(self.parametersSliders,self.parametersCtrl))
		
		
	
	def Web(self, event):
		for i in range(0,7):
			s=(self.parametersCtrl[i].GetLineText(0))
			self.label2.LabelText=self.parametersCtrl[0].GetLineText(0)
			d = ast.literal_eval(s)
			self.parametersSliders[i].SetValue(int(d))
				

				
	def OnCloseMe(self,event):
		self.Close(True)
	
	def Bonding(self,event):
		s=[]
		for i in range(0,7):
			s.append(self.parametersSliders[i].GetValue())
		for j in range(0,7):	
			self.parametersCtrl[j].SetLabelText(str(s[j]))
				
	
	def OnCloseWindow(self,event):
		self.Destroy()
		
if __name__ == '__main__':
	app=wx.App()
	frame=ModelFrame()
	frame.Show()
	app.MainLoop()

	
	