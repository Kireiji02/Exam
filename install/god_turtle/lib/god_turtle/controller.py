#!/usr/bin/python3

import yaml
import rclpy
import sys
import termios
import tty
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Int64
from turtlesim.msg import Pose
from turtlesim_plus_interfaces.srv import GivePosition


class ControllerNode(Node):
    def __init__(self):
        super().__init__('controller_node')
        
        self.frequency = 100.0
        self.create_timer(1/self.frequency, self.timer_callback)
        
        #--------------------Variables--------------------#
        
        self.declare_parameter('frequency', 10.0)   
        self.frequency = self.get_parameter('frequency').value
        self.declare_parameter('pizza_limit',20)
        self.pizza_limit = self.get_parameter('pizza_limit').value
        
        self.save_count = 0
        self.save_max = 4 # do param later
        self.pizza_count = 0
        self.remaining_pizza = 0
        self.check_pizza_remain = 0
        self.received_flag = 0
        self.save_pizza = [[[],[]],[[],[]],[[],[]],[[],[]]] #fix hard code
        
        #---------------------Topics---------------------#
        
        self.cmd_vel_pub = self.create_publisher(Twist,'cmd_vel',10)
        self.remaining_pizza_pub_ = self.create_publisher(Int64,'pizza_count',10)
        
        self.create_subscription(Twist, '/cmd_vel', self.callback_abs_cmd, 10)
        self.create_subscription(Pose, 'pose', self.callback_pose, 10)
        self.create_subscription(Int64, 'pizza_count',self.pizza_count_callback,10)
        self.create_subscription(Int64,'/flag_req',self.flag_req_callback,10)
        
        #--------------------Services--------------------#
        
        self.spawn_pizza_client = self.create_client(GivePosition, '/spawn_pizza')
        
    #---------------------Control---------------------#
        
    def cmdvel(self, v, w):
        msg = Twist()
        msg.linear.x = v
        msg.angular.z = w
        self.cmd_vel_pub.publish(msg)
        
    # def loadYAML(self):
    #     with open('/home/kireiji/RoboticsDev_ws/src/motorsim/via_point/via_point.yaml', 'r') as file:
    #         data = yaml.safe_load(file)
    #         return data['targets']
        
    #---------------------Callback---------------------#
    def flag_req_callback(self,msg):
        self.received_flag = msg.data
    
    def pizza_count_callback(self,msg):
        self.check_pizza_remain = msg.data

    def timer_callback(self):
        pass
       
        
        
    def callback_pose(self,msg):
        self.pizza_limit = self.get_parameter('pizza_limit').value
        if self.received_flag == 1 :
            if self.pizza_count <= self.pizza_limit:
                self.spawn_pizza(msg.x, msg.y)
                self.get_logger().info(f"\n Spawn pizza:: at X: {msg.x:.5f} Y: {msg.y:.5f} \n Remaining Pizza: {self.remaining_pizza}/{self.pizza_limit}")
                
        # data = {'pos1' : [],'pos2' : [],'pos3' : [],'pos4' : []}
        # data = {'pos1' : self.save_pizza}

        if self.received_flag == 2 :
            with  open('/home/kireiji/Documents/GitHub/Exam/src/god_turtle/yaml_files' + str(self.get_namespace()) + '_via_point.yaml', 'w') as file:
                yaml.dump(self.save_pizza,file)
        
            if self.save_count < 4 :
                self.save_count += 1
                
        self.received_flag = 0 
    def callback_abs_cmd(self,msg):
        self.cmdvel(msg.linear.x,msg.angular.z)
        
        
    #----------------------Service----------------------#
        
    def spawn_pizza(self, x, y):
        while not self.spawn_pizza_client.wait_for_service(1.0):
            self.get_logger().warn('Waiting for Server...')
        position_request = GivePosition.Request()
        position_request.x = x
        position_request.y = y

        self.pizza_count += 1
        self.spawn_pizza_client.call_async(position_request)

        self.remaining_pizza = self.pizza_limit - self.pizza_count
        remaining = Int64()
        remaining.data = self.pizza_limit - self.pizza_count
        
        if self.received_flag == 1 :
            if self.save_count == 0 :
                self.save_pizza[0][0].append(x)
                self.save_pizza[0][1].append(y)
            elif self.save_count == 1 :
                self.save_pizza[1][0].append(x)
                self.save_pizza[1][1].append(y)
            elif self.save_count == 2 :
                self.save_pizza[2][0].append(x)
                self.save_pizza[2][1].append(y)
            elif self.save_count == 3 :
                self.save_pizza[3][0].append(x)
                self.save_pizza[3][1].append(y)
            
        self.spawn_pizza_client.call_async(position_request)

def main(args=None):
    rclpy.init(args=args)
    node = ControllerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
