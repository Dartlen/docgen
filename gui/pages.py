#-*- coding:utf-8 -*-
import wx
from wx.grid import Grid
import wx.propgrid as wxpg
class PageOne(wx.Panel):
    """
    """
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        self.device=None
        sizer=wx.BoxSizer(wx.VERTICAL)

        self.text=wx.TextCtrl(self,size=(150,100))
        sizer.Add(self.text)

        self.label=wx.StaticText(self, wx.ID_ANY, ("None"))
        sizer.Add(self.label)
        self.grid=Grid(self)
        self.grid.CreateGrid(2,2)
        sizer.Add(self.grid)

        self.link=wx.Button(self,-1,'Attach')
        sizer.Add(self.link)

        self.button=wx.Button(self,-1,u'Сохранить')
        sizer.Add(self.button)
        self.Bind(wx.EVT_BUTTON,self.savevalue,self.button)

        self.hideall()
        self.Layout()
        self.SetSizer(sizer)
    def savevalue(self,event):
        if self.device.type_device==None:
            pass
        else:
            if self.device.type_device.lower()=="text":
                self.device.content=self.text.GetValue()
            if self.device.type_device.lower()=="table":
                self.device.content=[]
                for i in range(self.grid.GetNumberRows()):
                    l=[]
                    for k in range(self.grid.GetNumberCols()):
                        l.append(self.grid.GetCellValue(i,k))
                    self.device.content.append(l)
            if self.device.type_device.lower()=="link":
                pass
    def writevalue(self,event):
        if self.device.type_device==None:
            pass
        else:
            if self.device.type_device.lower()=="text":
                self.text.SetValue(self.device.content)
                pass
            if self.device.type_device.lower()=="table":
                if self.device.content=="":
                    self.grid.ClearGrid()
                else:
                    for i in range(self.grid.GetNumberRows()):
                        for k in range(self.grid.GetNumberCols()):
                            self.grid.SetCellValue(i,k,self.device.content[i][k])
            if self.device.type_device.lower()=="link":
                pass
    def hideall(self):
        self.link.Hide()
        self.grid.Hide()
        self.text.Hide()
        self.label.Hide()
        self.button.Hide()
    def mainedit(self,typedevice):
        content=typedevice.content
        typedevice=typedevice.type_device

        if typedevice==None:
            self.none(None)
            self.button.Hide()
        else:
            if typedevice.lower()=='table':
                self.table(content)
            if typedevice.lower()=='text':
                self.textopen(content)
            if typedevice.lower()=='link':
                self.ref(content)

    def none(self,content):
        self.hideall()
        self.label.Show()
        self.Layout()
    def table(self,content):
        self.hideall()
        self.grid.Show()
        self.button.Show()
        self.Layout()
    def textopen(self,content):
        self.hideall()
        self.text.SetValue(content)
        self.text.Show()
        self.button.Show()
        self.Layout()
    def ref(self,content):
        self.hideall()
        self.link.Show()
        self.button.Show()
        self.Layout()

class PageTwo(wx.Panel):
    '''
    '''
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.topsizer = wx.BoxSizer(wx.VERTICAL)
        self.pg = pg = wxpg.PropertyGridManager(self,
            style=wxpg.PG_SPLITTER_AUTO_CENTER |
                  wxpg.PG_AUTO_SORT,size=(300,300))

        self.pg.SetExtraStyle(wxpg.PG_EX_HELP_AS_TOOLTIPS)
        pg.AddPage( "Page 1 - Testing All" )




        self.topsizer.Add(self.pg)
        self.Layout()
        self.SetSizer(self.topsizer)
    def prop(self,device):
        self.pg.ClearPage(0)
        if device.propertylist==[]:
            pass
        else:
            count=1
            listpropery=["tag","type",'value']
            for i in device.propertylist:
                self.pg.Append( wxpg.PropertyCategory("%s."%count+"Property") )
                count+=1
                c=0
                for k in i:
                    self.pg.Append( wxpg.StringProperty("%s."%count+listpropery[c],value=str(k) ))
                    c+=1

class PageThree(wx.Panel):
    '''
    '''
    def __init__(self,parent):
        wx.Panel.__init__(self,parent=parent,id=wx.ID_ANY)
        self.text=wx.TextCtrl(self,size=(600,200),style=wx.TE_MULTILINE|wx.TE_PROCESS_TAB|wx.TE_PROCESS_ENTER)
    def open(self):
        f=open('texcode.tex','r')
        self.text.SetValue(f.read())
        f.close()