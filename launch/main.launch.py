from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition

def generate_launch_description():

    use_pub1_config = LaunchConfiguration('use_pub1', default=True)
    use_pub2_config = LaunchConfiguration('use_pub2', default=True)

    return LaunchDescription([
        Node(
            package='arguments',
            executable='pub',
            name='pub1',
            parameters=[
                {'num': 600},
                {'timer_delay': 2}
            ],
            remappings=[
                ('/pub_topic', '/pub1_topic')
            ],
            condition=IfCondition(use_pub1_config)
        ),
        Node(
            package='arguments',
            executable='pub',
            name='pub2',
            parameters=[
                {'num': 30},
                {'timer_delay': 0.5}
            ],
            remappings=[
                ('/pub_topic', '/pub2_topic')
            ],
            condition=IfCondition(use_pub2_config)
        )
    ])
