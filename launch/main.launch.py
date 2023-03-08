from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition
from ament_index_python.packages import get_package_share_directory 
import os

def generate_launch_description():

    use_pub1_config = LaunchConfiguration('use_pub1', default=True)
    use_pub2_config = LaunchConfiguration('use_pub2', default=True)

    pkg_share = get_package_share_directory('arguments')

    pub_config_file = os.path.join(pkg_share, 'config', 'pub.yaml')

    return LaunchDescription([
        Node(
            package='arguments',
            executable='pub',
            name='pub1',
            parameters=[
                pub_config_file
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
                pub_config_file
            ],
            remappings=[
                ('/pub_topic', '/pub2_topic')
            ],
            condition=IfCondition(use_pub2_config)
        )
    ])
