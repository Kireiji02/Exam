import yaml
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def loadYAML():
    with open('/home/kireiji/Documents/GitHub/Exam/src/god_turtle/yaml_files/sang_via_point.yaml', 'r') as file:
        data = yaml.safe_load(file)
    return data

def get_turtle_positions(turtle_index):
    """
    Get positions for a specific turtle by its index.
    """
    turtle_positions = loadYAML()[turtle_index]
    x_positions = turtle_positions[0]
    y_positions = turtle_positions[1]
    return x_positions, y_positions

def generate_launch_description():
    
    teleop_namespace = 'teleop'
    teleop_turtle_name = 'sang'
    copy_namespace = 'copy_turtle'
    name_list = ['Foxy', 'Noetic', 'Humble', 'Iron']
    launch_description = LaunchDescription()
    
    scheduler_node = Node(
        package='god_turtle',
        namespace='',
        executable='scheduler.py',
        name='scheduler_node',
        parameters=[
                {'namespace_list':name_list}
            ]
    )
    launch_description.add_action(scheduler_node)
    
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
                {'pizza_limit':50},
                {'save_limit':4}
            ]
    )
    launch_description.add_action(controller_node)
    

    turtle_copy_node = Node(
        package='turtlesim_plus',
        namespace=copy_namespace,
        executable='turtlesim_plus_node.py',
        name='turtle_node'
    )
    launch_description.add_action(turtle_copy_node)
    
    kill_turtle_copy = ExecuteProcess(
        cmd = [f"ros2 service call /{copy_namespace}/remove_turtle turtlesim/srv/Kill \"name: 'turtle1'\""],
        shell = True
    )
    launch_description.add_action(kill_turtle_copy)

    for i in range(len(name_list)):
        spawn_turtle = ExecuteProcess(
            cmd = [
                f"ros2 service call /{copy_namespace}/spawn_turtle turtlesim/srv/Spawn \"{{x: -1.0, y: -1.0, theta: 0.0, name: '/{name_list[i]}'}}\""
            ],
            shell = True
        )
        launch_description.add_action(spawn_turtle)


    for i in range(len(name_list)):
        positions_x, positions_y = get_turtle_positions(i)
        copy_turtle_node = Node(
            package='god_turtle',
            namespace=name_list[i],
            executable='copy_turtle.py',  # No need for .py extension here
            name='copy_turtle',
            parameters=[
                {'x_positions': positions_x},
                {'y_positions': positions_y},
                {'get_namespace': copy_namespace}
            ]
        )
        launch_description.add_action(copy_turtle_node)
        
    
    return launch_description