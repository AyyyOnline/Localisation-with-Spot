import rospy
from geometry_msgs.msg import PoseStamped, Twist
from math import atan2, sqrt

def path_deviation_correction(current_pose):
  # straight line path with a fixed target point
  target_x = 5.0    # targets x coordinate
  target_y = 0.0    # targets y coordinate
  return target_x, target_y

def path_follow(current_pose):
  """
  Simple line following algorithm for Spot.
  """

  # Get closest point on the path
  target_x, target_y = path_deviation_correction(current_pose.pose)

  # Calculate error (distance from the line)
  error_x = target_x - current_pose.pose.position.x
  error_y = target_y - current_pose.pose.position.y

  # Calculate the desired heading angle
  desired_heading = atan2(error_y, error_x)

  # Calculate the current heading angle
  current_heading = current_pose.pose.orientation.w  # w is the standard component for storing the yaw rotation (angular movement of an object around its vertical axis)

  # Calculate the angular error (difference between desired and current heading)
  angular_error = desired_heading - current_heading

  # Adjust for angular wrap-around. Wrap-around determines the most efficient direction to turn based on its current heading and the desired change in direction. Makes for smoother and more precise control.
  if angular_error > np.pi:
    angular_error -= 2.0 * np.pi
  elif angular_error < -np.pi:
    angular_error += 2.0 * np.pi

  # Proportional gain for angular error
  kp_angular = 1.0

  # Create a Twist message to send velocity commands
  twist_msg = Twist()
  twist_msg.linear.x = 0.5  # Set a forward linear velocity (adjust as needed)
  twist_msg.angular.z = kp_angular * angular_error  # Apply proportional control to steering

  # Publish the velocity command
  pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
  pub.publish(twist_msg)

def main():
  rospy.init_node('path_following')

  # Subscribe to Spot's odometry topic or tf
  rospy.Subscriber('/odom', PoseStamped, path_follow)

  # Start the ROS spin loop to keep the node running and listen for data
  rospy.spin()          

if __name__ == '__main__':
  main()
