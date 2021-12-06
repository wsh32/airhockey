#include <ros.h>
#include <FlexyStepper.h>

#include "pinout.h"
//#include "airhockey_firmware.h"

// configure the pins connected
int16_t striker_pos = 0;

FlexyStepper x_stepper;

void setup() {
    // Set target motor RPM to 1RPM and microstepping to 1 (full step mode)
    x_stepper.connectToPins(X_STEP_PIN, X_DIR_PIN);
    x_stepper.setSpeedInStepsPerSecond(2500);
    x_stepper.setAccelerationInStepsPerSecondPerSecond(1000);

    pinMode(X_EN, OUTPUT);

}

void loop() {
    digitalWrite(X_EN, LOW);
    x_stepper.moveRelativeInSteps(-100000);
//    if (digitalRead(POWER_SW) == LOW) {
//  x_stepper.setTargetPositionRelativeInSteps(0);
//}
//    while (!x_stepper.motionComplete()) {
 //     x_stepper.processMovement();
//}  
//      delay(1000);   
//    delay(1000);
//    x_stepper.moveRelativeInSteps(-1600);
 //   x_stepper.processMovement();
//    delay(1000);
}
