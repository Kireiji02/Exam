#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
from turtlesim_plus_interfaces.srv import GivePosition
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math


class CopyTurtleNode(Node):
    def __init__(self):
        super().__init__('copy_turtle_node')

        self.frequency = 100.0
        self.create_timer(1 / self.frequency, self.timer_callback)
        
        # Declare the parameters with default values as float arrays
        self.kp_d = 3.0
        self.kp_theta = 5.5
        self.declare_parameter('get_namespace', 'ns')
        self.get_ns = self.get_parameter('get_namespace').value
        
        # Get the positions from parameters
        self.declare_parameter('x_positions', None)
        self.declare_parameter('y_positions', None)
        self.x_position_seq = self.get_parameter('x_positions').value
        self.y_position_seq = self.get_parameter('y_positions').value
        
        # Store positions as (x, y) tuples
        self.save_pos = [(self.x_position_seq[i], self.y_position_seq[i]) for i in range(len(self.x_position_seq))]
        
        self.turtle_pose = [0.0, 0.0, 0.0]

        # Create publisher and client
        self.cmd_vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.spawn_pizza_client = self.create_client(GivePosition, f'/{self.get_ns}/spawn_pizza')
        self.create_subscription(Pose, 'pose', self.callback_pose, 10)
        
        self.trig = 0

    def cmdvel(self, v, w):
        msg = Twist()
        msg.linear.x = v
        msg.angular.z = w
        self.cmd_vel_pub.publish(msg)

    def timer_callback(self):
        if len(self.save_pos) > 0:
            target_x = self.save_pos[0][0]
            target_y = self.save_pos[0][1]

            delta_x = target_x - self.turtle_pose[0]
            delta_y = target_y - self.turtle_pose[1]
            dist = math.sqrt(pow(delta_x, 2) + pow(delta_y, 2))
            alpha = math.atan2(delta_y, delta_x)
            e_theta = alpha - self.turtle_pose[2]

            if dist > 0.15:
                if e_theta > math.pi:
                    e_theta -= 2 * math.pi
                elif e_theta < -math.pi:
                    e_theta += 2 * math.pi

                vx = self.kp_d * dist
                w = self.kp_theta * e_theta
            else:
                vx = 0.0
                w = 0.0
                self.spawn_pizza(target_x, target_y)
                self.save_pos.pop(0)
            
            self.cmdvel(vx, w)

    def callback_pose(self, msg):
        self.turtle_pose[0] = msg.x
        self.turtle_pose[1] = msg.y
        self.turtle_pose[2] = msg.theta

    def spawn_pizza(self, x, y):
        while not self.spawn_pizza_client.wait_for_service(1.0):
            self.get_logger().warn('Waiting for Server...')
        
        position_request = GivePosition.Request()
        position_request.x = x
        position_request.y = y
        self.spawn_pizza_client.call_async(position_request)


def main(args=None):
    rclpy.init(args=args)
    node = CopyTurtleNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
