Assigmnent with robot simulor
==========================================================================

# Description
This project is the assignment for the teaching presentation. You can control the robot simulator using a keyboard. There is a imu above the camera box. Please have a check and complete the following assignment:

1.Write a ROS node to read the IMU message from robot simulator.
2.Draw some images to show the estimation result from sensors and compare them with the odometry information.
3.Fuse the IMU message and odometry message.

## Installing the dependencies

### Step-by-step installation
1. Create the folder and download the simulator

mkdir interview

cd interview

mkdir src

cd src

git clone https://github.com/cyb1212/interview.git

2. Open the folder and compile the toolbox

cd ..

catkin_make

3. Source the file

source /home/user_name/interview/devel/setup.bash

4. Open two terminals and run commend to open gazebo simulation

roslaunch my_robot interview.launch

rosrun teleop_twist_keyboard teleop_twist_keyboard.py

rostopic echo /imu_data

After the above steps, you should have following outputs:

![Screenshot from 2023-01-23 16-24-57](https://user-images.githubusercontent.com/32351126/213977661-84e07bed-222c-49c3-8033-968b8cde86e1.png)


## Contact
For questions, bug reports or suggestions please contact
Yongbo Chen, E-Mail: Yongbo.Chen@student.uts.edu.au 
