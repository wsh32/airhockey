#include <ros.h>
#include <Arduino.h>
#include "A4988.h"
#include <std_msgs/Int16.h>
#include <std_msgs/Empty.h>

// using a 200-step motor (most common)
#define MOTOR_STEPS 200
// configure the pins connected
#define DIR 8
#define STEP 9
#define MS1 10
#define MS2 11
#define MS3 12
int striker_pos = 0; // TODO: incorporate into an equation to determine actual position

A4988 stepper(MOTOR_STEPS, DIR, STEP, MS1, MS2, MS3);

ros::NodeHandle nh;

void messageCb( const std_msgs::Int16& toggle_msg){
    stepper.rotate(180);   // eventually cause it to rotate the desired amount to reach the x,y coords we are fed
    striker_pos = ++striker_pos;
}

std_msgs::Int16 int_msg;
ros::Publisher chatter("/arduino/striker_pos", &int_msg);
ros::Subscriber<std_msgs::Int16> sub("/arduino/track_pos", &messageCb );

void setup() {
    // Set target motor RPM to 1RPM and microstepping to 1 (full step mode)
    stepper.begin(200, 1); // maximum ~250
    nh.initNode();
    nh.advertise(chatter);
    nh.subscribe(sub);
}

void loop() {
    // Tell motor to rotate 360 degrees. That's it.
    int_msg.data = striker_pos;
    chatter.publish( &int_msg );
    nh.spinOnce();
}
