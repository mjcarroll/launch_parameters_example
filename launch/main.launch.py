from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    arg_name = LaunchConfiguration('arg_name')

    name_launch_arg = DeclareLaunchArgument(
        'arg_name',
        default_value='foobar'
    )

    node = Node(
        package='py_launch_example',
        namespace='xxx',
        executable='main_node',
        name='main',
        parameters=[{
            'arg_name': LaunchConfiguration('arg_name')
        }]
    )

    return LaunchDescription([
        name_launch_arg,
        node,
    ])
