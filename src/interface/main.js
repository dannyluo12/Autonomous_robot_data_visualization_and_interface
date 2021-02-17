// const { exec } = require("child_process");

// exec("ls -la", (error, stdout, stderr) => {
//     if (error) {
//         console.log(`error: ${error.message}`);
//         return;
//     }
//     if (stderr) {
//         console.log(`stderr: ${stderr}`);
//         return;
//     }
//     console.log(`stdout: ${stdout}`);
// });
function refresh(node)
{
   var times = 100; // gap in Milli Seconds;

   (function startRefresh()
   {
      var address;
      if(node.src.indexOf('?')>-1)
       address = node.src.split('?')[0];
      else 
       address = node.src;
      node.src = address+"?time="+new Date().getTime();

      setTimeout(startRefresh,times);
   })();

}

window.onload = function()
{
  var node = document.getElementById('img_camera');
  refresh(node);
  var node2 = document.getElementById('img_navi');
  refresh(node2);
  // you can refresh as many images you want just repeat above steps
}
let vueApp = new Vue({
    el: "#vueApp",
    data: {
        // ros connection
        ros: null,
        rosbridge_address: 'ws://localhost:9090',
        connected: false,
        // page content
        menu_title: 'Connection',
        sub_title: 'RosBridge Subscribe',
        pub_title: 'RosBridge Publish',
        camera_title: "Input from Camera",
        IMU_title: "Input from IMU",
        navi_title: "RRT Nagivation"
    },
    methods: {
        connect: function() {
            // define ROSBridge connection object
            this.ros = new ROSLIB.Ros({
                url: this.rosbridge_address
            })

            // define callbacks
            this.ros.on('connection', () => {
                this.connected = true
                console.log('Connection to ROSBridge established!')

            // subsribe to topic
            let topic = new ROSLIB.Topic({
                ros: this.ros,
                name: '/cmr_filtered/image',
                messageType: 'sensor_msgs/Image'
            })
            topic.subscribe((message) => {
                console.log(message)
            })
            let topic1 = new ROSLIB.Topic({
                ros: this.ros,
                name: '/car_1/base/odom',
                messageType: 'nav_msgs/Odometry'
            })
            topic1.subscribe((message) => {
                document.getElementById("position").innerHTML = "x: " +message.pose.pose.position.x+" y: " +message.pose.pose.position.y+" z: " +message.pose.pose.position.z;
                document.getElementById("orientation").innerHTML = "x: " +message.pose.pose.orientation.x+" y: " +message.pose.pose.orientation.y+" z: " +message.pose.pose.orientation.z;
                document.getElementById("angular").innerHTML = "x: " +message.twist.twist.angular.x+" y: " +message.twist.twist.angular.y+" z: " +message.twist.twist.angular.z;
                document.getElementById("linear").innerHTML = "x: " +message.twist.twist.linear.x+" y: " +message.twist.twist.linear.y+" z: " +message.twist.twist.linear.z;
            })
            let topic2 = new ROSLIB.Topic({
                ros: this.ros,
                name: '/imu',
                messageType: 'sensor_msgs/Imu'
            })
            topic2.subscribe((message) => {
                // console.log(message)
                document.getElementById("linear_acceleration").innerHTML = "x: " +message.linear_acceleration.x+" y: " +message.linear_acceleration.y+" z: " +message.linear_acceleration.z;
                document.getElementById("orientation_imu").innerHTML = "x: " +message.orientation.x+" y: " +message.orientation.y+" z: " +message.orientation.z;
                document.getElementById("angular_velocity").innerHTML = "x: " +message.angular_velocity.x+" y: " +message.angular_velocity.y+" z: " +message.angular_velocity.z;
                

            })

            })
            this.ros.on('error', (error) => {
                console.log('Something went wrong when trying to connect')
                console.log(error)
            })
            this.ros.on('close', () => {
                this.connected = false
                console.log('Connection to ROSBridge was closed!')
            })
        },
        disconnect: function() {
            this.ros.close()
        },
        sendCommand: function() {
            let topic = new ROSLIB.Topic({
                ros: this.ros,
                name: '/turtle1//cmd_vel',
                messageType: 'geometry_msgs/Twist'
            })
            let message = new ROSLIB.Message({
                linear: { x: 1, y: 0, z: 0, },
                angular: { x: 0, y: 0, z: 0.5, },
            })
            topic.publish(message)
            console.log(message)
        },
        turnRight: function() {
            let topic = new ROSLIB.Topic({
                ros: this.ros,
                name: '/turtle1/cmd_vel',
                messageType: 'geometry_msgs/Twist'
            })
            let message = new ROSLIB.Message({
                linear: { x: 1, y: 0, z: 0, },
                angular: { x: 0, y: 0, z: -2, },
            })
            topic.publish(message)
        },
        stop: function() {
            let topic = new ROSLIB.Topic({
                ros: this.ros,
                name: '/turtle1/cmd_vel',
                messageType: 'geometry_msgs/Twist'
            })
            let message = new ROSLIB.Message({
                linear: { x: 0, y: 0, z: 0, },
                angular: { x: 0, y: 0, z: 0, },
            })
            topic.publish(message)
        },
    },
    mounted() {
        // page is ready
        console.log('page is ready!')
    },
})