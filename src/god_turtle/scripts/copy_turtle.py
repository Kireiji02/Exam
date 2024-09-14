#!/usr/bin/python3

from motorsim.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node
from motorsim.dc_motor_model import DCMotorModel
from turtlesim.srv import Spawn


class CopyTurtleNode(Node):
    def __init__(self):
        super().__init__('copy_turtle_node')

        # self.declare_parameter('')

        self.spawn_turtle_client = self.create_client(Spawn,'/spawn_turtle')

        self.spawn_turtle(0.1,0.1,0.0,'Foxy')
        self.spawn_turtle(0.3,0.1,0.0,'Noetic')
        self.spawn_turtle(0.8,0.1,0.0,'Humble')
        self.spawn_turtle(1.4,0.1,0.0,'Iron')

    def spawn_turtle(self,x,y,theta,name):
        while not self.spawn_turtle_client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server Starting . . .")
        spawn_request = Spawn.Request()
        spawn_request.x = x
        spawn_request.y = y
        spawn_request.theta = theta
        spawn_request.name = name
        self.spawn_turtle_client.call_async(spawn_request)
        self.get_logger().info(f'{name} has been spawned succesful')

def main(args=None):
    rclpy.init(args=args)
    node = CopyTurtleNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
