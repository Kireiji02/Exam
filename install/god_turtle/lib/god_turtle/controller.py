#!/usr/bin/python3

import math
import yaml
import rclpy
import time
from rclpy.node import Node
from std_srvs.srv import Empty
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
        
        # self.declare_parameter('frequency', 100.0)   
        # self.frequency = self.get_parameter('frequency').value
        self.declare_parameter('pizza_limit',20)
        self.pizza_limit = self.get_parameter('pizza_limit').value
        
        self.declare_parameter('name', 'turtle')
        self.name = self.get_parameter('name').get_parameter_value().string_value
        
        self.declare_parameter('save_limit', 4)
        self.save_max = self.get_parameter('save_limit').value
        
        self.kp_d = 3.0
        self.kp_theta = 25
        self.turtle_pose = [0.0,0.0,0.0]
        self.save_count = 0 # number of pizza config saved (max at 4 times [0,1,2,3])
        self.pizza_count = 1 # number of spawned pizzas
        self.remaining_pizza = 0 # Number of remaining pizzas
        # self.check_pizza_remain = 0 
        self.received_flag = 0 # Recieve action keys
        self.save_pizza = [[[],[]],[[],[]],[[],[]],[[],[]]] #fix hard code----------------
        self.clear_pizza = [[0.0],[0.0]] # Clear all unsaved pizzas present in the workspace by eating
        
        #---------------------Topics---------------------#
        
        self.cmd_vel_pub = self.create_publisher(Twist,'cmd_vel',10)
        self.remaining_pizza_pub_ = self.create_publisher(Int64,'pizza_count',10)
        
        self.create_subscription(Twist, '/cmd_vel', self.callback_abs_cmd, 10)
        self.create_subscription(Pose, 'pose', self.callback_pose, 10)
        self.create_subscription(Int64, 'pizza_count',self.pizza_count_callback,10)
        self.create_subscription(Int64,'/flag_req',self.flag_req_callback,10)
        
        #--------------------Services--------------------#
        
        self.spawn_pizza_client = self.create_client(GivePosition, f'/{self.name}/spawn_pizza')
        self.eat_client = self.create_client(Empty, 'eat') 
        
    #---------------------Control---------------------#
        
    def cmdvel(self, v, w):
        msg = Twist()
        msg.linear.x = v
        msg.angular.z = w
        self.cmd_vel_pub.publish(msg)
        
    #---------------------Callback---------------------#
    def flag_req_callback(self,msg):
        self.received_flag = msg.data
    
    def pizza_count_callback(self,msg):
        self.remaining_pizza = msg.data

    def timer_callback(self):
        # self.get_logger().info(f'\n{self.pizza_count}\n{self.remaining_pizza}')
        if len(self.clear_pizza[0]) > 0:
            delta_x = self.clear_pizza[0][0]-self.turtle_pose[0]
            delta_y = self.clear_pizza[1][0]-self.turtle_pose[1]
            dist = math.sqrt(pow(delta_x,2)+pow(delta_y,2))
            alpha = math.atan2(delta_y,delta_x)
            e_theta = alpha-self.turtle_pose[2]

            if dist > 0.15:
                if e_theta > math.pi:
                    e_theta -= 2*math.pi
                elif e_theta < -math.pi:
                    e_theta += 2*math.pi
                    
                vx = self.kp_d*dist
                w = self.kp_theta*e_theta
            
            else:
                vx = 0.0
                w = 0.0
                # self.get_logger().info("Turtle is at the pizza. Trying to eat...")
                # self.eat_pizza()
                # self.get_logger().info(f'{len(self.clear_pizza[0])}')
                self.clear_pizza = [self.clear_pizza[0][1:],self.clear_pizza[1][1:]]
                self.pizza_count -= 1
                
            if dist < 0.16:
                self.eat_pizza()
                
            self.cmdvel(vx, w)
                
        
    def callback_pose(self,msg):
        
        self.turtle_pose[0] = msg.x
        self.turtle_pose[1] = msg.y
        self.turtle_pose[2] = msg.theta
        
        self.pizza_limit = self.get_parameter('pizza_limit').value
        # self.get_logger().info(self.save_count-1)
        if self.received_flag == 1 :
            if self.save_count < 4 :
                if self.pizza_count < self.pizza_limit:
                    self.spawn_pizza(msg.x, msg.y)
                    self.get_logger().info(f"\n Spawn pizza:: at X: {msg.x:.5f} Y: {msg.y:.5f} \n Remaining Pizza: {self.remaining_pizza}/{self.pizza_limit}")

        elif self.received_flag == 2 :
            self.pizza_count += 1
            with  open('/home/kireiji/Documents/GitHub/Exam/src/god_turtle/yaml_files' + str(self.get_namespace()) + '_via_point.yaml', 'w') as file:
                yaml.dump(self.save_pizza,file)
        
            if self.save_count < 4 :
                self.get_logger().info(f'\n==================================\n      Saved successfully {self.save_count+1}/{self.save_max}\n==================================')
                self.save_count += 1
                
            self.clear_pizza = [[self.turtle_pose[0]],[self.turtle_pose[1]]]
        
        elif self.received_flag == 3 :
            if self.save_count < 4:
                if self.save_count >= 0 and self.save_count < 4 :
                    self.get_logger().info(f'\n==================================\n             Clearing\n==================================')
                    
                    self.clear_pizza = self.save_pizza[self.save_count]
                    # self.get_logger().info(f'{self.clear_pizza}')
                    
                self.save_pizza[self.save_count] = [[],[]]
        
                
        self.received_flag = 0 
    def callback_abs_cmd(self,msg):
        self.cmdvel(msg.linear.x,msg.angular.z)
        
        
    #----------------------Service----------------------#
    
    def eat_pizza(self):
        while not self.eat_client.wait_for_service(1.0):
            self.get_logger().warn('Waiting for Server...')
        # time.sleep(0.5)
        if self.eat_client.service_is_ready():
            eat_request = Empty.Request()
            self.eat_client.call_async(eat_request)
            
        
        
    def spawn_pizza(self, x, y):
        while not self.spawn_pizza_client.wait_for_service(1.0):
            self.get_logger().warn('Waiting for Server...')
        position_request = GivePosition.Request()
        position_request.x = x
        position_request.y = y

        if self.pizza_count < self.pizza_limit:
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
