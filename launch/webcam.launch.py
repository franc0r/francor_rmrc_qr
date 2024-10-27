from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='v4l2_camera',
            namespace='',
            executable='v4l2_camera_node',
            name='v4l2_camera_node',
            output="screen",
            emulate_tty=True,
            parameters=[
                {
                    'video_device': '/dev/video0'
                }
            ],
            remappings=[
                ('image', 'image_raw'),
            ],
            arguments=['--ros-args', '--log-level', 'info']
        )
    ])
