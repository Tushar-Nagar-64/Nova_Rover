// Include the message files and packages 
#include "ros/ros.h"
#include <induction_task/TurtleInfo.h>
#include "std_msgs/String.h"

// Standard namespace for strings
using namespace std;

#include <sstream> // Used for displaying output

// The callback when data has been received
void turtleCallback(const induction_task::TurtleInfo::ConstPtr& msg) {
  ROS_INFO("I heard: [%s]", msg->quality.c_str());
  ROS_INFO("I heard: [%s]", msg->index.c_str());
}

// The main function called when executed
int main (int argc, char **argv) {

	ros::init(argc, argv, "listener");
	ros::NodeHandle n;
	ros::Subscriber sub = n.subscribe("ocean", 1000, turtleCallback);
	ros::spin();

	return 0;
}
