# -*- coding: utf-8 -*-
import logging
import os

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
         self.name="latex_table"
         Idevice.__init__(self)

    def render_header(self):
        return '\\begin {longtable}'+"\n"

    def render_content(self):
        hline="\hline\n"
        S=""
        S+=self.propertylist[0][2]+"\n"
        S+=self.propertylist[1][0]+self.propertylist[1][2]+"\n"
        S+=self.propertylist[2][0]+self.propertylist[2][2]+r"\\"+"\n"
        S+=hline
        for i in self.content[0]:
            S+=i+"&"
        S=S[:-1]
        S+=r"\\"+"\n"
        S+=hline
        S+="\endfirsthead\n"
        S+=self.propertylist[1][0]+"{Prodoljenie tablici \\ref%s}"%self.propertylist[2][2]+r"\\"+"\n"
        S+=hline
        count=0
        for i in self.content:
            for k in i:
                S+=k+"&"
            S=S[:-1]
            S+=r"\\"+"\n"
            if count==0:
                S+="\endhead"+"\n"
            else:
                S+=hline
            count+=1
        return S

    def render_footer(self):
        return '\end {longtable}'+"\n"
    

# ===========================================================================
def register(ideviceStore):
    """Register with the ideviceStore"""
    ideviceStore.append(TextIdevice())

    
# ===========================================================================
