from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(
            package='arguments',
            executable='pub',
            parameters=[
                {'num': 600}
            ],
            remappings=[
                ('/pub_topic', '/remapped_topic')
            ]
        )
    ])
