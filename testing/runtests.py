#!/usr/bin/python

import unittest
from testidevice       import TestIdevice
from testidevicestore  import TestIdeviceStore



# ===========================================================================

if __name__ == "__main__":
    suite = unittest.TestSuite()
    #suite.addTest(unittest.makeSuite(TestIdevice))
    suite.addTest(unittest.makeSuite(TestIdeviceStore))
    unittest.TextTestRunner(verbosity=2).run(suite)
