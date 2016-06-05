#!/usr/bin/python
import unittest
import rospy
import rostest
from atf_core import ATF
from atf_test_tools import PublishTf

class Application:
    def __init__(self):
        self.atf = ATF()
        self.atf.add_testblock('testblock_circle')
        self.atf.add_testblock('testblock_quadrat')
        self.atf.add_testblock('testblock_all')
        self.ptf = PublishTf()

    def execute(self):
        self.atf.start()

        self.atf.testblocks["testblock_all"].start()

        # circle
        self.atf.testblocks["testblock_circle"].start()
        self.ptf.pub_circ(radius=1, time=5)
        self.atf.testblocks["testblock_circle"].stop()

        # quadrat
        self.atf.testblocks["testblock_quadrat"].start()
        self.ptf.pub_quadrat(length=2, time=10)
        self.atf.testblocks["testblock_quadrat"].stop()

        self.atf.testblocks["testblock_all"].stop()

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
