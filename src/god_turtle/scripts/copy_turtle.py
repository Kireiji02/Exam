#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
from turtlesim_plus_interfaces.srv import GivePosition
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
import math
import yaml
import os


class CopyTurtleNode(Node):
    def __init__(self):
        super().__init__('copy_turtle_node')

        self.frequency = 100.0
        self.create_timer(1 / self.frequency, self.timer_callback)
        
        self.move_to_final_pos = False
        self.relay = False
        
       
        # Declare the parameters with default values as float arrays
        self.declare_parameter('kp_d',3.0)
        self.kp_d = self.get_parameter('kp_d').value
        self.declare_parameter('kp_theta',5.5)
        self.kp_theta = self.get_parameter('kp_theta').value
        
        self.declare_parameter('get_namespace', 'ns')
        self.get_ns = self.get_parameter('get_namespace').value
        
        if self.get_namespace() == '/Foxy':
            self.x_position_seq, self.y_position_seq = self.get_turtle_positions(0)
        elif self.get_namespace() == '/Noetic':
            self.x_position_seq, self.y_position_seq = self.get_turtle_positions(1)
        elif self.get_namespace() == '/Humble':
            self.x_position_seq, self.y_position_seq = self.get_turtle_positions(2)
        elif self.get_namespace() == '/Iron':
            self.x_position_seq, self.y_position_seq = self.get_turtle_positions(3)
        
        
        # Store positions as (x, y) tuples
        self.save_pos = [(self.x_position_seq[i], self.y_position_seq[i]) for i in range(len(self.x_position_seq))]
        
        self.turtle_pose = [0.0, 0.0, 0.0]

        # Create publisher and client
        self.logic_pub = self.create_publisher(Bool, 'logic', 10)
        self.cmd_vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.spawn_pizza_client = self.create_client(GivePosition, f'/{self.get_ns}/spawn_pizza')
        self.create_subscription(Pose, 'pose', self.callback_pose, 10)
        self.create_subscription(Bool, '/copy', self.callback_copy, 10)
        self.create_subscription(Bool, '/to_final_pos', self.callback_final_pos, 10)
        
        
        
    def logic(self, b):
        msg = Bool()
        msg.data = b
        self.logic_pub.publish(msg)

    def cmdvel(self, v, w):
        msg = Twist()
        msg.linear.x = v
        msg.angular.z = w
        self.cmd_vel_pub.publish(msg)
        
    def toTarget(self,a,b):
        target_x = a
        target_y = b

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

    def timer_callback(self):
        if self.relay:
            if self.move_to_final_pos == True:
                self.toTarget(11.0,11.0)
                
            if len(self.save_pos) > 0:
                self.toTarget(self.save_pos[0][0],self.save_pos[0][1])
                
            else:
                self.logic(True)
            
    def callback_pose(self, msg):
        self.turtle_pose[0] = msg.x
        self.turtle_pose[1] = msg.y
        self.turtle_pose[2] = msg.theta
        
    def callback_copy(self, msg):
        self.relay = msg.data
    
    def callback_final_pos(self, msg):
        self.move_to_final_pos = msg.data

    def spawn_pizza(self, x, y):
        while not self.spawn_pizza_client.wait_for_service(1.0):
            self.get_logger().warn('Waiting for Server...')
        
        position_request = GivePosition.Request()
        position_request.x = x
        position_request.y = y
        self.spawn_pizza_client.call_async(position_request)
        
    def loadYAML(self):
        with open('/home/kireiji/Documents/GitHub/Exam/src/god_turtle/yaml_files/sang_via_point.yaml', 'r') as file:
            data = yaml.safe_load(file)
        return data

    def get_turtle_positions(self, turtle_index):
        """
        Get positions for a specific turtle by its index.
        """
        turtle_positions = self.loadYAML()[turtle_index]
        x_positions = turtle_positions[0]
        y_positions = turtle_positions[1]
        return x_positions, y_positions
 


def main(args=None):
    rclpy.init(args=args)
    node = CopyTurtleNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
