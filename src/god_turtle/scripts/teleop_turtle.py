#!/usr/bin/python3

# from god_turtle.dummy_module import dummy_function, dummy_var
import yaml
import rclpy
import sys
import termios
import tty
from rclpy.node import Node
from geometry_msgs.msg import Twist
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

        #--------------------Keyblinds--------------------#

        self.settings = termios.tcgetattr(sys.stdin)
        
        #--------------------Variables--------------------#
        
        self.declare_parameter('frequency', 10.0)   
        self.frequency = self.get_parameter('frequency').get_parameter_value().double_value
        
        self.create_timer(1/self.frequency, self.timer_callback)
        # self.target_pos = self.loadYAML()
        
        #---------------------Topics---------------------#

        self.cmd_vel_pub = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.create_subscription(Pose, 'turtle1/pose', self.callback_pose, 10)
        
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
        
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
    #---------------------Callback---------------------#
    
    def timer_callback(self):
        self.spawn_pizza(0.5,0.5)
        
    def callback_pose(self,msg):

        key = get_key(self.settings)
        if key in KEY_BINDINGS:
<<<<<<< Updated upstream
                v, w = KEY_BINDINGS[key]
                self.cmdvel(v, w)
=======
                linear, angular = KEY_BINDINGS[key]
                self.cmdvel(linear, angular)
>>>>>>> Stashed changes
        elif key == 'i':
            self.spawn_pizza(msg.x, msg.y)
        self.get_logger().info(f"{msg.x} and {msg.y}")
        
    #----------------------Service----------------------#
        
    def spawn_pizza(self, x, y):
        while not self.spawn_pizza_client.wait_for_service(1.0):
            self.get_logger().warn('Waiting for Server...')
        position_request = GivePosition.Request()
        position_request.x = x
        position_request.y = y
        
        data = {}

        with  open('/home/kireiji/Documents/GitHub/Exam/src/god_turtle/yaml_files' + str(self.get_namespace()) + '_via_point.yaml', 'w') as file:
            yaml.dump({},file)
            data = {'targets': [x, y]}
            
        with  open('/home/kireiji/Documents/GitHub/Exam/src/god_turtle/yaml_files' + str(self.get_namespace()) + '_via_point.yaml', 'w') as file:
            yaml.dump(data,file)
            
        self.spawn_pizza_client.call_async(position_request)
    
def main(args=None):
    rclpy.init(args=args)
    node = TeleopNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
