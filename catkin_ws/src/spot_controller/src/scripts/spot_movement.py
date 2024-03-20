#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

"""The following function will aim to instruct spot to move forwards
def move_spot_forward():
    # initialise ROS node
    rospy.init_node('move_spot_forward')

    # set the desired walking speed in metres/second
    linear_x = 0.2

    cmd_vel = Twist()
    cmd_vel.linear.x = linear_x

    # get ROS service proxy for spot_cmd_vel
    service_proxy = rospy.ServiceProxy('/spot/cmd_vel', Twist)

    # send the command to spot
    try:
        # duration to walk 10 metres
        dur = 5 / linear_x
        start_time = rospy.get_time()
       
        while (rospy.get_time() - start_time) < dur:
            service_proxy(cmd_vel)
            rospy.sleep(0.2)        # sleep for 0.2 secs between commands

        # stop the robot after reaching the target distance
        cmd_vel.linear.x = 0.0
        service_proxy(cmd_vel)
        rospy.loginfo("Spot has moved forward by 10 metres.")
    except rospy.ServiceException as e:
        rospy.logerr("Error detected: %s" % e)
"""
# Function aimed to instruct spot to move forwards
def move_spot_forward():
  # Initialize ROS node
  rospy.init_node('spot_movement')

  # Define publisher for velocity commands
  vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

  # Set desired velocity (adjust values for desired movement)
  linear_x = 0.5  # Forward speed (m/s)
  angular_z = 0.0  # Rotational speed (rad/s)

  # Create Twist message with desired velocities
  twist_msg = Twist()
  twist_msg.linear.x = linear_x
  twist_msg.angular.z = angular_z

  # Publish the velocity command
  rate = rospy.Rate(10)  # Publish at 10 Hz
  while not rospy.is_shutdown():
    vel_pub.publish(twist_msg)
    rate.sleep()

if __name__ == '__main__':
    #rospy.init_node('move_spot_forward')
    #rospy.loginfo("Moving spot node has started")

    """
    Publish to the relevant topic, info gathered from rostop info /cmd_vel/smooth rosshow 
    geometry_msgs/Twist
    queue_size is a buffer for unreliable networks when lots of messages are being sent but it
    is good to have regardless
    """
    '''
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)      
    
    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        # create message to send based on data displayed by geometry_msgs/Twist
        msg = Twist()
        msg.linear.x = 10.0
        msg.angular.z = 0.0
        #msg.linear.y = 0.0
        pub.publish(msg)
        rate.sleep()
    '''
    
    try:
        move_spot_forward()
    except rospy.ROSInterruptException:
        pass
    