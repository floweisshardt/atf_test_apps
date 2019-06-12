#!/usr/bin/python
import unittest
import rospy
import rostest
import sys

import atf_core

class Application:
    def __init__(self):
        self.atf = atf_core.ATF()
        rospy.sleep(3)

    def execute(self):

        self.atf.start("testblock_1")
        rospy.sleep(1)
        self.atf.stop("testblock_1")

        self.atf.start("testblock_2")
        rospy.sleep(1)
        self.atf.stop("testblock_2")

        #self.atf.shutdown()

if __name__ == '__main__':
    rospy.init_node('test_app')
    app = Application()
    app.execute()