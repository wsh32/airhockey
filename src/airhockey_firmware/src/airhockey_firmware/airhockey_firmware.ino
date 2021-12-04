#include <ros.h>
#include <A4988.h>
#include <FlexyStepper.h>

#include "pinout.h"
#include "airhockey_firmware.h"

#define MOTOR_STEPS 200

// configure the pins connected
int16_t striker_pos = 0;

FlexyStepper x_stepper;

void setup() {
    // Set target motor RPM to 1RPM and microstepping to 1 (full step mode)
    x_stepper.connectToPins(X_STEP_PIN, X_DIR_PIN);
    x_stepper.setSpeedInStepsPerSecond(2000);
    x_stepper.setAccelerationInStepsPerSecondPerSecond(40000);

    pinMode(X_EN, OUTPUT);
}

void loop() {
    digitalWrite(X_EN, LOW);
    x_stepper.moveRelativeInSteps(1600);
    x_stepper.processMovement();
    delay(1000);
    x_stepper.moveRelativeInSteps(-1600);
    x_stepper.processMovement();
    delay(1000);
}
