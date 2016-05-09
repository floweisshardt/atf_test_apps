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
        self.testblock_circle = RecordingManager('testblock_circle')
        self.testblock_quadrat = RecordingManager('testblock_quadrat')
        self.testblock_all = RecordingManager('testblock_all')
        self.ptf = PublishTf()

    def execute(self):
        rospy.loginfo("app start")
        print "app start"
        # Example for recorder usage
        self.testblock_circle.start()
        self.testblock_all.start()
        self.ptf.pub_circ(radius=1, time=5)
        self.testblock_circle.stop()
        self.testblock_quadrat.start()
        self.ptf.pub_quadrat(length=2, time=10)
        self.testblock_quadrat.stop()
        self.testblock_all.stop()
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
