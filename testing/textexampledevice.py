import unittest
from exe.engine.node    import Node
from exe.idevices.exampleidevice import ExampleIdevice
from exe.engine.packagestore import PackageStore


class TestExampleIDevice(unittest.TestCase):

    def testIdevice(self):
        myIdevice = ExampleIdevice()

        #self.assertEquals(myIdevice.parseproperty(),0)
