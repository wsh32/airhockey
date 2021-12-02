#include <ros.h>
#include <FlexyStepper.h>

#include "pinout.h"
#include "airhockey_firmware.h"

#define MOTOR_STEPS 200
FlexyStepper x_stepper;
FlexyStepper y1_stepper;
FlexyStepper y2_stepper;

ros::NodeHandle nh;

// configure the pins connected
int16_t pos; // change in position, brought in over ROS
int mode = 0; // changes state: 0 = stop, 1 = run, 2 = homing
unsigned long last_msg_time = millis();
int16_t MIN_X = 0;
int16_t MAX_X = 872;
int16_t MIN_Y1 = 0;
int16_t MAX_Y1 = 860;
int16_t MIN_Y2 = 0;
int16_t MAX_Y2 = 860;


ros::Publisher position_feedback_publisher("/arduino/feedback/striker_pos",
                                           &position_feedback_msg);
                                           
ros::Subscriber<geometry_msgs::PointStamped> position_command_subscriber(
    "/arduino/command/striker_pos", &position_command_callback);

void position_command_callback(const geometry_msgs::PointStamped& position_cmd) {
    last_msg_time = millis();
    pos = position_cmd.point.x;
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
    pinMode(POWER_SW, INPUT);
    
    // Breakbeam sensors
    attachInterrupt(digitalPinToInterrupt(X_FW_BB), x_fw_bb, RISING);
    attachInterrupt(digitalPinToInterrupt(X_BW_BB), x_bw_bb, RISING);
    attachInterrupt(digitalPinToInterrupt(Y1_FW_BB), y1_fw_bb, RISING);
    attachInterrupt(digitalPinToInterrupt(Y1_BW_BB), y1_bw_bb, RISING);
    attachInterrupt(digitalPinToInterrupt(Y2_FW_BB), y2_fw_bb, RISING);
    attachInterrupt(digitalPinToInterrupt(Y2_BW_BB), y2_bw_bb, RISING);
    // EStop -- TODO: figure out which pin this is
//    attachInterrupt(digitalPinToInterrupt(), update_mode, RISING);
}


void loop() {
  unsigned long elapsed = millis() - last_msg_time;
  nh.spinOnce();
  switch(mode){
    case 0: // stop
      stop_mode();
        if (digitalRead(POWER_SW) == HIGH && elapsed < 60000) {
          mode = 2;
        }
      delay(1000);
      break;
    case 1: // run
      run_mode();
      if (elapsed > 60000) {
        mode = 0; // over a minute elapses since last message
      }
      x_stepper.moveToPositionInMillimeters(pos);
      position_feedback_msg.data = x_stepper.getCurrentPositionInMillimeters();
      position_feedback_publisher.publish(&position_feedback_msg);
      delay(100);
      break;
    case 2: // homing
      x_stepper.moveToHomeInMillimeters(-1, 10.0, MAX_X - MIN_X, X_BW_BB);
      mode = 1; // add move to center and jitter
      break;
  }
}

void stop_mode() {
  digitalWrite(X_EN, HIGH); // need to think about where to put these calls
  digitalWrite(Y1_EN, HIGH);
  digitalWrite(Y2_EN, HIGH);
  digitalWrite(POWER_CTRL, LOW); // TODO: figure out if power supply is active high or low and control here
}

void run_mode() {
  digitalWrite(X_EN, LOW);
  digitalWrite(Y1_EN, LOW);
  digitalWrite(Y2_EN, LOW);
  digitalWrite(POWER_CTRL, HIGH);
}

void x_fw_bb() {
  x_stepper.setCurrentPositionInMillimeters(MIN_X);
  pos = MIN_X;
}
void x_bw_bb() {
  x_stepper.setCurrentPositionInMillimeters(MAX_X);
  pos = MAX_X;
}

void y1_fw_bb() {
  x_stepper.setCurrentPositionInMillimeters(MIN_Y1);
  pos = MIN_Y1;
}

void y1_bw_bb() {
  x_stepper.setCurrentPositionInMillimeters(MAX_Y1);
  pos = MAX_Y1;
}

void y2_fw_bb() {
  x_stepper.setCurrentPositionInMillimeters(MIN_Y2);
  pos = MIN_Y2;
}

void y2_bw_bb() {
  x_stepper.setCurrentPositionInMillimeters(MAX_Y2);
  pos = MAX_Y2;
}
