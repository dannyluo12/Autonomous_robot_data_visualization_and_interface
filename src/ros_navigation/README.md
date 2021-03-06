# Autonomous Navigation Using Gazebo Simulator / RViz

## INSTALLATION ROS KINETIC & TURTLEBOT (UBUNTU 16.04)

1) sudo apt-get install ros-kinetic-desktop-full
2) sudo apt-get install ros-kinetic-turtlebot*
3) sudo apt-get install ros-kinetic-catkin python-catkin-tools 

## EXTRACT & BUILD 

1) mkdir ucsd_sim_ws
2) catkin config --extend /opt/ros/kinetic 
3) paste src folder into ucsd_sim_ws directory.
4) catkin build

## SOURCE DIRECTORY

1) echo "source ~/ucsd_sim_ws/devel/setup.bash" >> ~/.bashrc
2) source ~/.bashrc
** delete existing bashrc:  gedit ~/.bashrc

## ROSLAUNCH CODE (GMapping using RRT* Algorithm)

### 0. RUN ROSCORE 
roscore

### 1. CREATING THE MAP:

1) Launch Gazebo Simulator
roslaunch ucsd_f1tenth_gazebo mybot_test.launch

2) Launch GMapping Node
roslaunch ucsd_f1tenth_navigation gmapping_demo.launch

3) Launch RViz with GMapping Node
roslaunch ucsd_f1tenth_description mybot_rviz_gmapping.launch

4) Launch Teleop Node For Control
roslaunch ucsd_f1tenth_navigation mybot_teleop.launch

### 2. SAVING THE MAP:

1) Save map to ucsd_f1tenth_navigation directory.
rosrun map_server map_saver -f ~/ucsd_sim_ws/src/ucsd_f1tenth_navigation/maps/test_map

### 3. LOADING THE MAP:

1) Launch Gazebo Simulator
roslaunch ucsd_f1tenth_gazebo mybot_test.launch

2) Launch Completd GMapped Node
roslaunch ucsd_f1tenth_navigation amcl_demo.launch

3) Launch RViz To Start Autonomous Navigation
roslaunch ucsd_f1tenth_description mybot_rviz_amcl.launch
