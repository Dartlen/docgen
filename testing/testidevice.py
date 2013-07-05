
import unittest

from docgen.engine.idevice import Idevice



class TestIdevice(unittest.TestCase):
    def setUp(self):
        #self.packageStore = PackageStore()
        #self.package      = self.packageStore.createPackage()
        pass
    def testIdevice(self):
        '''
        name,short_name,description,presence_content,
                 presence_couple,param_count,param_container,typecontent,dictinarywithproperty
        '''
        myIdevice = Idevice()

       # self.assertEquals(myIdevice.description, "description")
       # self.assertEquals(myIdevice.name, "name")
       # self.assertEquals(myIdevice.short_name,"short_name")
       # self.assertEquals(myIdevice.presence_content,True)
       # self.assertEquals(myIdevice.presence_couple,True)
       # self.assertEquals(myIdevice.param_count,"param_count")
       # self.assertEquals(myIdevice.param_container,True)
       # self.assertEquals(myIdevice.typecontent,"typecontent")


        
    def SetParentNode(self):
        parentNode = Node(self.package)
        idevice0 = Idevice("FirstIdevice", "", "", "", "")
        idevice0.setParentNode(parentNode)
        self.assert_(idevice0.parentNode is parentNode)
        
    def IsfirstAndIsLast(self):
        parentNode = Node(self.package)
        idevice0 = Idevice("FirstIdevice", "", "", "", "")
        idevice0.setParentNode(parentNode)
        idevice1 = Idevice("SecondIdevice", "", "", "", "")
        idevice1.setParentNode(parentNode)
        idevice2 = Idevice("ThirdIdevice", "", "", "", "")
        idevice2.setParentNode(parentNode)
        
        self.assert_(idevice0.isFirst)
        self.assert_(idevice2.isLast)
        
        
    def Cmp(self):
        idevice0 = Idevice("FirstIdevice", "", "", "", "")
        idevice1 = Idevice("SecondIdevice", "", "", "", "")
        idevice2 = Idevice("ThirdIdevice", "", "", "", "")
        self.assertEquals(idevice2.__cmp__(idevice1), 1)
        self.assertEquals(idevice1.__cmp__(idevice0), 1)
        self.assertEquals(idevice0.__cmp__(idevice2), -1)
        
    def Delete(self):
        parentNode = Node(self.package)
        idevice0 = Idevice("FirstIdevice", "", "", "", "")
        idevice0.setParentNode(parentNode)
        idevice1 = Idevice("SecondIdevice", "", "", "", "")
        idevice1.setParentNode(parentNode)
        idevice2 = Idevice("ThirdIdevice", "", "", "", "")
        idevice2.setParentNode(parentNode)
        idevice1.delete()
        if idevice1 in parentNode.idevices:
            print "delete failed"
    
    def Move(self):
        parentNode = Node(self.package)
        idevice0 = Idevice("FirstIdevice", "", "", "", "")
        idevice0.setParentNode(parentNode)
        idevice1 = Idevice("SecondIdevice", "", "", "", "")
        idevice1.setParentNode(parentNode)
        idevice2 = Idevice("ThirdIdevice", "", "", "", "")
        idevice2.setParentNode(parentNode)
        
        idevice0.moveNext()
        self.assertEquals(parentNode.idevices[1], idevice0)
        self.assertEquals(parentNode.idevices[0], idevice1)
        
        idevice2.movePrev()
        self.assertEquals(parentNode.idevices[1], idevice2)
        self.assertEquals(parentNode.idevices[2], idevice0)
        
if __name__ == "__main__":
    unittest.main()
