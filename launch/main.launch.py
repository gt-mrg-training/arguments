from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(
            package='arguments',
            executable='pub',
            name='pub1',
            parameters=[
                {'num': 600}
            ],
            remappings=[
                ('/pub_topic', '/pub1_topic')
            ]
        ),
        Node(
            package='arguments',
            executable='pub',
            name='pub2',
            parameters=[
                {'num': 30}
            ],
            remappings=[
                ('/pub_topic', '/pub2_topic')
            ]
        )
    ])
