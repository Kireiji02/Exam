#!/usr/bin/python3
import rclpy
import yaml
from rclpy.node import Node
from turtlesim.srv import Spawn


class CopyTurtleNode(Node):
    def __init__(self):
        super().__init__('copy_turtle_node')

        # self.declare_parameter('')

        # self.spawn_turtle_client = self.create_client(Spawn,'/spawn_turtle')

        # self.spawn_turtle(0.1,0.1,0.0,'Foxy')
        # self.spawn_turtle(0.3,0.1,0.0,'Noetic')
        # self.spawn_turtle(0.8,0.1,0.0,'Humble')
        # self.spawn_turtle(1.4,0.1,0.0,'Iron')

        # Load positions from YAML
        self.positions = self.loadYAML()

        # Store positions for each turtle in separate variables
        self.foxy_positions_x, self.foxy_positions_y = self.get_turtle_positions(0)
        self.noetic_positions_x, self.noetic_positions_y = self.get_turtle_positions(1)
        self.humble_positions_x, self.humble_positions_y = self.get_turtle_positions(2)
        self.iron_positions_x, self.iron_positions_y = self.get_turtle_positions(3)

        # Print out the stored positions
        self.print_positions()


    def loadYAML(self):
        with open('/home/tim/Documents/GitHub/Exam/src/god_turtle/yaml_files/sang_via_point.yaml', 'r') as file:
            data = yaml.safe_load(file)
            return data

    # def spawn_turtle(self,x,y,theta,name):
    #     while not self.spawn_turtle_client.wait_for_service(1.0):
    #         self.get_logger().warn("Waiting for Server Starting . . .")
    #     spawn_request = Spawn.Request()
    #     spawn_request.x = x
    #     spawn_request.y = y
    #     spawn_request.theta = theta
    #     spawn_request.name = name
    #     self.spawn_turtle_client.call_async(spawn_request)
    #     self.get_logger().info(f'{name} has been spawned succesful')

    def get_turtle_positions(self, turtle_index):
        """
        Get positions for a specific turtle by its index.
        """
        turtle_positions = self.positions[turtle_index]
        x_positions = turtle_positions[0]
        y_positions = turtle_positions[1]
        return x_positions, y_positions

    def print_positions(self):
        # Print positions for each turtle
        print('Foxy Positions:')
        print(f'X: {self.foxy_positions_x}')
        print(f'Y: {self.foxy_positions_y}\n')

        print('Noetic Positions:')
        print(f'X: {self.noetic_positions_x}')
        print(f'Y: {self.noetic_positions_y}\n')

        print('Humble Positions:')
        print(f'X: {self.humble_positions_x}')
        print(f'Y: {self.humble_positions_y}\n')

        print('Iron Positions:')
        print(f'X: {self.iron_positions_x}')
        print(f'Y: {self.iron_positions_y}\n')
        print(type(self.iron_positions_x))
        

def main(args=None):
    rclpy.init(args=args)
    node = CopyTurtleNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
