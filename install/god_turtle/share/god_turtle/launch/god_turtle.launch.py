from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    
    teleop_namespace = 'teleop'
    teleop_turtle_name = 'sang'
    launch_description = LaunchDescription()
    
    turtle_node = Node(
        package='turtlesim_plus',
        namespace=teleop_namespace,
        executable='turtlesim_plus_node.py',
        name='turtle_node'
    )
    launch_description.add_action(turtle_node)
    
    kill_turtle = ExecuteProcess(
        cmd = [f"ros2 service call /{teleop_namespace}/remove_turtle turtlesim/srv/Kill \"name: 'turtle1'\""],
        shell = True
    )
    launch_description.add_action(kill_turtle)
    
    #-----------------------------------------------------------------------------------#
    
    spawn_turtle = ExecuteProcess(
        cmd = [
            f"ros2 service call /{teleop_namespace}/spawn_turtle turtlesim/srv/Spawn \"{{x: -1.0, y: -1.0, theta: 0.0, name: '/{teleop_turtle_name}'}}\""
        ],
        shell = True
    )
    launch_description.add_action(spawn_turtle)
    
    controller_node = Node(
        package='god_turtle',
        namespace=teleop_turtle_name,
        executable='controller.py',
        name='controller_node',
            parameters=[
                {'name':teleop_namespace},
                {'pizza_limit':50}
            ]
    )
    launch_description.add_action(controller_node)
    
    return launch_description