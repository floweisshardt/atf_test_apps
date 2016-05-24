#!/usr/bin/python
import unittest
import rospy
import rostest
from atf_recorder import RecordingManager

class Application:
    def __init__(self):
        self.testblock_1 = RecordingManager('testblock_1')
        self.testblock_2 = RecordingManager('testblock_2')

    def execute(self):
        self.testblock_1.start()
        rospy.sleep(1)
        self.testblock_1.stop()
        self.testblock_2.start()
        rospy.sleep(1)
        self.testblock_2.stop()

class Test(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def tearDown(self):
        pass

    def test_Recording(self):
        self.app.execute()

if __name__ == '__main__':
    rospy.init_node('test_name')
    rostest.rosrun('application', 'recording', Test, sysargs=None)
