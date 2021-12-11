#ifndef _ROS_airhockey_vision_HomographyMatrix_h
#define _ROS_airhockey_vision_HomographyMatrix_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace airhockey_vision
{

  class HomographyMatrix : public ros::Msg
  {
    public:
      typedef float _h00_type;
      _h00_type h00;
      typedef float _h01_type;
      _h01_type h01;
      typedef float _h02_type;
      _h02_type h02;
      typedef float _h10_type;
      _h10_type h10;
      typedef float _h11_type;
      _h11_type h11;
      typedef float _h12_type;
      _h12_type h12;
      typedef float _h20_type;
      _h20_type h20;
      typedef float _h21_type;
      _h21_type h21;
      typedef float _h22_type;
      _h22_type h22;

    HomographyMatrix():
      h00(0),
      h01(0),
      h02(0),
      h10(0),
      h11(0),
      h12(0),
      h20(0),
      h21(0),
      h22(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const override
    {
      int offset = 0;
      offset += serializeAvrFloat64(outbuffer + offset, this->h00);
      offset += serializeAvrFloat64(outbuffer + offset, this->h01);
      offset += serializeAvrFloat64(outbuffer + offset, this->h02);
      offset += serializeAvrFloat64(outbuffer + offset, this->h10);
      offset += serializeAvrFloat64(outbuffer + offset, this->h11);
      offset += serializeAvrFloat64(outbuffer + offset, this->h12);
      offset += serializeAvrFloat64(outbuffer + offset, this->h20);
      offset += serializeAvrFloat64(outbuffer + offset, this->h21);
      offset += serializeAvrFloat64(outbuffer + offset, this->h22);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer) override
    {
      int offset = 0;
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->h00));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->h01));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->h02));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->h10));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->h11));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->h12));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->h20));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->h21));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->h22));
     return offset;
    }

    virtual const char * getType() override { return "airhockey_vision/HomographyMatrix"; };
    virtual const char * getMD5() override { return "62b3d04eb1c94add88fbfa899ebf6f01"; };

  };

}
#endif
