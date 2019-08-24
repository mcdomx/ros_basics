#!/usr/bin/env python


# This container has the task of analyzing an image array
# and returning a dictionary that includes the objects identified
# and a count of their occurrances.  Each entry also contains
# a time stamp and the topic name from where the data was collected.
# Once the dictionary entry is returned, the corresponding image can
# be deleted.

# Each dictionary entry is represented by a file where the name of the file
# corresponds to the name of the array file from which the objects were
# counted.  This will allow the subscriber to identify which image array
# files can be deleted.

# This container only performs the object count of an image and
# returns the results.

# Because counting objects in images may be processor intensive
# This image is not using ROS since ROS does not communicate
# between RaspberryPi's and Mac or Windows reliably.

# Data is exchanged using share Docker volumes.


import objectCounter

if __name__ == '__main__':

	print("Obect Counter has started")
	# Get a new image array

	# Count the objects in the array

	# Create a file with a dictionary entry of counted objects and occurrances

	# Put the dict file back on the device where the image came from