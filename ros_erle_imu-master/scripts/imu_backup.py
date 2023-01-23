#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu
from std_msgs.msg import String

IMU_whole = Imu()

def callback_gyro(msg):
	IMU_whole.angular_velocity.x = msg.angular_velocity.x
	IMU_whole.angular_velocity.y = msg.angular_velocity.y
	IMU_whole.angular_velocity.z = msg.angular_velocity.z
	IMU_whole.angular_velocity_covariance = msg.angular_velocity_covariance
	rospy.loginfo("I heard the gyroscopy value (angular velocity): %f %f %f", msg.angular_velocity.x, msg.angular_velocity.y, msg.angular_velocity.z)

def callback_accel(msg):
	IMU_whole.linear_acceleration.x = msg.linear_acceleration.x
	IMU_whole.linear_acceleration.y = msg.linear_acceleration.y
	IMU_whole.linear_acceleration.z = msg.linear_acceleration.z
	IMU_whole.linear_acceleration_covariance = msg.linear_acceleration_covariance
	rospy.loginfo("I heard the accelerometer value (acceleration value): %f %f %f", msg.linear_acceleration.x, msg.linear_acceleration.y, msg.linear_acceleration.z)

if __name__ == '__main__':
	rospy.init_node('imu_sub_pub', anonymous=True)
	rospy.Subscriber("/camera/gyro/sample", Imu, callback_gyro)
	rospy.Subscriber("/camera/accel/sample", Imu, callback_accel)
	pub = rospy.Publisher('gyroscope', Imu, queue_size=10)
	rate = rospy.Rate(3) # 3hz

	while not rospy.is_shutdown():
		planning_case_str = "Read IMU data"
		rospy.loginfo(planning_case_str)
		pub.publish(IMU_whole)
		rate.sleep()

