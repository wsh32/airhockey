#include <ros.h>
#include <A4988.h>

#include "pinout.h"
#include "airhockey_firmware.h"

#define MOTOR_STEPS 200

ros::NodeHandle nh;

// configure the pins connected
int16_t striker_pos = 0;

A4988 stepper(MOTOR_STEPS, STEPPER_DIR_PIN, STEPPER_STEP_PIN, STEPPER_MS1_PIN,
              STEPPER_MS2_PIN, STEPPER_MS3_PIN);

ros::Publisher position_feedback_publisher("/arduino/feedback/striker_pos",
                                           &position_feedback_msg);
ros::Subscriber<std_msgs::Int16> position_command_subscriber(
    "/arduino/command/striker_pos", &position_command_callback);

void position_command_callback(const std_msgs::Int16& position_cmd) {
    int16_t delta_pos = position_cmd.data - striker_pos;
    striker_pos = position_cmd.data;
    stepper.rotate(delta_pos);
}

void setup() {
    // Set target motor RPM to 1RPM and microstepping to 1 (full step mode)
    stepper.begin(200, 16);
    nh.initNode();
    nh.advertise(position_feedback_publisher);
    nh.subscribe(position_command_subscriber);
}

void loop() {
    // Tell motor to rotate 360 degrees. That's it.
    position_feedback_msg.data = striker_pos;
    position_feedback_publisher.publish(&position_feedback_msg);
    nh.spinOnce();
    delay(100);
}
