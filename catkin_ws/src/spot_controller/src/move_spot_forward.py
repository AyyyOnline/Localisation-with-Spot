import rospy
from geometry_msgs.msg import Twist


"""The following function will aim to instruct spot to move forwards"""
def move_spot_forward():
    # initialise a ROS node
    rospy.init_node('spot_move_forward')


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
        rospy.logerr("Service call failed: %s" % e)


if __name__ == '__main__':
    try:
        move_spot_forward
    except rospy.ROSInterruptException
        pass

