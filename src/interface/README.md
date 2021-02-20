run this to launch the server first, only after this the "Connect!" button can be clicked:

1. roslaunch rosbridge_server rosbridge_websocket.launch

next: 

python3 rgb8.py is to extract image data from .bagfile (put data.bag into the same direction)

make sure to run generate_rrt_vis.py first to see nagivation demo on interface

make sure to run rosbag play [ImuFileName].bag to see IMU sensor demo
