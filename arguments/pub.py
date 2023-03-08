import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class PubNode(Node):

    def __init__(self):
        super().__init__('pub')

        # self.declare_parameter(name='num', value=10)
        self.declare_parameters(namespace='', parameters=[
            ('num', 10),
            ('timer_delay', 1.0)
        ])

        self.pub = self.create_publisher(
            Int32,
            '/pub_topic',
            10
        )

        self.create_timer(
            self.get_parameter('timer_delay').value, 
            self.execute
        )
    
    def execute(self):
        num = self.get_parameter('num').value

        msg = Int32(data=num)

        self.get_logger().info(f'Publishing: {msg}')
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = PubNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()