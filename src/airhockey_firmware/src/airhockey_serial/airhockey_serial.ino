//805-325-3270 stan
#include <ros.h>
#include <FlexyStepper.h>

#include "pinout.h"
#include "airhockey_firmware.h"

//#define MOTOR_STEPS 200
FlexyStepper x_stepper;
//FlexyStepper y1_stepper;
//FlexyStepper y2_stepper;

//ros::NodeHandle nh;

// configure the pins connected
//int16_t pos; // change in position, brought in over ROS
int mode = 0; // changes state: 0 = stop, 1 = run, 2 = homing
unsigned long last_msg_time = millis() - 70000;
unsigned long last_loop = millis();
int16_t MIN_X = 0;
int16_t MAX_X = 400;
int16_t MIN_Y1 = 0;
int16_t MAX_Y1 = 400;
int16_t MIN_Y2 = 0;
int16_t MAX_Y2 = 400;
int16_t STEPS_PER_MM = 400 / (60 * 2); // 400 steps per rev / 60 teeth * 2 mm per tooth
bool newPos = false;

String input = "";
int x_pos;

//ros::Publisher position_feedback_publisher("/arduino/feedback/striker_pos",
//                                           &position_feedback_msg);
//ros::Publisher striker_state_publisher("/arduino/feedback/striker_state",
//                                          &striker_state_msg);
//                                           
//ros::Subscriber<geometry_msgs::PointStamped> position_command_subscriber(
//    "/arduino/command/striker_pos", &position_command_callback);
    

//void position_command_callback(const geometry_msgs::PointStamped& position_cmd) {
//    last_msg_time = millis();
//    x_ pos = position_cmd.point.x;
//    y_pos = position_cmd.point.y;
//}

void setup() {
    Serial.begin(115200);
    x_stepper.connectToPins(X_STEP_PIN, X_DIR_PIN);
    x_stepper.setSpeedInStepsPerSecond(2500);
    x_stepper.setAccelerationInStepsPerSecondPerSecond(2500);
//    x_stepper.setStepsPerMillimeter(STEPS_PER_MM); 
//    x_stepper.setSpeedInMillimetersPerSecond(70.0);
//    x_stepper.setAccelerationInMillimetersPerSecondPerSecond(70.0);

//    y1_stepper.connectToPins(Y1_STEP_PIN, Y1_DIR_PIN);
//    y1_stepper.setStepsPerMillimeter(STEPS_PER_MM);
//    y1_stepper.setSpeedInMillimetersPerSecond(10.0);
//    y1_stepper.setAccelerationInMillimetersPerSecondPerSecond(10.0);
//    y1_stepper.setCurrentPositionInMillimeters(0);
//
//    y2_stepper.connectToPins(Y2_STEP_PIN, Y2_DIR_PIN);
//    y2_stepper.setStepsPerMillimeter(STEPS_PER_MM);
//    y2_stepper.setSpeedInMillimetersPerSecond(10.0);
//    y2_stepper.setAccelerationInMillimetersPerSecondPerSecond(10.0);
//    y2_stepper.setCurrentPositionInMillimeters(0);

//    nh.initNode();
//    nh.advertise(position_feedback_publisher);
//    nh.advertise(striker_state_publisher);
//    nh.subscribe(position_command_subscriber);
    pinMode(POWER_SW, INPUT);
    pinMode(12, OUTPUT);
    pinMode(X_EN, OUTPUT);
    digitalWrite(X_EN, LOW);
//    digitalWrite(Y1_EN, LOW);
//    digitalWrite(Y2_EN, LOW);
    digitalWrite(POWER_CTRL, HIGH);
    
    // Breakbeam sensors
//    attachInterrupt(digitalPinToInterrupt(X_FW_BB), x_fw_bb, RISING);
//    attachInterrupt(digitalPinToInterrupt(X_BW_BB), x_bw_bb, RISING);
//    attachInterrupt(digitalPinToInterrupt(Y1_FW_BB), y1_fw_bb, RISING);
//    attachInterrupt(digitalPinToInterrupt(Y1_BW_BB), y1_bw_bb, RISING);
//    attachInterrupt(digitalPinToInterrupt(Y2_FW_BB), y2_fw_bb, RISING);
//    attachInterrupt(digitalPinToInterrupt(Y2_BW_BB), y2_bw_bb, RISING);
//    attachInterrupt(digitalPinToInterrupt(POWER_SW), setStop, FALLING);
    // EStop -- TODO: figure out which pin this is
//    attachInterrupt(digitalPinToInterrupt(), update_mode, RISING);
}


