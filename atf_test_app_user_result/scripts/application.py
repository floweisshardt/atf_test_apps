#!/usr/bin/python
import unittest
import rospy
import rostest
import sys

import atf_core

class Application:
    def __init__(self):
        self.atf = atf_core.ATF()

    def execute(self):

        self.atf.start("testblock_8s")
        self.atf.start("testblock_3s")

        rospy.sleep(3)

        details = []
        self.atf.set_user_result("testblock_3s", 0.8, details)

        self.atf.stop("testblock_3s")
        self.atf.start("testblock_5s")

        rospy.sleep(5)

        details = []
        self.atf.set_user_result("testblock_5s", 0.8, details)
        self.atf.set_user_result("testblock_8s", 0.8, details)

        self.atf.stop("testblock_5s")
        self.atf.stop("testblock_8s")

        self.atf.shutdown()

if __name__ == '__main__':
    rospy.init_node('test_app')
    app = Application()
    app.execute()