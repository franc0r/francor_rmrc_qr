from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='v4l2_camera',
            namespace='cam1',
            executable='v4l2_camera_node',
            name='v4l2_camera_node1',
            output="screen",
            emulate_tty=True,
            parameters=[
                {
                    'video_device': '/dev/video0'
                }
            ],
            arguments=['--ros-args', '--log-level', 'info']
        )
        Node(
            package='v4l2_camera',
            namespace='cam2',
            executable='v4l2_camera_node',
            name='v4l2_camera_node2',
            output="screen",
            emulate_tty=True,
            parameters=[
                {
                    'video_device': '/dev/video2'
                }
            ],
            arguments=['--ros-args', '--log-level', 'info']
        )
    ])
