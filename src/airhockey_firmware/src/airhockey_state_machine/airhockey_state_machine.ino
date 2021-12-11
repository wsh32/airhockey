#include <ros.h>
#include <FlexyStepper.h>

#include "pinout.h"
#include "airhockey_firmware.h"

FlexyStepper x_stepper;
//FlexyStepper y1_stepper;
//FlexyStepper y2_stepper;

ros::NodeHandle nh;

// configure the pins connected
int16_t x_pos; // change in position, brought in over ROS
//int16_t y_pos; 

int16_t mode = 0; // changes state: 0 = stop, 1 = run, 2 = homing

// time 
unsigned long last_msg_time = millis() - 70000;
unsigned long last_send = millis();
int16_t MIN_X = 0;
int16_t MAX_X = 872;
int16_t MIN_Y1 = 0;
int16_t MAX_Y1 = 860;
int16_t MIN_Y2 = 0;
int16_t MAX_Y2 = 860;
int16_t STEPS_PER_REV = 1600;
int16_t STEPS_PER_MM = (STEPS_PER_REV / (60 * 2)); // 400 steps per rev / 60 teeth * 2 mm per tooth
//int16_t SPEED_IN_MM = 10000.0;
//int16_t ACCEL_IN_MM = ;
bool newPos = false;

ros::Publisher position_feedback_publisher("/arduino/feedback/striker_pos",
                                           &position_feedback_msg);
ros::Publisher striker_state_publisher("/arduino/feedback/striker_state",
                                          &striker_state_msg);
                                           
ros::Subscriber<geometry_msgs::PointStamped> position_command_subscriber(
    "/arduino/command/striker_pos", &position_command_callback);
    

void position_command_callback(const geometry_msgs::PointStamped& position_cmd) {
    last_msg_time = millis();
    x_pos = position_cmd.point.x;
    newPos = true;
//    y_pos = position_cmd.point.y;
    
}

void setup() {
    x_stepper.connectToPins(X_STEP_PIN, X_DIR_PIN);
//    x_stepper.setStepsPerRevolution(STEPS_PER_REV);
    x_stepper.setStepsPerMillimeter(STEPS_PER_MM); 
    x_stepper.setSpeedInMillimetersPerSecond(10000.0);
    x_stepper.setAccelerationInMillimetersPerSecondPerSecond(10000.0);

//    y1_stepper.connectToPins(Y1_STEP_PIN, Y1_DIR_PIN);
//    y1_stepper.setStepsPerMillimeter(STEPS_PER_MM);
//    y1_stepper.setSpeedInStepsPerSecond(SPEED_IN_STEPS);
//    y1_stepper.setAccelerationInStepsPerSecondPerSecond(ACCEL_IN_STEPS);
//
//    y2_stepper.connectToPins(Y2_STEP_PIN, Y2_DIR_PIN);
//    y2_stepper.setStepsPerMillimeter(STEPS_PER_MM);
//    y2_stepper.setSpeedInStepsPerSecond(SPEED_IN_STEPS);
//    y2_stepper.setAccelerationInStepsPerSecondPerSecond(ACCEL_IN_STEPS);

    nh.initNode();
    nh.advertise(position_feedback_publisher);
    nh.advertise(striker_state_publisher);
    nh.subscribe(position_command_subscriber);
    
    pinMode(POWER_SW, INPUT);
    pinMode(X_EN, OUTPUT);
    digitalWrite(X_EN, LOW);
    digitalWrite(POWER_CTRL, HIGH);
    
//    digitalWrite(Y1_EN, LOW);
//    digitalWrite(Y2_EN, LOW);
}


void loop() {
  unsigned long elapsed = millis() - last_msg_time;
  switch(mode){
    case 0: // stop
        x_stepper.moveRelativeInSteps(-80); // bounce back and forth to indicate stop mode
        x_stepper.moveRelativeInSteps(80);
        if (digitalRead(POWER_SW) == HIGH && elapsed < 60000) {
          setHoming();
        } else {
          delay(1000);
        }
      break;
    case 1: // run
      if (elapsed > 120000) {
        setStop(); // over two minute elapses since last message
//        x_stepper.moveToPositionInMillimeters(100); // signal that we're in stop mode
      }
      if (newPos == true) {
        x_stepper.setTargetPositionInMillimeters(x_pos);
        newPos = false;
      }
      digitalWrite(X_EN, LOW);
      x_stepper.processMovement();
      break;
    case 2: // homing
      x_stepper.moveToHomeInMillimeters(-1, 250.0, MAX_X - MIN_X, X_BW_BB);
      x_stepper.moveToPositionInMillimeters(MAX_X / 2);
      x_stepper.moveRelativeInMillimeters(-50.0);
      x_stepper.moveRelativeInMillimeters(50.0);
      x_pos = MAX_X / 2;
      setRun();
      break;
  }
  // change so this happens once a second (20x a sec max)
//  if (last_send > 100) {
////    position_feedback_msg.x_pos = x_stepper.getCurrentPositionInMillimeters();
//////    position_feedback_msg.y_pos = y1_stepper.getCurrentPositionInMillimeters();
////    position_feedback_msg.x_vel = x_stepper.getCurrentVelocityInMillimetersPerSecond();
//////    position_feedback_msg.y_vel = y1_stepper.getCurrentVelocityInMillimetersPerSecond();
//    striker_state_msg.data = toInt(x_stepper.getCurrentPositionInMillimeters);
////    position_feedback_publisher.publish(&position_feedback_msg);
////    striker_state_publisher.publish(&striker_state_msg);
////    last_send = 0;
//  } else {
//    last_send ++;
//  }

  nh.spinOnce();

}

void setStop() {
  mode = 0;
}

void setRun() {
  mode = 1;
}

void setHoming() {
  mode = 2;
}
