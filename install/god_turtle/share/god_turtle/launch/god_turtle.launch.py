from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    
    teleop_turtle_name = 'sang'
    launch_description = LaunchDescription()
    
    turtle_node = Node(
        package='turtlesim_plus',
        namespace='',
        executable='turtlesim_plus_node.py',
        name='turtle_node'
    )
    launch_description.add_action(turtle_node)
    
    kill_turtle = ExecuteProcess(
        cmd = ["ros2 service call /remove_turtle turtlesim/srv/Kill \"name: 'turtle1'\""],
        shell = True
    )
    launch_description.add_action(kill_turtle)
    
    spawn_turtle = ExecuteProcess(
        cmd = [
            f"ros2 service call /spawn_turtle turtlesim/srv/Spawn \"{{x: -1.0, y: -1.0, theta: 0.0, name: '{teleop_turtle_name}'}}\""
        ],
        shell = True
    )
    launch_description.add_action(spawn_turtle)
    
    return launch_description