#!/usr/bin/python
import unittest
import rospy
import rostest
import sys

from atf_core import ATF


class Application:
    def __init__(self):
        self.atf = ATF()

    def execute(self):

        #self.atf.start("testblock_8s")
        self.atf.start("testblock_3s")

        rospy.sleep(3)

        self.atf.stop("testblock_3s")
        self.atf.start("testblock_5s")

        rospy.sleep(5)

        self.atf.stop("testblock_5s")
        #self.atf.stop("testblock_8s")

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