void loop() {
  unsigned long elapsed = millis() - last_msg_time;
  if(Serial.available()){
    input = Serial.readStringUntil('\n');
    // modify turn speed
    if (input[0] == 'x') {
      newPos = true;
      x_pos = (input.substring(1)).toInt();
      last_msg_time = millis();
    }
    Serial.print("got: ");
    Serial.println(input);
  }

  

    
  switch(mode){
    case 0: // stop
//      stop_mode();
        Serial.println("in stop");
        Serial.print("elapsed: ");
        Serial.println(elapsed);
        x_stepper.moveRelativeInSteps(-100);
        if (digitalRead(POWER_SW) == HIGH && elapsed < 60000) {
          Serial.println("homing time!");
          setHoming();
        }
      delay(1000);
      break;
    case 1: // run
//      run_mode();
      if (elapsed > 60000) {
        setStop(); // over a minute elapses since last message
      }

      if (newPos == true) {
        x_stepper.setTargetPositionInMillimeters(x_pos);
//        y1_stepper.setTargetPositionInMillimeters(y_pos);
//        y2_stepper.setTargetPositionInMillimeters(y_pos);
        newPos = false;
      }
      digitalWrite(X_EN, LOW);
      x_stepper.processMovement();
//      y1_stepper.processMovement();
//      y2_stepper.processMovement();
      break;
    case 2: // homing
      Serial.println("homing");
      Serial.println(digitalRead(X_BW_BB));
      x_stepper.moveToHomeInMillimeters(-1, 150.0, MAX_X - MIN_X, X_BW_BB); //x_bw_bb goes low to signify homing done
      Serial.println(digitalRead(X_BW_BB));

      Serial.println("Homing Complete");
      x_stepper.moveToPositionInMillimeters(MAX_X / 2);
      x_stepper.moveRelativeInMillimeters(-10.0);
      x_stepper.moveRelativeInMillimeters(10.0);
      Serial.println("Moved to Center");
      x_pos = MAX_X / 2;
      setRun(); // add move to center and jitter
      break;
  }
  // change so this happens once a second (20x a sec max)
  if (millis() - last_loop > 1000) {
    Serial.print("x pos ");
    Serial.println(x_stepper.getCurrentPositionInMillimeters());
    Serial.print("mode: ");
    Serial.println(mode);
//    position_feedback_msg.x_pos = x_stepper.getCurrentPositionInMillimeters();
//    position_feedback_msg.y_pos = y1_stepper.getCurrentPositionInMillimeters();
//    position_feedback_msg.x_vel = x_stepper.getCurrentVelocityInMillimetersPerSecond();
//    position_feedback_msg.y_vel = y1_stepper.getCurrentVelocityInMillimetersPerSecond();
//    striker_state_msg.data = mode;
//    
//    position_feedback_publisher.publish(&position_feedback_msg);
//    striker_state_publisher.publish(&striker_state_msg);
    last_loop = millis();
  }
//
//
//  digitalWrite(12, HIGH);
//  nh.spinOnce();
//  digitalWrite(12, LOW);
}

//void stop_mode() {
//  digitalWrite(X_EN, HIGH); // need to think about where to put these calls
//  digitalWrite(Y1_EN, HIGH);
//  digitalWrite(Y2_EN, HIGH);
//  digitalWrite(POWER_CTRL, LOW); // TODO: figure out if power supply is active high or low and control here
//}

//void run_mode() {
//
//}

//void x_fw_bb() {
//  MIN_X = x_stepper.getCurrentPositionInMillimeters();
//  pos = MIN_X;
//}
//void x_bw_bb() {
//  MAX_X = x_stepper.getCurrentPositionInMillimeters();
//  pos = MAX_X;
//}
//
//void y1_fw_bb() {
//  x_stepper.setCurrentPositionInMillimeters(MIN_Y1);
//  pos = MIN_Y1;
//}
//
//// TODO: Update these functions
//void y1_bw_bb() {
//  x_stepper.setCurrentPositionInMillimeters(MAX_Y1);
//  pos = MAX_Y1;
//}
//
//void y2_fw_bb() {
//  x_stepper.setCurrentPositionInMillimeters(MIN_Y2);
//  pos = MIN_Y2;
//}
//
//void y2_bw_bb() {
//  x_stepper.setCurrentPositionInMillimeters(MAX_Y2);
//  pos = MAX_Y2;
//}

void setStop() {
  mode = 0;
}

void setRun() {
  mode = 1;
}

void setHoming() {
  mode = 2;
}
