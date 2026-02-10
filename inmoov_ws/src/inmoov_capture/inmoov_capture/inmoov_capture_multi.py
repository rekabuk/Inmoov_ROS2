import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int16
from functools import partial


class MultiTopicSubscriber(Node):
    def __init__(self):
        super().__init__('multi_topic_subscriber')
        
        # Array of topics to subscribe to
        self.topic_names = ['/shoulder_R', '/rotate_R', '/omoplate_R','/jaw']
        self.subs = []
        
        # Create a subscriber for each topic
        for topic in self.topic_names:
            sub = self.create_subscription(
                Int16,
                topic,
                partial(self.listener_callback, index=1),
                10)
            self.subs.append(sub)
            self.get_logger().info(f'Subscribed to: {topic}')

    def listener_callback(self, msg, index):
        # Callback processes messages from all topics
        self.get_logger().info(f'Received: "{self.topic_names[index]}" "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = MultiTopicSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()