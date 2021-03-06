# Data Visualizations and Interface for Autonomous Robots

This project aims to create data visualizations and an interactive interface for autonomous robots. The intent and design of visualizations created for this project were catered towards optimizing racing performance on the [Thunderhill track](https://www.thunderhill.com/). Visualizations include birdseye view of optimal path on mapped track, live camera feed, lidar readings, IMU data (position and orientation) visualized, battery status display, and various other visualizations to show the health and status of the vehicle. The interface that displays all of these various tools and visualizations are meant to be interactive and communicate with the Autonomous Robot via Rosbridge. The visualizations will be primarily illustrated through Python, ROS, Gazebo, RViz, and other robotics software. RRT* and A* algorithms are explored and visualized in this respective repo. Ultimately, through various testing, RRT* algorithm was decided to be the better natvigation planning algorithm. 

## Running the project
* Use the command `launch.sh -i dannyluo12/visualization_and_interface:latest -c 4 -m 8 -P Always` in order to have the necessary docker environment for creating the visualizations and genearting the interface.

## Building the project using `run.py`
* Use the command `python run.py data` to ...
* Use the command `python run.py clean` to ...
* Use the command `python run.py test` to run the visualization of RRT algorithm in test data, output images can be found in the testdata/step_out and testdata/test_out directories.
* Use the command `python run.py all` to run the visualization of RRT algorithm on cleaned data/map, output images can be found in the data/step_out and data/test_out directories.

### Contributions:
<b>Yuxi Luo</b> A14862234 <br />
Contributed to developing visualizations for RRT* and A* algorithms. Collected and cleaned data from alternative groups to enable visualization and interface development. Tested different ROSBAGS for data type compatibility. Investigated various forms of visualization from different ROS topics (diff sensors, camera, lidar, etc.). Helped in managing and updating Github repo.

<b>Seokmin Hong</b> A14614169 <br />
Contributed by developing the RRT* and A* algorithms in the gazebo simulator using different ROS packages as well as writing Rviz scripts to allow autonomous navigation using these algorithms. Also downloaded and implemented the F1Tenth track in the gazebo simulator that will be used for future on-line racing. Mainly helped teammates in creating and writing the report.

<b>Jia Shi</b> A15233744 <br />
Contributed to the research of visualization and interface. Developed a interactive interface with roslibjs and webridge to connect ROS with web page. Finished the course of web visualization on Robot ignite and transfer the workspace into local machine. Helped other teams with the line detection algorithm. Helped teammates with the coding and helped with the setup and completion of github repo.
