#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from custom_messages_pkg.srv import TwoInts_OneInt

# called when service is requested
def handle_addition_request(request):
	result = request.input1 + request.input2
        rospy.loginfo("Sum" + str(request.input1) + " + " + str(request.input2) + " = " + str(result))
        return result

if __name__ == '__main__':
        rospy.init_node('service_server')
        rospy.loginfo("Service server has been started")

        # Create a service
        service = rospy.Service("/addition_service", TwoInts_OneInt, handle_addition_request)

        # stops and waits for here until message received
        rospy.spin()

        rospy.loginfo("exiting service_server.py")
