import rclpy
import rclpy.node

class MinimalParam(rclpy.node.Node):
    def __init__(self):
        super().__init__('minimal_param_node')

        self.declare_parameter('arg_name', 'world')
        self.timer = self.create_timer(1, self.timer_callback)
        my_param = self.get_parameter('arg_name').get_parameter_value().string_value
        self.get_logger().info('(Constructor) Hello %s!' % my_param)

    def timer_callback(self):
        my_param = self.get_parameter('arg_name').get_parameter_value().string_value
        self.get_logger().info('(Timer) %s!' % my_param)


def main():
    rclpy.init()
    node = MinimalParam()
    rclpy.spin(node)


if __name__ == '__main__':
    main()
