#!/usr/bin/python
import rospy

from atf_core.atf import ATF

class Application:
    def __init__(self):
        self.atf = ATF()

    def execute(self):

        self.atf.start("testblock_3s")
        self.atf.start("testblock_1s")

        rospy.sleep(1)

        self.atf.stop("testblock_1s")
        self.atf.start("testblock_2s")

        rospy.sleep(2)

        self.atf.stop("testblock_2s")
        self.atf.stop("testblock_3s")

        # shutdown atf
        self.atf.shutdown()

if __name__ == '__main__':
    rospy.init_node('test_app')
    app = Application()
    app.execute()
