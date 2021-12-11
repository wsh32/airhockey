#ifndef AIRHOCKEY_FIRMWARE_H
#define AIRHOCKEY_FIRMWARE_H

#include <Arduino.h>
#include <std_msgs/Int16.h>

std_msgs::Int16 position_command_msg;
std_msgs::Int16 position_feedback_msg;

void position_command_callback(const std_msgs::Int16& position_cmd);

#endif
