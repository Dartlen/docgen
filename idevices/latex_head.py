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
         self.name="latex_head"
         Idevice.__init__(self)

    def render_header(self):
        return """\documentclass [russian,utf8,floatsection,equationsection] {eskdtext}\n

\usepackage[titles]{tocloft}\n

\ESKDsectStyle{section}{\\bfseries}\n
\ESKDsectStyle{subsection}{\\bfseries}\n
\ESKDsectStyle{subsubsection}{\\bfseries}\n

\usepackage{longtable}\n
\usepackage{mathtext}\n
\usepackage[T2A]{fontenc}\n

\RequirePackage{amsmath}\n
\RequirePackage{zref-perpage}\n
\DeclareSymbolFont{T2Aletters}{T2A}{cmr}{m}{it}\n

\usepackage{graphicx}\n
\usepackage{multirow}\n"""

    def render_content(self):

        S=""
        for i in self.propertylist:
            S+=i[0]+i[2]

        return S

    def render_footer(self):
        return """
\usepackage{floatrow}
\usepackage{array,fr-longtable}
\\floatsetup[longtable]{LTcapwidth=table,margins=centering}
\\renewcommand\cftsecfont{\\normalfont}
\\renewcommand{\cftsecpagefont}{\\normalfont}
\zmakeperpage{footnote}
\let\\footnotesize\small
\\renewcommand{\\thefootnote}{\\arabic{footnote})}
\\begin {document}
\maketitle
\setcounter{page}{5}
\\tableofcontents
            """
    

# ===========================================================================
def register(ideviceStore):
    """Register with the ideviceStore"""
    ideviceStore.append(TextIdevice())

    
# ===========================================================================
