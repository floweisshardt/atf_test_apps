#!/usr/bin/python
import unittest
import rospy
import rostest
from atf_core import ATF

class Application:
    def __init__(self):
        self.atf = ATF()
        self.atf.add_testblock('testblock_1')
        self.atf.add_testblock('testblock_2')

    def execute(self):
        self.atf.start()

        self.atf.testblocks["testblock_1"].start()
        rospy.sleep(1)
        self.atf.testblocks["testblock_1"].stop()

        self.atf.testblocks["testblock_2"].start()
        rospy.sleep(1)
        self.atf.testblocks["testblock_2"].stop()

        self.atf.stop()

class Test(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def tearDown(self):
        pass

    def test_Recording(self):
        self.app.execute()

if __name__ == '__main__':
    rospy.init_node('test_name')
    #app = Application()
    #app.execute()
    rostest.rosrun('application', 'recording', Test, sysargs=None)
