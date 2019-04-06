#!/usr/bin/python
import unittest
import rospy
import rostest
import sys

#from atf_core import ATF
from atf_core.atf_controller import ATFController


class Application:
    def __init__(self):
        self.atf = ATFController()
        #TODO WAIT FOR ATF to be initialized inside ATFController 
        rospy.sleep(3)

    def execute(self):
        print "--- start ---"

        self.atf.start("testblock_8s")
        self.atf.start("testblock_3s")

        rospy.sleep(3)

        self.atf.stop("testblock_3s")
        self.atf.start("testblock_5s")

        rospy.sleep(5)

        self.atf.stop("testblock_5s")
        self.atf.stop("testblock_8s")
        print "--- end ---"

        #self.atf.shutdown()

if __name__ == '__main__':
    rospy.init_node('test_app')
    app = Application()
    app.execute()
