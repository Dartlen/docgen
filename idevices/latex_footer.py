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
         self.name="latex_footer"
         Idevice.__init__(self)

    def render_header(self):
        return "\end {document}"

    def render_content(self):
        return ""

    def render_footer(self):
        return ""
    

# ===========================================================================
def register(ideviceStore):
    """Register with the ideviceStore"""
    ideviceStore.append(TextIdevice())

    
# ===========================================================================
