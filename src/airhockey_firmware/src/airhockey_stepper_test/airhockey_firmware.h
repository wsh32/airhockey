#ifndef AIRHOCKEY_FIRMWARE_H
#define AIRHOCKEY_FIRMWARE_H

#include <Arduino.h>
#include <std_msgs/Int16.h>
#include <geometry_msgs/PointStamped.h>

geometry_msgs::PointStamped position_command_msg;
std_msgs::Int16 position_feedback_msg;

void position_command_callback(const geometry_msgs::PointStamped& position_cmd);

#endif
