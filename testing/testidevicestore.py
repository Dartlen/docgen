# -*- coding: utf-8 -*-
from docgen.engine.idevice      import Idevice
from docgen.engine.idevicestore import IdeviceStore
import unittest
import os


# ===========================================================================

class TestIdeviceStore(unittest.TestCase):

    def testLoad(self):
        """
        Tests that idevices can be loaded
        """
        store = IdeviceStore()
        store.loadDevices()
    def testTree(self):
        store = IdeviceStore()
        store.loadDevices()

        store.add_idevice(store.idevices[2])

        for i in store.idevices:

            if i.name=='latex_itemize':
                store.add_idevice(i)
                i.content='fsafsa\nfsafsafa\ndfasfsafsa'
            if i.name=='latex_text':
                store.add_idevice(i)
                i.content='prosto text'
            if i.name=='latex_subsection':
                store.add_idevice(i)
                i.content='SUBSECT'
            if i.name=='latex_section':
                store.add_idevice(i)
                i.content=unicode('русские буквы', 'utf-8')
            if i.name=='latex_newpage':
                store.add_idevice(i)
                pass
            if i.name=='latex_figure':

                #store.add_idevice(i)
                i.content="2.jpg"
                S=""
                S+=i.propertylist[0][0]+'\n'
                S+=i.propertylist[3][0]+i.propertylist[3][2]+"{"+i.content+"}"+"\n"
                S+=i.propertylist[1][0]+i.propertylist[1][2]+'\n'
                S+=i.propertylist[2][0]+i.propertylist[2][2]+'\n'
                #print S
            if i.name=='latex_table':
                i.propertylist[0][2]="{|p{11cm}|p{5cm}|p{6cm}}"
                store.add_idevice(i)
                i.content=[["1","2","3"],["11","22","33"],["111","222","333"]]

        store.add_idevice(store.idevices[1])

        store.render_tex()

        #self.assertEquals(store.addIdevice(store.idevices[0]),store.idevices[0])
        #self.assertEquals(store.set_select_item(store.idevices[1]),store.idevices[1])
        #self.assertEquals(store.get_select_item(),store.idevices[1])

        #self.assertEquals(store.render(store.root),'')



if __name__ == "__main__":
    unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestIdeviceStore))
    unittest.TextTestRunner(verbosity=2).run(suite)
