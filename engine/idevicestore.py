# -*- coding: utf-8 -*-
"""
Класс колелекции всех доступных iDevices
"""
#from docgen.engine.idevice import Idevice
import sys
import logging
import os
from copy import deepcopy
log = logging.getLogger(__name__)

# ===========================================================================
class IdeviceStore:
    """
    Коллекция доступных iDevices
    """
    def __init__(self):
        """
        """
        self._nextIdeviceId = 0
        self.selecttreeitem = None
#         self.extended       = []
#         self.generic        = []
        self.idevices  = []
        self.rootmytree = []

    def append(self,param):
        self.idevices.append(param)

    def getNewIdeviceId(self):
        """
        Возвращает уникальный iDevice Id 
        """
        id_ = unicode(self._nextIdeviceId)
        self._nextIdeviceId += 1
        return id_

    def allitemtree(self,root):
        '''
        Возвращает все элементы дерева в одном списке
        '''
        listitem=[]
        for i in root:
            listitem.append(i)
            if i.child!=None:
                l=self.allitemtree(i.child)
                for k in l:
                    listitem.append(k)
        return listitem

    def render(self,root):
        '''
        Итерирует дерево, вызывая функции генерации Idevice, возвращает строку
        '''
        S=''
        for i in root:
            #listitem.append(i)
            if i.render_header()==0:
                pass
            else:
                S+=i.render_header()
            if i.render_content()==0:
                pass
            else:
                S+=i.render_content()

            if i.child!=None:
                l=self.render(i.child)
                #for k in l:
                    #listitem.append(k)
                S+=l
            if i.render_footer()==0:
                pass
            else:
                S+=i.render_footer()
        return S

    def set_select_item(self,value):
        '''
        Принимает value,где value Idevice
        '''
        self.selecttreeitem=deepcopy(value)
        return value

    def get_select_item(self):
        return self.selecttreeitem

    item = property(get_select_item,set_select_item)

    def get_idevice(self):
        """
        Получает idevices из заданного пакета
        """
        return self.idevices

    def del_idevice(self, idevice):
        """
        Delete a generic idevice from idevicestore.
        """
        for i in self.idevices:
            if i==idevice:
                self.idevices.remove(i)

    def add_idevice(self, idevice):
        """
        Register another iDevice as available
        """
        item=idevice
        self.rootmytree.append(idevice)
        return item

    idevice = property(get_idevice,add_idevice,del_idevice)

    def loadDevices(self):
        """
        Load the user-created extended iDevices which are in the idevices
        directory
        """
        idevicePath = os.path.dirname(__file__)
        idevicePath=idevicePath[:(-1)*len(idevicePath.split('\\')[-1])]+'idevices'
        listdir = os.listdir(idevicePath)
        sys.path.insert(0,idevicePath)
        for s in listdir:
            if s[-3:]=='.py':
                module=__import__(os.path.splitext(s)[0], None, None, [''])
                try:
                    module.register(self)
                except AttributeError:
                    pass

    def render_tex(self):
        #print self.render(self.rootmytree)
        #f=open('texcode.tex','w')
        #sys.stdout=f

        #import codecs
        #sys.stdout = codecs.getwriter('utf8')(sys.stdout)
        print self.render(self.rootmytree)

        #f.close()

# ===========================================================================
