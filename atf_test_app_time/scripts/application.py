#!/usr/bin/python
import unittest
import rospy
import rostest
from atf_core import ATF

class Application:
    def __init__(self):
        self.atf = ATF()
        self.atf.add_testblock('testblock_3s')
        self.atf.add_testblock('testblock_5s')
        self.atf.add_testblock('testblock_8s')

    def execute(self):
        self.atf.start()

        self.atf.testblocks["testblock_8s"].start()
        self.atf.testblocks["testblock_3s"].start()

        rospy.sleep(3)

        self.atf.testblocks["testblock_3s"].stop()
        self.atf.testblocks["testblock_5s"].start()

        rospy.sleep(5)

        self.atf.testblocks["testblock_5s"].stop()
        self.atf.testblocks["testblock_8s"].stop()

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
