from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='zbar_ros',
            namespace='',
            executable='barcode_reader',
            name='qr_code_reader',
            output="screen",
            emulate_tty=True,
            parameters=[
                {
                }
            ],
            remappings=[
                ('image', 'image_raw'),
                ('barcode', 'qr_codes')
            ],
            arguments=['--ros-args', '--log-level', 'info']
        ),
        Node(
            package='francor_rmrc_qr',
            namespace='',
            executable='qr_log',
            name='qr_log',
            output="screen",
            emulate_tty=True,
            parameters=[
                {
                }
            ],
            arguments=['--ros-args', '--log-level', 'info']
        ),
    ])
