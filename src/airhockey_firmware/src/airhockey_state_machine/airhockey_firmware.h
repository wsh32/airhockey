#ifndef AIRHOCKEY_FIRMWARE_H
#define AIRHOCKEY_FIRMWARE_H

#include <Arduino.h>
#include <std_msgs/Int16.h>
#include <geometry_msgs/PointStamped.h>
#include <airhockey_vision/State.h>

geometry_msgs::PointStamped position_command_msg;
airhockey_vision::State position_feedback_msg;
std_msgs::Int16 striker_state_msg;

void position_command_callback(const geometry_msgs::PointStamped& position_cmd);

void setStop();
void setRun();
void setHoming();

#endif
