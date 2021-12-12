#include <ros.h>
#include <AccelStepper.h>

#include "pinout.h"
#include "airhockey_firmware.h"
  
AccelStepper x_stepper(AccelStepper::DRIVER, X_STEP_PIN, X_DIR_PIN);
AccelStepper y1_stepper(AccelStepper::DRIVER, Y1_STEP_PIN, Y1_DIR_PIN);
AccelStepper y2_stepper(AccelStepper::DRIVER, Y2_STEP_PIN, Y2_DIR_PIN);

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
int16_t STEPS_PER_REV = 400;
int16_t MM_PER_REV = 60 * 2;
int16_t STEPS_PER_MM = STEPS_PER_REV / MM_PER_REV;  // 400 steps per rev / 60 teeth * 2 mm per tooth
int16_t SPEED_MM_SEC = 2000.0;
int16_t ACCEL_MM_SEC2 = 5000.0;
bool newPos = false;

float inch_to_mm = 25.4;
float x_offset_in = 2;

ros::Publisher position_feedback_publisher("/arduino/feedback/striker_pos",
                                           &position_feedback_msg);
ros::Publisher striker_state_publisher("/arduino/feedback/striker_state",
                                       &striker_state_msg);
ros::Publisher striker_command_publisher("/arduino/feedback/striker_command_mm",
                                         &striker_pos_msg);
 
ros::Subscriber<geometry_msgs::PointStamped> position_command_subscriber(
    "/arduino/command/striker_pos", &position_command_callback);
ros::Subscriber<std_msgs::Int16> speed_update_subscriber(
    "/arduino/command/set_max_speed", &speed_update_callback);
ros::Subscriber<std_msgs::Int16> acceleration_update_subscriber(
    "/arduino/command/set_acceleration", &acceleration_update_callback);
ros::Subscriber<std_msgs::Int16> state_subscriber(
    "/arduino/command/set_state", &set_state_callback);
    
int16_t clamp(int16_t input, int16_t min_val, int16_t max_val) {
    return min(max(input, min_val), max_val);
}

void position_command_callback(const geometry_msgs::PointStamped& position_cmd) {
    last_msg_time = millis();
    x_pos = clamp(position_cmd.point.x, MIN_X, MAX_X);
    newPos = true; //(new_x_pos - x_pos) > 1;
//    y_pos = position_cmd.point.y;
}

void speed_update_callback(const std_msgs::Int16& speed) {
    x_stepper.setMaxSpeed(speed.data);
}

void acceleration_update_callback(const std_msgs::Int16& acceleration) {
    x_stepper.setAcceleration(acceleration.data);
}

void set_state_callback(const std_msgs::Int16& state) {
    mode = state.data;
}

long last_sent = 0;
void publish_data() {
    last_sent = millis();
    striker_state_msg.data = mode;
    striker_state_publisher.publish(&striker_state_msg);
    striker_pos_msg.data = x_pos;
    striker_command_publisher.publish(&striker_pos_msg);
}

void setup() {
    setup_pins();

    x_stepper.setMaxSpeed(8000); //SPEED_MM_SEC * STEPS_PER_MM);
    x_stepper.setAcceleration(8000); //ACCEL_MM_SEC2 * STEPS_PER_MM);
    x_stepper.setPinsInverted(true, false, false);

    nh.initNode();
    nh.advertise(position_feedback_publisher);
    nh.advertise(striker_state_publisher);
    nh.advertise(striker_command_publisher);
    nh.subscribe(position_command_subscriber);
    nh.subscribe(speed_update_subscriber);
    nh.subscribe(acceleration_update_subscriber);
    nh.subscribe(state_subscriber);
}

long power_count = 0;

bool handle_power_switch() {
    if (digitalRead(POWER_SW) == HIGH) {
        power_count++;
    } else {
        power_count = 0;
    }

    return power_count < 10;
    // returns true if switch is on
}

void loop() {
    unsigned long elapsed = millis() - last_msg_time;

    bool switch_state = handle_power_switch();

    if (switch_state) {
        digitalWrite(POWER_CTRL, LOW);
    } else {
        digitalWrite(POWER_CTRL, HIGH);
    }

    switch(mode){
        case 0: // stop
            if (elapsed < 6000) {
                setHoming();
            } else {
                delay(100);
            }
            break;
        case 1: // run
            if (elapsed > 120000) {
                setStop(); // over two minute elapses since last message
                break;
            }
            x_stepper.moveTo(x_pos * STEPS_PER_MM);
            x_stepper.run();
            break;

        case 2: // homing
            if (homeX()) {
                setRun();
            }
            break;
    }

    // oops recovery
    if (digitalRead(X_BW_BB)) {
        x_stepper.setCurrentPosition(MIN_X);
    }

    if (millis() - last_sent > 50) {
        publish_data();
    }

    nh.spinOnce();
}

bool homeX() {
    // Returns true if homing is done, returns false if we need to call again
    if (digitalRead(X_BW_BB)) {
        x_stepper.stop();
        x_stepper.setCurrentPosition(MIN_X);
        return true;
    }

    x_stepper.move(-500); 
    x_stepper.run();
    return false;
}

void setStop() {
    digitalWrite(X_EN, HIGH);
    x_stepper.stop();
    mode = 0;
}

void setRun() {
    digitalWrite(X_EN, LOW);
    mode = 1;
}

void setHoming() {
    digitalWrite(X_EN, LOW);
    mode = 2;
}
