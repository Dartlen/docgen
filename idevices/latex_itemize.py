# ===========================================================================
# eXe 
# Copyright 2004-2005, University of Auckland
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
# ===========================================================================

"""
This is an example of a user created iDevice plugin.  If it is copied
into the user's ~/.exe/idevices dircectory it will be loaded along with
the system idevices.
"""
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
         self.name="latex_itemize"
         Idevice.__init__(self)

    def render_header(self):
        return '''\\begin{itemize}'''

    def render_content(self):
        if self.content==u'':
            return u''
        else:
            L=self.content.split('\n')
            S=u"\n"
            for i in L:
                S+='\item '+i+'\n'
            return S

    def render_footer(self):
        return '''\end{itemize}'''

# ===========================================================================
def register(ideviceStore):
    """Register with the ideviceStore"""
    ideviceStore.append(TextIdevice())

    
# ===========================================================================
