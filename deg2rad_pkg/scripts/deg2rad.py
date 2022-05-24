#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
import math

def convert_deg(msg):
    radians = (rospy.get_param("/degrees")) * ((math.pi) / (180))
    rospy.loginfo(f"{msg} -> {radians}")

if __name__ == '__main__':
    rospy.init_node('deg2rad')
    sub = rospy.Subscriber("/get_deg", Float32, convert_deg)
    rospy.spin()
