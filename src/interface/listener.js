  var txt_listener = new ROSLIB.Topic({
    ros : ros,
    name : '/txt_msg',
    messageType : 'std_msgs/String'
  });

  txt_listener.subscribe(function(m) {
    document.getElementById("msg").innerHTML = m.data;
  });
