#!/usr/bin/python
import unittest
import rospy
import rostest
import sys

import atf_core
from atf_msgs.msg import MetricResult, Groundtruth

class Application:
    def __init__(self):
        self.atf = atf_core.ATF()

    def execute(self):

        self.atf.start("testblock_8s")
        self.atf.start("testblock_3s")

        rospy.sleep(3)

        # user result
        metric_result = MetricResult()
        metric_result.data.data = 0.83
        metric_result.groundtruth.result = Groundtruth.SUCCEEDED
        metric_result.groundtruth.error_message = "all ok in application of atf_test"
        self.atf.stop("testblock_3s", metric_result) # user result with groundtruth result
        self.atf.start("testblock_5s")

        rospy.sleep(5)

        # user result
        metric_result = MetricResult()
        metric_result.data.data = 0.85
        self.atf.stop("testblock_5s", metric_result) # user result without groundtruth result

        metric_result = MetricResult()
        metric_result.groundtruth.result = Groundtruth.SUCCEEDED
        self.atf.stop("testblock_8s", metric_result) # empty but successfull user result

        # shutdown atf
        self.atf.shutdown()

if __name__ == '__main__':
    rospy.init_node('test_app')
    app = Application()
    app.execute()
