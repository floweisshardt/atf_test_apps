#!/usr/bin/python
import rospy

from atf_core.atf import ATF
from atf_msgs.msg import MetricResult, Groundtruth

class Application:
    def __init__(self):
        self.atf = ATF()

    def execute(self):

        self.atf.start("testblock_3s")
        self.atf.start("testblock_1s")

        rospy.sleep(1)

        # user result
        metric_result = MetricResult()
        metric_result.data.data = 0.83
        metric_result.groundtruth.result = Groundtruth.SUCCEEDED
        metric_result.groundtruth.error_message = "all ok in application of atf_test"
        self.atf.stop("testblock_1s", metric_result) # user result with groundtruth result
        self.atf.start("testblock_2s")

        rospy.sleep(2)

        # user result
        metric_result = MetricResult()
        metric_result.data.data = 0.85
        self.atf.stop("testblock_2s", metric_result) # user result without groundtruth result

        metric_result = MetricResult()
        metric_result.groundtruth.result = Groundtruth.SUCCEEDED
        self.atf.stop("testblock_3s", metric_result) # empty but successfull user result

        # shutdown atf
        self.atf.shutdown()

if __name__ == '__main__':
    rospy.init_node('test_app')
    app = Application()
    app.execute()
