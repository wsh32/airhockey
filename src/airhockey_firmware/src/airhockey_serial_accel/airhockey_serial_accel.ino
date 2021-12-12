#include <AccelStepper.h>

//805-325-3270 stan
#include <ros.h>

#include "pinout.h"
#include "airhockey_firmware.h"

//#define MOTOR_STEPS 200
AccelStepper x_stepper(1, X_STEP_PIN, X_DIR_PIN);
//FlexyStepper y1_stepper;
//FlexyStepper y2_stepper;

//ros::NodeHandle nh;

// configure the pins connected
//int16_t pos; // change in position, brought in over ROS
int mode = 0; // changes state: 0 = stop, 1 = run, 2 = homing
unsigned long last_msg_time = millis() - 70000;
unsigned long last_loop = millis();
int16_t MIN_X = 0;
int16_t MAX_X = 815; // mm
long initial_homing=-1;
int16_t STEPS_PER_REV = 1600;
int16_t STEPS_PER_MM = (STEPS_PER_REV / (60 * 2)); // 400 steps per rev / 60 teeth * 2 mm per tooth
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
    x_stepper.setMaxSpeed(20000.0 * STEPS_PER_MM);
    x_stepper.setAcceleration(20000.0 * STEPS_PER_MM);

    pinMode(POWER_SW, INPUT);
    pinMode(12, OUTPUT);
    pinMode(X_EN, OUTPUT);
    pinMode(POWER_CTRL, OUTPUT);
    digitalWrite(X_EN, LOW);
    digitalWrite(POWER_CTRL, HIGH);
}

void loop() {
  unsigned long elapsed = millis() - last_msg_time;
  bool switch_state = true; //handle_power_switch();
  if (switch_state) {
    digitalWrite(POWER_CTRL, LOW);
} else {
    digitalWrite(POWER_CTRL, HIGH);
}
  if(Serial.available()){
    input = Serial.readStringUntil('\n');
    // modify turn speed
    if (input[0] == 'x') {
      newPos = true;
      x_pos = (input.substring(1)).toInt();
      last_msg_time = millis();
    } else if (input[0] == 'h') {
      setHoming();
    }
    Serial.print("got: ");
    Serial.println(x_pos);
  }

  switch(mode){
    case 0: // stop
//      stop_mode();
        Serial.println("in stop");
        Serial.print("elapsed: ");
        Serial.println(elapsed);
//        x_stepper.moveRelativeInSteps(-150); // bounce back and forth to indicate stop mode
//        x_stepper.moveRelativeInSteps(150);
//        if (digitalRead(POWER_SW) == HIGH && elapsed < 60000) {
//          Serial.println("homing time!");
//          setHoming();
            if (switch_state && elapsed < 60000) {
                setHoming();
                Serial.println("homing time!");
            } else {
                delay(100);
            }
            break;
      delay(1000);
      break;
    case 1: // run
//      run_mode();
        if (elapsed > 120000) {
            setStop(); // over two minute elapses since last message
            break;
      if (newPos == true) {
        if (x_pos > MAX_X) {
          x_pos = MAX_X - 10;
        } else if (x_pos < MIN_X) {
          x_pos = MIN_X + 10;
        }
        x_stepper.moveTo(x_pos);
        newPos = false;
      }
      digitalWrite(X_EN, LOW);
      x_stepper.run();
      break;
    case 2: // homing
      Serial.println("homing");
      Serial.println(digitalRead(X_BW_BB));
      home_time(); //x_bw_bb goes low to signify homing done
      Serial.println(digitalRead(X_BW_BB));

      Serial.println("Homing Complete");
      x_stepper.moveToPositionInMillimeters(MAX_X / 2);
      x_stepper.moveRelativeInMillimeters(-50.0);
      x_stepper.moveRelativeInMillimeters(50.0);
      Serial.println("Moved to Center");
      x_pos = MAX_X / 2;
      setRun(); // add move to center and jitter
      break;
  }
  // change so this happens once a second (20x a sec max)
  if (millis() - last_loop > 6000) {
    Serial.print("x pos ");
    Serial.println(x_stepper.getCurrentPositionInMillimeters());
    Serial.print("mode: ");
    Serial.println(mode);
    last_loop = millis();
  }
}
}

void home_time {
  pinMode(X_BW_BB, INPUT);
  x_stepper.setMaxSpeed(100.0);
  x_stepper.setAcceleration(100.0);
  while (!digitalRead(X_BW_BB)) {
    x_stepper.moveTo(initial_homing);
    initial_homing--;
    x_stepper.run();
    delay(5);
  }
  x_stepper.setCurrentPosition(0);
  initial_homing=1;
  stepperX.setMaxSpeed(100.0);      // Set Max Speed of Stepper (Slower to get better accuracy)
  stepperX.setAcceleration(100.0);  // Set Acceleration of Stepper

  while (!digitalRead(home_switch)) { // Make the Stepper move CW until the switch is deactivated
    stepperX.moveTo(initial_homing);  
    stepperX.run();
    initial_homing++;
    delay(5);
  }
  
  stepperX.setCurrentPosition(0);
  Serial.println("Homing Completed");

  x_stepper.setMaxSpeed(20000.0 * STEPS_PER_MM);
  x_stepper.setAcceleration(20000.0 * STEPS_PER_MM);
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
