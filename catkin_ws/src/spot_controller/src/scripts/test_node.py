#!/usr/bin/env python3
import rospy

'''
rosrun rospy_tutorials talker talker - node that prints and sends data to another node
rosrun rospy_tutorials talker listener - is receiving info from talker
This was observed by running rqt_graph to viusualise the nodes:
(talker->chatter->listener)

There are multiple ways to check various info around the nodes running using rostopic. These include:
    list                                # lists nodes
    info /chatter                       # lists publishers and subscribers
    echo /chatter                       # shows the type of data used
    rosmsg show std_msgs/String

'''

if __name__ == '__main__':
    rospy.init_node("test_node")        # initilaise node to register file
    rospy.loginfo("node is active")     # display info msg
    rospy.logwarn("Warning")            # display warning msg
    rospy.logerr("Error detected")      # display error msg
    rate = rospy.Rate(5)        # setup a rate of speed for an object to loop
    rospy.sleep(0.5)        

    # loop to test rate
    while not rospy.is_shutdown():      
        rospy.loginfo("hello")
        rate.sleep()

    rospy.loginfo("End")