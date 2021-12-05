#include <ros.h>
#include <A4988.h>
#include <FlexyStepper.h>

#include "pinout.h"
#include "airhockey_firmware.h"

#define MOTOR_STEPS 200

ros::NodeHandle nh;

// configure the pins connected
int16_t striker_pos = 0;

FlexyStepper x_stepper;
FlexyStepper y_stepper1;
FlexyStepper y_stepper2;

ros::Publisher position_feedback_publisher("/arduino/feedback/striker_pos",
                                           &position_feedback_msg);
ros::Subscriber<std_msgs::Int16> position_command_subscriber(
    "/arduino/command/striker_pos", &position_command_callback);

void position_command_callback(const std_msgs::Int16& position_cmd) {
    int16_t delta_pos = position_cmd.data - striker_pos;
    striker_pos = position_cmd.data;
    x_stepper.rotate(delta_pos);
}

void setup() {
    // Set target motor RPM to 1RPM and microstepping to 1 (full step mode)
    x_stepper.connectToPins(X_STEP_PIN, X_DIR_PIN);
    x_stepper.setStepsPerMillimeter(25 * 1);
    x_stepper.setSpeedInMillimetersPerSecond(10.0);
    x_stepper.setAccelerationInMillimetersPerSecondPerSecond(10.0);

    y_stepper1.connectToPins(Y1_STEP_PIN, Y1_DIR_PIN);
    y_stepper1.setStepsPerMillimeter(25 * 1);
    y_stepper1.setSpeedInMillimetersPerSecond(10.0);
    y_stepper1.setAccelerationInMillimetersPerSecondPerSecond(10.0);

    y_stepper2.connectToPins(Y2_STEP_PIN, Y2_DIR_PIN);
    y_stepper2.setStepsPerMillimeter(25 * 1);
    y_stepper2.setSpeedInMillimetersPerSecond(10.0);
    y_stepper2.setAccelerationInMillimetersPerSecondPerSecond(10.0);
    
    nh.initNode();
    nh.advertise(position_feedback_publisher);
    nh.subscribe(position_command_subscriber);
}

void loop() {
  x_stepper.setCurrentPositionInSteps(0);

  
    // Tell motor to rotate 360 degrees. That's it.
    position_feedback_msg.data = striker_pos;
    position_feedback_publisher.publish(&position_feedback_msg);
    nh.spinOnce();
    delay(100);
}
