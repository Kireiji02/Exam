from launch import LaunchDescription
from launch_ros.actions import Node
import yaml
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
    ns = 'copy_turtle'
    name_list = ['Foxy', 'Noetic', 'Humble', 'Iron']
    ld = LaunchDescription()

    turtle_node = Node(
        package='turtlesim_plus',
        namespace=ns,
        executable='turtlesim_plus_node.py',
        name='turtle_node'
    )
    ld.add_action(turtle_node)
    
    kill_turtle = ExecuteProcess(
        cmd = [f"ros2 service call /{ns}/remove_turtle turtlesim/srv/Kill \"name: 'turtle1'\""],
        shell = True
    )
    ld.add_action(kill_turtle)

    for i in range(len(name_list)):
        spawn_turtle = ExecuteProcess(
            cmd = [
                f"ros2 service call /{ns}/spawn_turtle turtlesim/srv/Spawn \"{{x: -1.0, y: -1.0, theta: 0.0, name: '/{name_list[i]}'}}\""
            ],
            shell = True
        )
        ld.add_action(spawn_turtle)


        for i in range(len(name_list)):    
            copy_turtle_node = Node(
                package='god_turtle',
                namespace=name_list[i],
                executable='copy_turtle.py',  
                name='copy_turtle',
                parameters=[
                    {'get_namespace': ns},
                    {'kp_d': 3.0},
                    {'kp_theta': 5.5}
                ]
            )
            ld.add_action(copy_turtle_node)

    
    return ld
