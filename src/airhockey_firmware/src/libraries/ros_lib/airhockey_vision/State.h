#ifndef _ROS_airhockey_vision_State_h
#define _ROS_airhockey_vision_State_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"
#include "std_msgs/Header.h"

namespace airhockey_vision
{

  class State : public ros::Msg
  {
    public:
      typedef std_msgs::Header _header_type;
      _header_type header;
      typedef float _x_pos_type;
      _x_pos_type x_pos;
      typedef float _y_pos_type;
      _y_pos_type y_pos;
      typedef float _x_vel_type;
      _x_vel_type x_vel;
      typedef float _y_vel_type;
      _y_vel_type y_vel;

    State():
      header(),
      x_pos(0),
      y_pos(0),
      x_vel(0),
      y_vel(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      offset += this->header.serialize(outbuffer + offset);
      offset += serializeAvrFloat64(outbuffer + offset, this->x_pos);
      offset += serializeAvrFloat64(outbuffer + offset, this->y_pos);
      offset += serializeAvrFloat64(outbuffer + offset, this->x_vel);
      offset += serializeAvrFloat64(outbuffer + offset, this->y_vel);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      offset += this->header.deserialize(inbuffer + offset);
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->x_pos));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->y_pos));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->x_vel));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->y_vel));
     return offset;
    }

    virtual const char * getType() override { return "airhockey_vision/State"; };
    virtual const char * getMD5() override { return "a6feb44357e1187284915a8dda3f9271"; };

  };

}
#endif
