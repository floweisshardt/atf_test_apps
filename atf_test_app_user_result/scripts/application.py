#!/usr/bin/python
import unittest
import rospy
import rostest
import sys

import atf_core
from atf_msgs.msg import MetricResult

class Application:
    def __init__(self):
        self.atf = atf_core.ATF()

    def execute(self):

        self.atf.start("testblock_8s")
        self.atf.start("testblock_3s")

        rospy.sleep(3)

        # user result
        metric_result = MetricResult()
        metric_result.data.data = 0.8
        metric_result.groundtruth.result = True
        metric_result.groundtruth.error_message = "all ok in application of atf_test"
        self.atf.stop("testblock_3s", metric_result) # user result with groundtruth result
        self.atf.start("testblock_5s")

        rospy.sleep(5)

        # user result
        metric_result = MetricResult()
        metric_result.data.data = 0.7
        self.atf.stop("testblock_5s", metric_result) # user result without groundtruth result
        self.atf.stop("testblock_8s") # no user result

        # shutdown atf
        self.atf.shutdown()

if __name__ == '__main__':
    rospy.init_node('test_app')
    app = Application()
    app.execute()
