from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    params_file = (
        '/home/atharv/assignment_ws/src/level01_ros_assignment/'
        'testbed_navigation/config/amcl_params.yaml'
    )

    return LaunchDescription([

        Node(
            package='nav2_amcl',
            executable='amcl',
            name='amcl',
            output='screen',
            parameters=[
                params_file,
                {'use_sim_time': True},
            ],
        ),

        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager_localization',
            output='screen',
            parameters=[
                {'use_sim_time': True},
                {'autostart': True},
                {'node_names': ['amcl']},
            ],
        ),
    ])
