#ifndef AIRHOCKEY_FIRMWARE_H
#define AIRHOCKEY_FIRMWARE_H

#include <Arduino.h>
#include <std_msgs/Int16.h>
#include <geometry_msgs/PointStamped.h>
#include <airhockey_vision/State.h>

geometry_msgs::PointStamped position_command_msg;
airhockey_vision::State position_feedback_msg;
std_msgs::Int16 striker_state_msg;
std_msgs::Int16 striker_pos_msg;

void position_command_callback(const geometry_msgs::PointStamped& position_cmd);
void x_speed_update_callback(const std_msgs::Int16& xspeed);
void x_acceleration_update_callback(const std_msgs::Int16& x_acceleration);
void y_speed_update_callback(const std_msgs::Int16& yspeed);
void y_acceleration_update_callback(const std_msgs::Int16& y_acceleration);
void set_state_callback(const std_msgs::Int16& state);


void setStop();
void setRun();
void setHoming();

bool homeX();

#endif
