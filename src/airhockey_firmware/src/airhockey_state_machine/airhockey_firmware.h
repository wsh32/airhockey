#ifndef AIRHOCKEY_FIRMWARE_H
#define AIRHOCKEY_FIRMWARE_H

#include <Arduino.h>
#include <std_msgs/Int16.h>
#include <geometry_msgs/PointStamped.h>
#include <airhockey_vision/State.h>

geometry_msgs::PointStamped position_command_msg;
airhockey_vision::State position_feedback_msg;

void position_command_callback(const geometry_msgs::PointStamped& position_cmd);

void stop_mode();
void run_mode();
void x_fw_bb();
void x_bw_bb();
void y1_bw_bb();
void y1_fw_bb();
void y2_bw_bb();
void y2_fw_bb();

#endif
