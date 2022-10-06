#!/usr/bin/env python3

import os

from launch import LaunchDescription
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
                package="image_tools", 
                executable="cam2image", 
                namespace="left", 
                name="cam", 
                arguments = [
                    "--out", "in", 
                    "--cam", "/dev/videoL",
                    "--width", width, 
                    "--height", height,
                    "--out-width", out_width,
                    "--out-height", out_height,
                    ]
                ),
            Node(
                package="image_tools", 
                executable="cam2image", 
                namespace="right", 
                name="cam", 
                arguments = [
                    "--out", "in", 
                    "--cam", "/dev/videoR",
                    "--width", width, 
                    "--height", height,
                    "--out-width", out_width,
                    "--out-height", out_height,
                    ]
                ),
            Node(
                package="image_tools", 
                executable="cam2image", 
                namespace="front", 
                name="cam", 
                arguments = [
                    "--out", "in", 
                    "--cam", "/dev/videoF",
                    "--width", width, 
                    "--height", height,
                    "--out-width", out_width,
                    "--out-height", out_height,
                    ]
                ),
            Node(
                package="image_tools", 
                executable="cam2image", 
                namespace="back", 
                name="cam", 
                arguments = ["--out", "in", 
                    "--cam", "/dev/videoB",
                    "--width", width, 
                    "--height", height,
                    "--out-width", out_width,
                    "--out-height", out_height,
                    ]
                ),
            Node(
                package='image_transport', 
                executable='republish', 
                output='screen', 
                name='republish', 
                arguments=["raw"],
                namespace='left',
                # remappings=[
                    # ('left/in', 'left'),
                    # ('out', 'left_compressed') 
                # ], 
            ),
            Node(
                package='image_transport', 
                executable='republish', 
                output='screen', 
                name='republish', 
                arguments=["raw"],
                namespace='right',
                # remappings=[
                    # ('right/in', 'right'),
                    # ('out', 'right_compressed') 
                # ], 
            ), 
            Node(
                package='image_transport', 
                executable='republish', 
                output='screen', 
                name='republish', 
                arguments=["raw"],
                namespace='front',
                # remappings=[
                    # ('front/in', 'front'),
                    # ('out', 'right_compressed') 
                # ], 
            ), 
            Node(
                package='image_transport', 
                executable='republish', 
                output='screen', 
                name='republish', 
                arguments=["raw"],
                namespace='back',
                # remappings=[
                    # ('back/in', 'back'),
                    # ('out', 'right_compressed') 
                # ], 
            ),
        ]
    )
