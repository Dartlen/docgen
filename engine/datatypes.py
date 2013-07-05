# -*- coding: utf-8 -*-
"""
Простые типы данных которые могут использоваться в iDevice дл хранения контента.
"""

import logging


log = logging.getLogger(__name__)


# ===========================================================================
class DType:
    """
    Поле. абстрактный класс. использовать его потомков
    """
    # Class attributes
    nextId = 1

    def __init__(self, name, instruc):
        """        
        """
        self._name     = name
        self._instruc  = instruc
        self._id       = DType.nextId
        DType.nextId  += 1
        self.idevice   = None

    # Properties
    name    = 'name'
    instruc = 'instruc'

    def getId(self):
        """
        """
        if self.idevice:
            fieldId = self.idevice.id + "_"
        else:
            fieldId = ""
        fieldId += unicode(self._id)
        return fieldId
    id = property(getId)


# ===========================================================================
class TextDType(DType):
    """
    Текстовое поле - одна строка
    """
    def __init__(self, name, instruc, content):
        """        
        """
        DType.__init__(self, name, instruc)
        self.content = content
        self.name    = name
        self.instruc = instruc

# ===========================================================================
class TextMultilineDType(DType):
    """
    Многострочный текст
    """
    def __init__(self, name, instruc, content):
        """

        """
        DType.__init__(self, name, instruc)
        self.content = content
        self.name    = name
        self.instruc = instruc


# ===========================================================================

class FileDType(DType):
    """
    Ресурс внешнего файла
    """
    def __init__(self, name, instruc,content):
        """
        """
        DType.__init__(self, name, instruc)
        self.FileResource   = None
        self.content = content
        self.name    = name
        self.instruc = instruc
        self.imageResource = ''

    def setFile(self, filePath):
        """
        Сохраняет файл в пакете
        """
        log.debug(u"setFile "+unicode(filePath))
        resourceFile = Path(filePath)

        assert(self.idevice.parentNode,
               'File '+self.idevice.id+' has no parentNode')
        assert(self.idevice.parentNode.package,
               'iDevice '+self.idevice.parentNode.id+' has no package')

        if resourceFile.isfile():
            if self.FileResource:
                self.FileResource.delete()
                self.idevice.userResources.remove(self.FileResource)
            self.FileResource = Resource(self.idevice.parentNode.package,
                                          resourceFile)
            self.idevice.FileResource.append(self.imageResource)

        else:
            log.error('File %s is not a file' % resourceFile)
   
  