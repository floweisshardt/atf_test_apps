#!/usr/bin/python
import unittest
import rospy
import rostest
import sys

from atf_core import ATF
from atf_test_tools import PublishTf

class Application:
    def __init__(self):
        self.atf = ATF()
        self.ptf = PublishTf()

    def execute(self):

        self.atf.start("testblock_all")

        # circle
        self.atf.start("testblock_circle")
        self.ptf.pub_circ(radius=1, time=5)
        self.atf.stop("testblock_circle")

        # quadrat
        self.atf.start("testblock_quadrat")
        self.ptf.pub_quadrat(length=2, time=10)
        self.atf.stop("testblock_quadrat")

        self.atf.stop("testblock_all").stop()

        self.atf.shutdown()

class Test(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def tearDown(self):
        pass

    def test_Recording(self):
        self.app.execute()

if __name__ == '__main__':
    rospy.init_node('test_name')
    if "standalone" in sys.argv:
        app = Application()
        app.execute()
    else:
        rostest.rosrun('application', 'recording', Test, sysargs=None)
