# Autonomous Robots Data Visualization and Interface

This project aims to create and illustrate data visualizations for autonomous robots. In addition, interfacing and interacting with the robot via an interface will also be demonstrated in this repository. Primarily, visualizations will be done in ROS, Gazebo, and other robotics software. Visualizations will demonstrate the process in which an autnomous vehicle decides the best path to navigate. RRT* and A* algorithms are algorithms that are explored and visualized in this respective repo. Autoware simulator is also a potential building block later on. 

## Running the project
* Use the command `launch.sh -i dannyluo12/visualization_and_interface:latest -c 4 -m 8 -P Always` in order to have the necessary environment to run data processing, analysis, and visualization.

## Building the project using `run.py`
* Use the command `python run.py test` to run the visualization of RRT algorithm in test data, output images can be found in the testdata/step_out and testdata/test_out directories.

### Contributions:
<b>Yuxi Luo</b> A14862234 <br />
Contributed to developing visualizations for RRT* and A* algorithms. Collected and cleaned data from alternative groups to enable visualization and interface development. Tested different ROSBAGS for data type compatibility. Investigated various forms of visualization from different ROS topics (diff sensors, camera, lidar, etc.). Helped in managing and updating Github repo.

<b>Seokmin Hong</b> A14614169 <br />
Contributed by developing the RRT* and A* algorithms in the gazebo simulator using different ROS packages as well as writing Rviz scripts to allow autonomous navigation using these algorithms. Also downloaded and implemented the F1Tenth track in the gazebo simulator that will be used for future on-line racing. Mainly helped teammates in creating and writing the report.

<b>Jia Shi</b> A15233744 <br />
Contributed to the research of visualization and interface. Developed a interactive interface with roslibjs and webridge to connect ROS with web page. Finished the course of web visualization on Robot ignite and transfer the workspace into local machine. Helped other teams with the line detection algorithm. Helped teammates with the coding and helped with the setup and completion of github repo.
