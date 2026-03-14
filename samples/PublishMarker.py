#!/usr/bin/env python3 


from math import pi, sin, cos
from numpy import array
from numpy.linalg import norm

import rclpy
from rclpy.node import Node
from std_msgs.msg import Header
from marker_msgs.msg import MarkerStamped, Marker


    
class publish_marker(Node):
    def __init__(self):
        super().__init__('publish_marker_sample')
        self.__pub = self.create_publisher(
            MarkerStamped, 'marker', 10)
        self.__timer = self.create_timer(0.1, self.pub_sample)
        self.__counter = 0
        self.__header = Header()


    def pub_sample(self):
        while self.__pub.get_subscription_count() == 0:
            return
        self.__header.stamp = self.get_clock().now().to_msg()
        self.__header.frame_id = 'map'

        # Reset counter and indices if counter is a multiple of 30
        if self.__counter % 100 == 0:
            self.__counter = 0

        # Create a single message
        msg = MarkerStamped()
        msg.marker.ids.append(12)
        msg.marker.ids_confidence.append(0.99)
        msg.marker.pose.position.x = 2.
        msg.marker.pose.position.y = 0. + self.__counter * 0.01
        msg.marker.pose.position.z = 0.
        msg.marker.pose.orientation.x = 0.
        msg.marker.pose.orientation.y = 0.
        msg.marker.pose.orientation.z = 0.
        msg.marker.pose.orientation.w = 1.

        msg.header = self.__header
        self.__pub.publish(msg)
        self.__counter = self.__counter + 1


def main(args=None):
    rclpy.init(args=args)
    node = publish_marker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
