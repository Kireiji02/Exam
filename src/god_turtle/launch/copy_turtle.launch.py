from launch import LaunchDescription
from launch_ros.actions import Node
import yaml


def loadYAML():
    with open('/home/tim/RoboticsDev2024/src/god_turtle/yaml_files/sang_via_point.yaml', 'r') as file:
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
    name_list = ['Foxy', 'Noetic', 'Humble', 'Iron']
    ld = LaunchDescription()
    
    for i in range(len(name_list)):
        positions_x, positions_y = get_turtle_positions(i)
        copy_turtle_node = Node(
            package='god_turtle',
            namespace='',
            executable='copy_turtle.py',  # No need for .py extension here
            name=name_list[i],
            parameters=[
                {'x_positions': positions_x},
                {'y_positions': positions_y}
            ]
        )
        ld.add_action(copy_turtle_node)
    
    return ld
