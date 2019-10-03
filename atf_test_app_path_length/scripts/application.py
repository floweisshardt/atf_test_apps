#!/usr/bin/python
import unittest
import rospy
import rostest
import sys

import atf_core
from atf_test_tools import PublishTf

class Application:
    def __init__(self):
        self.atf = atf_core.ATF()
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

        self.atf.stop("testblock_all")

        # shutdown atf
        self.atf.shutdown()

if __name__ == '__main__':
    rospy.init_node('test_app')
    app = Application()
    app.execute()
