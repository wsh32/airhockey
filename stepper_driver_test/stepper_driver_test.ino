#include <ros.h>
#include <Arduino.h>
#include "A4988.h"
#include <std_msgs/Int16.h>

// using a 200-step motor (most common)
#define MOTOR_STEPS 200
// configure the pins connected
#define DIR 8
#define STEP 9
#define MS1 10
#define MS2 11
#define MS3 12

A4988 stepper(MOTOR_STEPS, DIR, STEP, MS1, MS2, MS3);

ros::NodeHandle  nh;

std_msgs::Int16 int_msg;
ros::Publisher chatter("striker_pos", &int_msg);

int striker_pos = 0; // TODO: incorporate into an equation to determine actual position

void setup() {
    // Set target motor RPM to 1RPM and microstepping to 1 (full step mode)
    stepper.begin(140, 1); // maximum ~250
    nh.initNode();
    nh.advertise(chatter);
}

void loop() {
    // Tell motor to rotate 360 degrees. That's it.
    stepper.rotate(360);
    int_msg.data = striker_pos;
    chatter.publish( &int_msg );
    nh.spinOnce();
    delay(2000);
    striker_pos = ++striker_pos;
}
