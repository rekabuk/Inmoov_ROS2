import rclpy
from rclpy.node import Node

from std_msgs.msg import Int16
from std_msgs.msg import Int32


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('pose_capture')
        self.subscription = self.create_subscription(
            Int16,
            '/jaw',
            self.jaw_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.get_logger().info('Subscriber started')

    def jaw_callback(self, msg):
        self.get_logger().info('Hi')
        self.get_logger().info('Received: %d' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    pose_capture = MinimalSubscriber()

    try:
        rclpy.spin(pose_capture)
    except KeyboardInterrupt:
        pass
   # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    pose_capture.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()






    #https://robotics.stackexchange.com/questions/101471/dynamic-publishers-subscribers-and-callbacks


#    https://www.google.com/search?client=firefox-b-d&hs=kIKp&sca_esv=85eca064802d3472&channel=entpr&q=ros2+subsrribe+to+an+array+of+topics&nfpr=1&sa=X&ved=2ahUKEwjz65TbiM-SAxWAVEEAHWmnM7UQvgUoAXoECBEQAg&biw=1604&bih=931&dpr=1