#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move():
    # initializing the publisher
    rospy.init_node('speed_publisher', anonymous=True)
    # defining the publisher topic
    speed_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(1)  # 1 Hz
    while not rospy.is_shutdown():
        # message = "Hello, ROS!"
        # speed_pub.publish(message)
        # rate.sleep()
        twist = Twist()
        twist.linear.x = -0.1
        twist.linear.y = -0.1

        twist.angular.x = 0.1
        twist.angular.y = 0.1

        speed_pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    move()