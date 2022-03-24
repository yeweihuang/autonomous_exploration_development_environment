#!/usr/bin/env python
import pandas as pd
import rospy
import numpy as np
from geometry_msgs.msg import PointStamped
from plyfile import PlyData, PlyElement

global waypoint_list

def callback(data):
    pt = data.point
    waypoint_list.append((pt.x, pt.y, pt.z))
    waypoint_array = np.array(waypoint_list, dtype=[('x', 'f4'), ('y', 'f4'),('z', 'f4')])
    el = PlyElement.describe(waypoint_array, 'vertex')
    PlyData([el],text=True).write('waypoint.ply')
    rospy.loginfo(pt)


def listener():
    rospy.init_node('waypoint_listener', anonymous=True)
    rospy.Subscriber("way_point", PointStamped, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    waypoint_list = []
    listener()
