#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def callback(meassage):
    rospy.loginfo(f"{meassage}")

def listener():
    # initializing the subscriber
    rospy.init_node('speed_subscriber', anonymous=True)
    # defining the subscriber topic
    rospy.Subscriber("/turtle1/cmd_vel", Twist, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

