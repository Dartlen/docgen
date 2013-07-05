# -*- coding: utf-8 -*-
import wx
import wx.aui
from copy import deepcopy
import pickle
from engine.idevicestore import IdeviceStore
from pages import PageOne,PageTwo,PageThree
from menu import ContextMenuTree
from worktree import MyTreeCtrl

def hhh():
    app = wx.App(0)
    frame_1 = TestGui(None, -1, "DocGen")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()


class TestGui(wx.Frame,ContextMenuTree,IdeviceStore):
    def __init__(self, parent, id=-1, title="", pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE |
                                            wx.SUNKEN_BORDER |
                                            wx.CLIP_CHILDREN):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        super(ContextMenuTree,self).__init__()
        IdeviceStore.__init__(self)

        self.loadDevices()



        self.menubar = wx.MenuBar()
        menu = wx.Menu()
        Doc=menu.Append(wx.NewId(),u'Обход документа','',wx.ITEM_NORMAL)
        Save=menu.Append(wx.NewId(),u'Сохранить','',wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU,self.SaveTree,Save)
        Open=menu.Append(wx.NewId(),u'Загрузить','',wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU,self.OpenTree,Open)
        AppendText=menu.Append(wx.NewId(), u"2", "", wx.ITEM_NORMAL)
        Gen=menu.Append(wx.NewId(),u'Генерация','',wx.ITEM_NORMAL)
        menu.Append(wx.ID_EXIT, u"Exit",)
        self.menubar.Append(menu, u"Документ")
        menu2=wx.Menu()

        self.Bind(wx.EVT_MENU,self.Renderrrr,Gen)


        self.SetMenuBar(self.menubar)

        # tell FrameManager to manage this frame



        self._mgr = wx.aui.AuiManager()
        self._mgr.SetManagedWindow(self)
        self._mgr.AddPane(self.CreateInteractiveTree(), wx.aui.AuiPaneInfo().
                          Name("test8").Caption(u"Структура документа").
                          Left().Layer(1).Position(1).CloseButton(True).MaximizeButton(True).MinSize(wx.Size(150, 100)))

        self._mgr.AddPane(self.CreateTreeCtrl(), wx.aui.AuiPaneInfo().Name("test2").Caption(u"Элементы документа").
        Left().Layer(1).Position(1).CloseButton(True).MaximizeButton(True).MinSize(wx.Size(150, 200)))

        self.One=self.AppendContent()

        self._mgr.AddPane(self.One,wx.aui.AuiPaneInfo().Name("test3").Caption(u"Панель заполнения контента")
        .Center().Layer(1).Position(1).CloseButton(True).MaximizeButton(True).MinSize(wx.Size(150, 200)))

        self.Two=self.CreateMainPanel()

        self._mgr.AddPane(self.Two,wx.aui.AuiPaneInfo().Name("test4").Caption(u"Настройки")
        .Center().Layer(1).Position(1).CloseButton(True).MaximizeButton(True).MinSize(wx.Size(100, 50)))

        self._mgr.Update()

        #===================================
        #self.Bind(wx.EVT_BUTTON,self.appenditemintree,source=self.appendbutton)
        self.Bind(wx.EVT_CONTEXT_MENU, self.OnContextMenu)
        self.Bind(wx.EVT_MENU,self.appenditemintree,id=wx.ID_ADD)
        self.Bind(wx.EVT_TREE_SEL_CHANGED,self.change)




    def change(self,event):
        if self.tree.GetSelections()[0]==event.GetItem():

            devicetype=self.tree.GetPyData(event.GetItem())

            self.One.device=devicetype
            self.One.writevalue(devicetype)
            self.One.mainedit(devicetype)
            self.tabTwo.prop(devicetype)
    def AppendContent(self):
        panel=PageOne(self)
        return panel

    def CreateMainPanel(self):
        self.panel=wx.Panel(self,size=(self.GetSize()+(10,10)))
        self.book=wx.Notebook(self.panel,wx.ID_ANY,size=(500,500))
        #self.book.SetClientSize(self.panel.GetSize()+(10,10))
        self.tabOne = PageThree(self.book)
        self.tabTwo = PageTwo(self.book)
        self.tabTwo.SetBackgroundColour(u'Gray')
        self.tabOne.SetBackgroundColour(u"Gray")
        self.book.AddPage(self.tabTwo, u'Свойства')
        self.book.AddPage(self.tabOne, u"Исходный код")
        return self.panel

    def CreateTreeCtrl(self):
        #panel=wx.Panel(self)
        #sizer=wx.BoxSizer(wx.VERTICAL)
        self.tree2 = wx.TreeCtrl(self, -1,style=wx.TR_DEFAULT_STYLE|wx.TR_HIDE_ROOT,size=(200,175))
        #sizer.Add(self.tree2)
        #self.appendbutton=wx.Button(panel,wx.ID_ANY,u"Добавить")
        #sizer.Add(self.appendbutton)
        #panel.SetSizer(sizer)
        #panel.Layout()
        root = self.tree2.AddRoot("lol") #Заголовок дерева
        for i in self.idevices:
            item=self.tree2.AppendItem(root,i.name)
            self.tree2.SetPyData(item,i)
        return self.tree2

    def appenditemintree(self,event):
        item=deepcopy(self.tree2.GetPyData(self.tree2.GetSelection()))
        appenditem=self.tree.AppendItem(self.root,item.name)
        isize = (16,16)
        il = wx.ImageList(isize[0], isize[1])
        fldridx   = il.Add(wx.ArtProvider_GetBitmap(wx.ART_REPORT_VIEW,  wx.ART_OTHER, isize))
        fldropenidx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_REPORT_VIEW, wx.ART_OTHER,isize))
        self.tree.SetItemImage(appenditem, fldridx, wx.TreeItemIcon_Normal)
        self.tree.SetItemImage(appenditem, fldropenidx, wx.TreeItemIcon_Selected)
        self.tree.SetPyData(appenditem,item)
        self.tree.Expand(self.root)

        #self.append(item)
        #self.tree.SetFocusedItem(appenditem)

    def CreateInteractiveTree(self):
        tID = wx.NewId()
        self.tree = MyTreeCtrl(self, tID, wx.DefaultPosition, wx.DefaultSize,
            wx.TR_HAS_BUTTONS|wx.TR_EDIT_LABELS )
        isize = (16,16)
        il = wx.ImageList(isize[0], isize[1])
        fldridx   = il.Add(wx.ArtProvider_GetBitmap(wx.ART_REPORT_VIEW,  wx.ART_OTHER, isize))
        fldropenidx = il.Add(wx.ArtProvider_GetBitmap(wx.ART_REPORT_VIEW, wx.ART_OTHER,isize))
        fileidx   = il.Add(wx.ArtProvider_GetBitmap(wx.ART_REPORT_VIEW, wx.ART_OTHER,isize))
        self.tree.SetImageList(il)
        self.il = il
        self.root = self.tree.AddRoot(u"Документ")

        class root:
            def __init__(self):
                self.param_container =  True
                self.type_device     =  'Root'
                self.content         =  None
                self.propertylist    =  []

        self.tree.SetPyData(self.root,root())
        self.tree.SetItemImage(self.root, fldridx, wx.TreeItemIcon_Normal)
        self.tree.SetItemImage(self.root, fldropenidx, wx.TreeItemIcon_Expanded)
        self.tree.Expand(self.root)

        # These go at the end of __init__

        self.tree.Bind(wx.EVT_TREE_BEGIN_DRAG, self.OnBeginLeftDrag)
        self.tree.Bind(wx.EVT_TREE_END_DRAG, self.OnEndDrag)

        return self.tree

    def OnBeginLeftDrag(self, event):
        '''Allow drag-and-drop for leaf nodes.'''

        event.Allow()
        self.dragType = "left button"
        self.dragItem = event.GetItem()

    def OnBeginRightDrag(self, event):
        '''Allow drag-and-drop for leaf nodes.'''

        event.Allow()
        self.dragType = "right button"
        self.dragItem = event.GetItem()

    def OnEndDrag(self, event):
        #print "OnEndDrag"

        # If we dropped somewhere that isn't on top of an item, ignore the event
        if event.GetItem().IsOk():
            target = event.GetItem()
        else:
            return

        # Make sure this member exists.
        try:
            source = self.dragItem
        except:
            return

        # Prevent the user from dropping an item inside of itself
        if self.tree.ItemIsChildOf(target, source):
            print "the tree item can not be moved in to itself! "
            self.tree.Unselect()
            return

        # Get the target's parent's ID
        targetparent = self.tree.GetItemParent(target)
        if not targetparent.IsOk():
            targetparent = self.tree.GetRootItem()

        # One of the following methods of inserting will be called...
        def MoveHere(event):
            # Save + delete the source
            save = self.tree.SaveItemsToList(source)
            self.tree.Delete(source)
            newitems = self.tree.InsertItemsFromList(save, targetparent, target)
            #self.tree.UnselectAll()
            for item in newitems:
                self.tree.SelectItem(item)

        def InsertInToThisGroup(event):
            # Save + delete the source
            save = self.tree.SaveItemsToList(source)
            self.tree.Delete(source)
            newitems = self.tree.InsertItemsFromList(save, target)
            for item in newitems:
                self.tree.SelectItem(item)

        if self.tree.GetPyData(target).param_container==True:
            InsertInToThisGroup(target)
        else:
            pass

    def OnSize(self, event):
        w,h = self.GetClientSizeTuple()
        self.tree.SetDimensions(0, 0, w, h)

    def OnExit(self, event):
        self.Close()

    def SaveTree(self,events):
        list=[]
        for i in self.MyDoc(self.tree,self.root):
            words=self.tree.SaveItemsToList(i)
            list.append(words)
        na_file = open('object', 'w')
        pickle.dump(list,na_file)
        na_file.close()

    def OpenTree(self,events):
        self.tree.DeleteChildren(self.root)
        na_file = open('object', 'r')
        list = pickle.load(na_file)
        list.reverse()
        for i in list:
            if list[0][0]['label']==u'Документ':
                continue
            else:
                newitems = self.tree.InsertItemsFromList(i,self.root)
                for item in newitems:
                    self.tree.SelectItem(item)

    def AllItems(self,root):
        '''
        Обход подереву вызов скриптов шаблонов, выозвращает код tex
        '''
        item, cookie = self.tree.GetFirstChild(root)
        S=""
        while item.IsOk():
            i=self.tree.GetPyData(item)
            if i.render_header()==0:
                pass
            else:
                S+=i.render_header()
            if i.render_content()==0:
                pass
            else:
                S+=i.render_content()

            if self.tree.ItemHasChildren(item):
                match = self.AllItems(item)
                S+=match
            if i.render_footer()==0:
                pass
            else:
                S+=i.render_footer()
            item, cookie = self.tree.GetNextChild(self.root, cookie)
        return S

    def Renderrrr(self,event):
        #print self.AllItems(self.root)
        #self.render_tex()

        import sys

        f=open('texcode.tex','w')
        sys.stdout=f

        import codecs
        sys.stdout = codecs.getwriter('utf8')(sys.stdout)
        print self.AllItems(self.root)
        f.close()



        self.tabOne.open()

    def MyDoc(self,tree,root,):
        item, cookie = self.tree.GetFirstChild(root)
        list=[]
        while item.IsOk():
            #path=self.tree.GetItemText(root)+'#'+self.tree.GetItemText(item)
            #print self.tree.GetPyData(item)['Device']['name']
            list.append(item)
            #if self.tree.ItemHasChildren(item):
            #    match = self.MyDoc(self.tree,item)
            item, cookie = self.tree.GetNextChild(self.root, cookie)
        return list

if __name__=="__main__":
    hhh()

