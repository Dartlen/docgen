# -*- coding: utf-8 -*-
import logging
import os
import codecs

from engine.idevice import Idevice


log = logging.getLogger(__name__)

# ===========================================================================

class TextIdevice(Idevice):
    """
    This is an example of a user created iDevice plugin.  If it is copied
    into the user's ~/.exe/idevices dircectory it will be loaded along with
    the system idevices.
    """
    def __init__(self):
         self.name="latex_figure"
         Idevice.__init__(self)
         self.caption=''
    def render_header(self):
        return u'\\begin{figure}[h]'

    def render_content(self):
        S=u""
        S+=self.propertylist[0][0]+u'\n'
        S+=self.propertylist[3][0]+self.propertylist[3][2]+u"{"+self.content+u"}"+u"\n"
        S+=self.propertylist[1][0]+self.propertylist[1][2]+u'\n'
        S+=self.propertylist[2][0]+self.propertylist[2][2]+u'\n'
        return S

def render_footer(self):
        return u'\end{figure}'
    

# ===========================================================================
def register(ideviceStore):
    """Register with the ideviceStore"""
    ideviceStore.append(TextIdevice())

    
# ===========================================================================
