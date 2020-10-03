#!/usr/bin/env python

import rospy
import numpy as np
from std_msgs.msg import String
from induction_task.msg import TurtleInfo # Import the turtle information

pub = rospy.Publisher('ocean', TurtleInfo, queue_size=10) # Topic is called ocean
rospy.init_node('turtle', anonymous=True) # Node is called turtle
rate = rospy.Rate(5) # 5 samples a seconds
Index_count =0 # This is how we count the iterations, as we need to also return the index

while not rospy.is_shutdown():
	msg = TurtleInfo()
	Quality_run = np.random.randint(1,11) # Quality ranges from 1 to 10
	Index_count+=1 # Update index for each run
	
	if Quality_run>=7: # Only returning turtles with a high enough quality
		
		msg.quality = str(Quality_run)
		msg.index = str(Index_count)

		rospy.loginfo(msg)
		pub.publish(msg)
		rate.sleep()

	else: # If quality <7, dont return anything
		rate.sleep()
		pass

if __name__ == '__main__':
	try:
		main_function()
	except rospy.ROSInterruptException:
		pass
