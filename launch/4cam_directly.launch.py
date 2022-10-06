#!/usr/bin/env python3

import os

from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.actions import ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node
'''
import argparse
parser = argparse.ArgumentParser()

parser.add_argument(
    "--width", 
    type=str, 
    required=False, 
    default="640"
)
parser.add_argument(
    "--height", 
    type=str, 
    required=False, 
    default="480"
)
args, unknown = parser.parse_known_args()
'''
left_param_path = os.path.join(get_package_share_directory("usb_camera_driver"), "config", "left_param.txt")
right_param_path = os.path.join(get_package_share_directory("usb_camera_driver"), "config", "right_param.txt")
front_param_path = os.path.join(get_package_share_directory("usb_camera_driver"), "config", "front_param.txt")
back_param_path = os.path.join(get_package_share_directory("usb_camera_driver"), "config", "back_param.txt")

width = "640"
height = "360"
out_width = "320"
out_height = "180"

# this is the function launch  system will look for
def generate_launch_description():

    # create and return launch description object
    return LaunchDescription(
        [
            Node(
                package="image_transport_tutorials", 
                executable="publisher_from_video", 
                namespace="left", 
                name="cam",
                arguments = [
                    "/dev/videoL",
                    left_param_path,
                    ]
                ),
            Node(
                package="image_transport_tutorials", 
                executable="publisher_from_video", 
                namespace="right", 
                name="cam", 
                arguments = [
                    "/dev/videoR",
                    right_param_path,
                    ]
                ),
            Node(
                package="image_transport_tutorials", 
                executable="publisher_from_video", 
                namespace="front", 
                name="cam", 
                arguments = [
                    "/dev/videoF",
                    front_param_path,
                    ]
                ),
            Node(
                package="image_transport_tutorials", 
                executable="publisher_from_video", 
                namespace="back", 
                name="cam", 
                arguments = [
                    "/dev/videoB",
                    back_param_path,
                    ]
                ),
        ]
    )
