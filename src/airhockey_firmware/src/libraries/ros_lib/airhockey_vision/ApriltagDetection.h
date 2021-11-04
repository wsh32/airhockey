#ifndef _ROS_airhockey_vision_ApriltagDetection_h
#define _ROS_airhockey_vision_ApriltagDetection_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"
#include "geometry_msgs/Point32.h"
#include "geometry_msgs/Polygon.h"

namespace airhockey_vision
{

  class ApriltagDetection : public ros::Msg
  {
    public:
      typedef const char* _tag_family_type;
      _tag_family_type tag_family;
      typedef uint8_t _tag_id_type;
      _tag_id_type tag_id;
      typedef geometry_msgs::Point32 _center_position_type;
      _center_position_type center_position;
      typedef geometry_msgs::Polygon _corner_positions_type;
      _corner_positions_type corner_positions;

    ApriltagDetection():
      tag_family(""),
      tag_id(0),
      center_position(),
      corner_positions()
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      uint32_t length_tag_family = strlen(this->tag_family);
      varToArr(outbuffer + offset, length_tag_family);
      offset += 4;
      memcpy(outbuffer + offset, this->tag_family, length_tag_family);
      offset += length_tag_family;
      *(outbuffer + offset + 0) = (this->tag_id >> (8 * 0)) & 0xFF;
      offset += sizeof(this->tag_id);
      offset += this->center_position.serialize(outbuffer + offset);
      offset += this->corner_positions.serialize(outbuffer + offset);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      uint32_t length_tag_family;
      arrToVar(length_tag_family, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_tag_family; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_tag_family-1]=0;
      this->tag_family = (char *)(inbuffer + offset-1);
      offset += length_tag_family;
      this->tag_id =  ((uint8_t) (*(inbuffer + offset)));
      offset += sizeof(this->tag_id);
      offset += this->center_position.deserialize(inbuffer + offset);
      offset += this->corner_positions.deserialize(inbuffer + offset);
     return offset;
    }

    virtual const char * getType() override { return "airhockey_vision/ApriltagDetection"; };
    virtual const char * getMD5() override { return "af2150c9592a4ada3209b09df886ce77"; };

  };

}
#endif
