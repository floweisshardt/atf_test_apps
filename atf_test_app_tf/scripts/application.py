#!/usr/bin/python
import rospy

from atf_core.atf import ATF
from atf_test_tools.publish_tf import PublishTf

class Application:
    def __init__(self):
        self.atf = ATF()
        self.ptf = PublishTf()

    def execute(self):
        self.atf.start("testblock_all")

        # circle
        self.atf.start("testblock_circle")
        # FIXME: due to timing problem the first tf message is sometimes omitted
        #        so next line (pub_zero) is used as a workaround
        self.ptf.pub_zero(doSleep=True)
        self.ptf.pub_circ(radius=1, time=10)
        self.atf.stop("testblock_circle")

        # line
        self.atf.start("testblock_line")
        self.ptf.pub_line(length=2, time=5)
        self.atf.stop("testblock_line")

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
