#include <ros.h>
#include <FlexyStepper.h>

#include "pinout.h"
#include "airhockey_firmware.h"

#define MOTOR_STEPS 200
FlexyStepper x_stepper;

ros::NodeHandle nh;

// configure the pins connected
int16_t striker_pos = 0; // x position of striker
int16_t delta_pos; // change in position, brought in over ROS

ros::Publisher position_feedback_publisher("/arduino/feedback/striker_pos",
                                           &position_feedback_msg);
ros::Subscriber<std_msgs::Int16> position_command_subscriber(
    "/arduino/command/striker_pos", &position_command_callback);
ros::Subscriber<std_msgs::Int16> striker_position_subscriber(
    "/arduino/command/striker_fb", &striker_position_callback);

void position_command_callback(const std_msgs::Int16& position_cmd) {
    delta_pos = position_cmd.data - x_stepper.getCurrentPositionInMillimeters();
    x_stepper.moveToPositionInMillimeters(delta_pos);
}

void striker_position_callback(const std_msgs::Int16& striker_cmd) {
  x_stepper.setCurrentPositionInMillimeters(striker_cmd.data);
}

void setup() {
    // Set target motor RPM to 1RPM and microstepping to 1 (full step mode)
    x_stepper.connectToPins(X_STEP_PIN, X_DIR_PIN);
//    x_stepper.setStepsPerMillimeter(25 * 1); //TODO: is this the right number of steps per mm?
    x_stepper.setSpeedInMillimetersPerSecond(10.0);
    x_stepper.setAccelerationInMillimetersPerSecondPerSecond(10.0);
    x_stepper.setCurrentPositionInMillimeters(0);

    nh.initNode();
    nh.advertise(position_feedback_publisher);
    nh.subscribe(position_command_subscriber);
}

void loop() {
  position_feedback_msg.data = x_stepper.getCurrentPositionInMillimeters();
  position_feedback_publisher.publish(&position_feedback_msg);
  nh.spinOnce();
  delay(100);
}
