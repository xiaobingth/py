from uiautomator import device as d
import unittest
class firt(unittest.TestCase):
    def setUp(self):
        pass;
    def tearDown(self):
        pass;
    def test_opencamera(self):
        if(d.screen=="off"):
            d.wakeup()
        d(text ="Camera").click()
        d.press("back")
if __name__=="__main__":
    testUnit = unittest.TestSuite()
    testUnit.addTest(firt("test_opencamera"))
    runner = unittest.TextTestRunner()
    runner .run(testUnit)