#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from rospy_tutorials.srv import AddTwoInts

# called when service is requested
def handle_service_request(request):
	result = request.a + request.b
        rospy.loginfo("Sum" + str(request.a) + " + " + str(request.b) + " = " + str(result))
        return result

if __name__ == '__main__':
        rospy.init_node('service_server')
        rospy.loginfo("Service server has been started")

        # Create a service
        service = rospy.Subscriber("/basic_service", AddTwoInts, handle_service_request)

        # stops and waits for here until message received
        rospy.spin()

        rospy.loginfo("existing service.py")
