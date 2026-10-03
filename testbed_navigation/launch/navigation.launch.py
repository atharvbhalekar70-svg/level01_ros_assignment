from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    params_file = (
        '/home/atharv/assignment_ws/src/level01_ros_assignment/'
        'testbed_navigation/config/nav2_params.yaml'
    )

    return LaunchDescription([

        # Planner Server
        Node(
            package='nav2_planner',
            executable='planner_server',
            name='planner_server',
            output='screen',
            parameters=[
                params_file,
                {'use_sim_time': True},
            ],
        ),

        # Controller Server
        Node(
            package='nav2_controller',
            executable='controller_server',
            name='controller_server',
            output='screen',
            parameters=[
                params_file,
                {'use_sim_time': True},
            ],
        ),

        # Behavior Server
        Node(
            package='nav2_behaviors',
            executable='behavior_server',
            name='behavior_server',
            output='screen',
            parameters=[
                params_file,
                {'use_sim_time': True},
            ],
        ),

        # Behavior Tree Navigator
        Node(
            package='nav2_bt_navigator',
            executable='bt_navigator',
            name='bt_navigator',
            output='screen',
            parameters=[
                params_file,
                {'use_sim_time': True},
            ],
        ),

        # Velocity Smoother
        Node(
            package='nav2_velocity_smoother',
            executable='velocity_smoother',
            name='velocity_smoother',
            output='screen',
            parameters=[
                params_file,
                {'use_sim_time': True},
            ],
        ),

        # Lifecycle Manager
        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager_navigation',
            output='screen',
            parameters=[
                {'use_sim_time': True},
                {'autostart': True},
                {
                    'node_names': [
                        'planner_server',
                        'controller_server',
                        'behavior_server',
                        'bt_navigator',
                        'velocity_smoother',
                    ]
                },
            ],
        ),
    ])
