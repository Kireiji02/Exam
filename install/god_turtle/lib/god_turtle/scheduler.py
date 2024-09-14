#!/usr/bin/python3

from god_turtle.dummy_module import dummy_function, dummy_var
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool


class SchedulerNode(Node):
    def __init__(self):
        super().__init__('scheduler_node')
        
        self.frequency = 100.0
        self.create_timer(1 / self.frequency, self.timer_callback)
        
        self.mux1 = False
        self.mux2 = False
        self.mux3 = False
        self.mux4 = False
        
        self.create_subscription(Bool, '/Foxy/logic', self.callback_1, 10)
        self.create_subscription(Bool, '/Noetic/logic', self.callback_2, 10)
        self.create_subscription(Bool, '/Humble/logic', self.callback_3, 10)
        self.create_subscription(Bool, '/Iron/logic', self.callback_4, 10)
        self.to_final_pos_pub = self.create_publisher(Bool, '/to_final_pos', 10)
        
    def toFinalPose(self, b):
        msg = Bool()
        msg.data = b
        self.to_final_pos_pub.publish(msg)
        
    def timer_callback(self):
        if self.mux1 == True and self.mux2 == True and self.mux3 == True and self.mux4 == True:
            self.toFinalPose(True)
        
    def callback_1 (self, msg):
        self.mux1 = msg.data
    
    def callback_2 (self, msg):
        self.mux2 = msg.data
    
    def callback_3 (self, msg):
        self.mux3 = msg.data
    
    def callback_4 (self, msg):
        self.mux4 = msg.data

def main(args=None):
    rclpy.init(args=args)
    node = SchedulerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
