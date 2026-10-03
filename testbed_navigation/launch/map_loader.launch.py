from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    map_file = (
        '/home/atharv/assignment_ws/src/level01_ros_assignment/'
        'testbed_bringup/maps/testbed_world.yaml'
    )

    return LaunchDescription([
        Node(
            package='nav2_map_server',
            executable='map_server',
            name='map_server',
            output='screen',
            parameters=[
                {'yaml_filename': map_file},
                {'use_sim_time': True},
            ],
        ),

        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager_map',
            output='screen',
            parameters=[
                {'use_sim_time': True},
                {'autostart': True},
                {'node_names': ['map_server']},
            ],
        ),
    ])
