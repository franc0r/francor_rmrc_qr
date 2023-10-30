import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import datetime


class MyNode(Node):
    def __init__(self):
        super().__init__('qr_log')
        rclpy.get_default_context().on_shutdown(self.shutdown)

        # Create subscriber to receive QR codes
        self._subscription = self.create_subscription(
            String,
            '/qr_codes',
            self.listener_callback,
            10)

        # QR code list        
        self._qr_timestamp_list = []
        self._qr_code_list = []

    def listener_callback(self, msg):
        # Check if QR code is already in list and list is not larger than 100 entries
        if msg.data not in self._qr_code_list and len(self._qr_code_list) < 100:
            # Append QR code to list
            self._qr_code_list.append(msg.data)

            # Append timestamp to list
            now = datetime.datetime.now()
            self._qr_timestamp_list.append(now.strftime("%H:%M:%S"))

            # Print QR code to console
            self.get_logger().info('QR-Code: %s' % msg.data)

    def shutdown(self):
        # Found QR codes
        self.get_logger().info('Found QR codes: %d' % len(self._qr_code_list))

        # Generate filename with current date
        now = datetime.datetime.now()
        filename = now.strftime("%Y-%m-%d_%H%M%S-qr_codes.txt")
        self.get_logger().info('Store QR codes to file %s' % filename)

        # Store QR codes to file
        with open(filename, 'w') as f:
            for idx in range(len(self._qr_code_list)):
                f.write("%s : %s\n" % (self._qr_timestamp_list[idx], self._qr_code_list[idx]))

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    try:
        rclpy.spin(node)
    finally:
        print('Shutdown')
        node.shutdown()

    node.destroy_node()        
    rclpy.shutdown()

if __name__ == '__main__':
    main()
