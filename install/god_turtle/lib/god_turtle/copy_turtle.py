#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn


class CopyTurtleNode(Node):
    def __init__(self):
        super().__init__('copy_turtle_node')

        # Declare the parameters with default values as float arrays
        self.declare_parameter('x_positions', None)
        self.x_position_seq = self.get_parameter('x_positions').get_parameter_value().double_array_value
        self.declare_parameter('y_positions', None)
        self.y_position_seq = self.get_parameter('y_positions').get_parameter_value().double_array_value

        
        self.spawn_turtle_client = self.create_client(Spawn, '/spawn_turtle')

        # Spawn the turtle at the first position in the list
        if len(self.x_position_seq) > 0 and len(self.y_position_seq) > 0:
            self.spawn_turtle(0.1, 0.1, 0.0, self.get_name())
        else:
            self.get_logger().error("No positions provided for the turtle.")
            
    def spawn_turtle(self, x, y, theta, name):
        while not self.spawn_turtle_client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for the /spawn service to be available...")
        
        spawn_request = Spawn.Request()
        spawn_request.x = x
        spawn_request.y = y
        spawn_request.theta = theta
        spawn_request.name = name

        future = self.spawn_turtle_client.call_async(spawn_request)
        future.add_done_callback(self.turtle_spawned_callback)

    def turtle_spawned_callback(self, future):
        try:
            response = future.result()
            self.get_logger().info(f'{response.name} has been spawned successfully!')
        except Exception as e:
            self.get_logger().error(f"Failed to spawn turtle: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = CopyTurtleNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
