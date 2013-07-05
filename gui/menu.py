#-*- coding:utf-8 -*-
import wx
class ContextMenuTree(object):
    """

    """
    def __init__(self):
        super(ContextMenuTree, self).__init__()
        self._menusecond = None
        self._menufirst = None
        self.tree2=None
        self.tree = None

    def OnContextMenu(self, event):
        if self.tree2==event.GetEventObject():
            self._menusecond = wx.Menu()
            self.CreateContextMenuSecond(self._menusecond)
            self.PopupMenu(self._menusecond)
        else:
            if self.tree==event.GetEventObject():
                self._menufirst = wx.Menu()
                self.CreateContextMenuFirst(self._menufirst)
                self.PopupMenu(self._menufirst)

    def CreateContextMenuSecond(self, menu):
        self._menusecond.Append(wx.ID_ADD)

    def CreateContextMenuFirst(self,menu):
        self._menufirst.Append(wx.ID_DELETE)