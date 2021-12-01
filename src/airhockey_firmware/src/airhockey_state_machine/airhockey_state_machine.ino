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
int mode = 0; // changes state: 0 = stop, 1 = run, 2 = homing
unsigned long last_msg_time = millis();

ros::Publisher position_feedback_publisher("/arduino/feedback/striker_pos",
                                           &position_feedback_msg);
ros::Subscriber<std_msgs::Int16> position_command_subscriber(
    "/arduino/command/striker_pos", &position_command_callback);
ros::Subscriber<std_msgs::Int16> striker_position_subscriber(
    "/arduino/command/striker_fb", &striker_position_callback);

void position_command_callback(const std_msgs::Int16& position_cmd) {
    mode = 1;
    last_msg_time = millis();
    digitalWrite(X_EN, LOW); // not sure this is best place for this call
    digitalWrite(Y1_EN, LOW);
    digitalWrite(Y2_EN, LOW);
    delta_pos = position_cmd.data;
}

void striker_position_callback(const std_msgs::Int16& striker_cmd) {
  x_stepper.setCurrentPositionInMillimeters(striker_cmd.data);
}

void setup() {
    x_stepper.connectToPins(X_STEP_PIN, X_DIR_PIN);
    x_stepper.setStepsPerMillimeter(400 / (60 * 2)); // 400 steps per rev, 120 mm per rev
    x_stepper.setSpeedInMillimetersPerSecond(10.0);
    x_stepper.setAccelerationInMillimetersPerSecondPerSecond(10.0);
    x_stepper.setCurrentPositionInMillimeters(0);

    y1_stepper.connectToPins(Y1_STEP_PIN, Y1_DIR_PIN);
    y1_stepper.setStepsPerMillimeter(400 / (60 * 2)); // 400 steps per rev, 120 mm per rev
    y1_stepper.setSpeedInMillimetersPerSecond(10.0);
    y1_stepper.setAccelerationInMillimetersPerSecondPerSecond(10.0);
    y1_stepper.setCurrentPositionInMillimeters(0);

    y2_stepper.connectToPins(Y2_STEP_PIN, Y2_DIR_PIN);
    y2_stepper.setStepsPerMillimeter(400 / (60 * 2)); // 400 steps per rev, 120 mm per rev
    y2_stepper.setSpeedInMillimetersPerSecond(10.0);
    y2_stepper.setAccelerationInMillimetersPerSecondPerSecond(10.0);
    y2_stepper.setCurrentPositionInMillimeters(0);

    nh.initNode();
    nh.advertise(position_feedback_publisher);
    nh.subscribe(position_command_subscriber);

    // Breakbeam sensors
    attachInterrupt(digitalPinToInterrupt(X_FRONT_BB), stop_mode, RISING);
    attachInterrupt(digitalPinToInterrupt(X_BACK_BB), stop_mode, RISING);
    attachInterrupt(digitalPinToInterrupt(Y1_FRONT_BB), stop_mode, RISING);
    attachInterrupt(digitalPinToInterrupt(Y1_BACK_BB), stop_mode, RISING);
    attachInterrupt(digitalPinToInterrupt(Y2_FRONT_BB), stop_mode, RISING);
    attachInterrupt(digitalPinToInterrupt(Y2_BACK_BB), stop_mode, RISING);
    // EStop -- TODO: figure out which pin this is
//    attachInterrupt(digitalPinToInterrupt(), update_mode, RISING);
}


void loop() {
  switch(mode){
    case 0: // stop
      delay(1000);
      nh.spinOnce();
      break;
    case 1: // run
      unsigned long elapsed = millis() - last_msg_time;
      if (elapsed > 60000) {
        stop_mode(); // over a minute elapses since last message
      }
      x_stepper.processMovement();
      position_feedback_msg.data = x_stepper.getCurrentPositionInMillimeters();
      position_feedback_publisher.publish(&position_feedback_msg);
      nh.spinOnce(); // do we need to spin once every time?
      delay(100);
      break;
    case 2: // homing
      x_stepper.moveToPositionInMillimeters(0); // might not make sense to keep calling this
      break;
  }
    
}

void stop_mode() {
  mode = 0;
  digitalWrite(X_EN, HIGH); // need to think about where to put these calls
  digitalWrite(Y1_EN, HIGH);
  digitalWrite(Y2_EN, HIGH);
}
