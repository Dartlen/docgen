# -*- coding: utf-8 -*-
"""
Базовый класс для iDevices
"""

import logging
from engine.datatypes import TextMultilineDType,TextDType,FileDType
import xml.etree.ElementTree as etree


log = logging.getLogger(__name__)

# ===========================================================================
class Idevice:
    """    
    Базовый класс для всех Devices
    На базе его создаеются потомки, с помощью которого создается итоговый документ    
    """

    # Class attributes
    # see derieved classes for persistenceVersion 
    nextId = 1
    NoEmphasis, SomeEmphasis, StrongEmphasis = range(3)

    def __init__ (self):

        log.debug("Creating iDevice")
        
        #должен выпполнить загрузку параметров из файла 
        #self.name + ".xml"

        self.id          = unicode(Idevice.nextId)
        Idevice.nextId  += 1

        self.content=u""
        self.propertyStore = []
        self.userResources = []
        self.L             = []
        self.propertylist  = []
        self.parseproperty(self.name)

        self.__container()
        self.__content()
        self.__couple()

        if self.param_container:
            self.child = []
        else:
            self.child = None

    def additem(self,device):
        item=device
        self.child.append(item)
        return item

    def __content(self):
        if self.presence_content.lower()=='yes':
            self.presence_content=True
        else:
            self.presence_content=False

    def __container(self):
        if self.param_container.lower()=='yes':
            self.param_container=True
        else:
            self.param_container=False

    def __couple(self):
        if self.presence_couple.lower()=='yes':
            self.presence_couple=True
        else:
            self.presence_couple=False


    def render_header(self):
        return ''

    def render_content(self):
        return ''

    def render_footer(self):
        return ''

    def appendproperty(self,item):
        self.propertyStore.append(item)


    def setvaluedeviceproperty(self):
        self.ideviceproeprty=[]
        self.name               = self.L[1]
        self.short_name         = self.L[0]
        self.description        = self.L[2]
        self.presence_content   = self.L[3]
        self.presence_couple    = self.L[4]
        self.param_container    = self.L[5]
        self.type_device        = self.L[6]




    def parseproperty(self,name):
        """
        load property in list
        """
        l=[]
        path=__file__.split("\\")[:-2]
        newpath=""
        for i in path:
            newpath+=i+"\\"
        idevicesxml=etree.parse(newpath+'idevices\\'+name+".xml")
        filexml=idevicesxml.getroot()
        for child in filexml.iter('idevice'):
            for childchild in child:
                if childchild.tag=="params":
                    pass
                else:

                    self.L.append(childchild.text)

            for child in filexml.iter('param'):
                for childchild in child:

                    l.append(childchild.text)
                self.propertylist.append(l)
                l=[]
        self.setvaluedeviceproperty()
        return 0

    def prop(self):
        """
        create property object, append in idevice
        """
        for prop in self.propertylist:
            if prop[2]=='line':
                self.appendproperty(TextDType(prop[0],prop[1],prop[3]))
            elif prop[2]=='multiline':
                self.appendproperty(TextMultilineDType(prop[0],prop[1],prop[3]))
            elif prop[2]=='ref':
                self.appendproperty(FileDType(prop[0],prop[1],prop[3]))
        return self.propertylist

# ===========================================================================
