cmd_vel_listener = new ROSLIB.Topic({
    ros : ros,
    name : "/cmd_vel",
    messageType : 'geometry_msgs/Twist'
  });

  move = function (linear, angular) {
    var twist = new ROSLIB.Message({
      linear: {
        x: linear,
        y: 0,
        z: 0
      },
      angular: {
        x: 0,
        y: 0,
        z: angular
      }
    });
    cmd_vel_listener.publish(twist);
  }
