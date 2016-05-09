#!/usr/bin/python
import unittest
import yaml
from subprocess import call

import rospy
import rostest
import rostopic
from atf_recorder import RecordingManager
from atf_test_tools import PublishTf
import sys

class Application:
    def __init__(self):
        self.testblock_1 = RecordingManager('testblock_1')
        self.testblock_2 = RecordingManager('testblock_2')
        self.testblock_3 = RecordingManager('testblock_3')
        self.ptf = PublishTf()

    def execute(self):
        rospy.loginfo("app start")
        print "app start"
        # Example for recorder usage
        self.testblock_1.start()
        self.testblock_3.start()
        self.ptf.pub_circ(radius=1, time=5)
        self.testblock_1.stop()
        self.testblock_2.start()
        self.ptf.pub_quadrat(length=2, time=10)
        self.testblock_2.stop()
        self.testblock_3.stop()
        rospy.loginfo("app end")

class Test(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def tearDown(self):
        pass

    def test_Recording(self):
        self.app.execute()

if __name__ == '__main__':
    rospy.init_node('test_name')
    rostest.rosrun('application', 'test_application', Test, sysargs=None)
