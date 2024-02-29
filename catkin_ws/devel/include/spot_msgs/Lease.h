// Generated by gencpp from file spot_msgs/Lease.msg
// DO NOT EDIT!


#ifndef SPOT_MSGS_MESSAGE_LEASE_H
#define SPOT_MSGS_MESSAGE_LEASE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace spot_msgs
{
template <class ContainerAllocator>
struct Lease_
{
  typedef Lease_<ContainerAllocator> Type;

  Lease_()
    : resource()
    , epoch()
    , sequence()  {
    }
  Lease_(const ContainerAllocator& _alloc)
    : resource(_alloc)
    , epoch(_alloc)
    , sequence(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _resource_type;
  _resource_type resource;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _epoch_type;
  _epoch_type epoch;

   typedef std::vector<uint32_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<uint32_t>> _sequence_type;
  _sequence_type sequence;





  typedef boost::shared_ptr< ::spot_msgs::Lease_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::spot_msgs::Lease_<ContainerAllocator> const> ConstPtr;

}; // struct Lease_

typedef ::spot_msgs::Lease_<std::allocator<void> > Lease;

typedef boost::shared_ptr< ::spot_msgs::Lease > LeasePtr;
typedef boost::shared_ptr< ::spot_msgs::Lease const> LeaseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::spot_msgs::Lease_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::spot_msgs::Lease_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::spot_msgs::Lease_<ContainerAllocator1> & lhs, const ::spot_msgs::Lease_<ContainerAllocator2> & rhs)
{
  return lhs.resource == rhs.resource &&
    lhs.epoch == rhs.epoch &&
    lhs.sequence == rhs.sequence;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::spot_msgs::Lease_<ContainerAllocator1> & lhs, const ::spot_msgs::Lease_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace spot_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::spot_msgs::Lease_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::spot_msgs::Lease_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::spot_msgs::Lease_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::spot_msgs::Lease_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::spot_msgs::Lease_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::spot_msgs::Lease_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::spot_msgs::Lease_<ContainerAllocator> >
{
  static const char* value()
  {
    return "268ed4f702e0ce57ac084653ad1ace93";
  }

  static const char* value(const ::spot_msgs::Lease_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x268ed4f702e0ce57ULL;
  static const uint64_t static_value2 = 0xac084653ad1ace93ULL;
};

template<class ContainerAllocator>
struct DataType< ::spot_msgs::Lease_<ContainerAllocator> >
{
  static const char* value()
  {
    return "spot_msgs/Lease";
  }

  static const char* value(const ::spot_msgs::Lease_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::spot_msgs::Lease_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string resource\n"
"string epoch\n"
"uint32[] sequence\n"
;
  }

  static const char* value(const ::spot_msgs::Lease_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::spot_msgs::Lease_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.resource);
      stream.next(m.epoch);
      stream.next(m.sequence);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Lease_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::spot_msgs::Lease_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::spot_msgs::Lease_<ContainerAllocator>& v)
  {
    s << indent << "resource: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.resource);
    s << indent << "epoch: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.epoch);
    s << indent << "sequence[]" << std::endl;
    for (size_t i = 0; i < v.sequence.size(); ++i)
    {
      s << indent << "  sequence[" << i << "]: ";
      Printer<uint32_t>::stream(s, indent + "  ", v.sequence[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // SPOT_MSGS_MESSAGE_LEASE_H
