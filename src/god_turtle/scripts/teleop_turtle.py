#!/usr/bin/python3

# from god_turtle.dummy_module import dummy_function, dummy_var
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

# Key bindings
KEY_BINDINGS = {
    'w': (3.0, 0.0),
    's': (-3.0, 0.0),
    'a': (0.0, 2.0),
    'd': (0.0, -2.0),
    'q': (0.0, 0.0)
}

def get_key(settings):
    """
    Capture key input from the terminal.
    """
    tty.setraw(sys.stdin.fileno())
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

class TeleopNode(Node):
    def __init__(self):
        super().__init__('teleop_node')

        print(
            """
    ---------------- Turtle Teleop ---------------- 

                        W
                    A   S   D

    W: Moving Forward (linear velocity = 3.0 m/s)
    S: Moving Backward (linear velocity = -3.0 m/s)
    D: Turn Right (angular velocity = 2.0 rad/s)
    A: Turn Left (angular velocity = -2.0 rad/s)

    I: Spawn Pizza accord to the current position 
    E: Save all the pizza positions 

    ------------------------------------------------

        """
        )
        #--------------------Keyblinds--------------------#

        self.settings = termios.tcgetattr(sys.stdin)
        
        self.frequency = 100.0
        self.create_timer(1/self.frequency, self.timer_callback)
        # self.target_pos = self.loadYAML()
        
        #---------------------Topics---------------------#

        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.send_flag_req_pub = self.create_publisher(Int64,'/flag_req',10)
        # self.create_subscription(Int64,'flag_res',10)
    
    
    def send_flag(self,flag):
        msg = Int64()
        msg.data = flag
        self.send_flag_req_pub.publish(msg)
        
    #---------------------Control---------------------#

    def cmdvel(self, v, w):
        msg = Twist()
        msg.linear.x = v
        msg.angular.z = w
        self.cmd_vel_pub.publish(msg)
        
    def timer_callback(self):
        key = get_key(self.settings)
        if key in KEY_BINDINGS:
            linear, angular = KEY_BINDINGS[key]
            self.cmdvel(linear, angular)
    
        elif key == 'i':
            self.send_flag(1)
                
        elif key == 'e':
            self.send_flag(2)
            
        elif key == 'c':
            self.send_flag(3)
                
        elif key == "\x03" :
            rclpy.shutdown()
    
def main(args=None):
    rclpy.init(args=args)
    node = TeleopNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
