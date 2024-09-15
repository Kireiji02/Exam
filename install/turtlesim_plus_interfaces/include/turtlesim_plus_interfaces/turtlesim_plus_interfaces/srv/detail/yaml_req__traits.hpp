// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from turtlesim_plus_interfaces:srv/YamlReq.idl
// generated code does not contain a copyright notice

#ifndef TURTLESIM_PLUS_INTERFACES__SRV__DETAIL__YAML_REQ__TRAITS_HPP_
#define TURTLESIM_PLUS_INTERFACES__SRV__DETAIL__YAML_REQ__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "turtlesim_plus_interfaces/srv/detail/yaml_req__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace turtlesim_plus_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const YamlReq_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: req
  {
    out << "req: ";
    rosidl_generator_traits::value_to_yaml(msg.req, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const YamlReq_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: req
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "req: ";
    rosidl_generator_traits::value_to_yaml(msg.req, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const YamlReq_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace turtlesim_plus_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use turtlesim_plus_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const turtlesim_plus_interfaces::srv::YamlReq_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  turtlesim_plus_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use turtlesim_plus_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const turtlesim_plus_interfaces::srv::YamlReq_Request & msg)
{
  return turtlesim_plus_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<turtlesim_plus_interfaces::srv::YamlReq_Request>()
{
  return "turtlesim_plus_interfaces::srv::YamlReq_Request";
}

template<>
inline const char * name<turtlesim_plus_interfaces::srv::YamlReq_Request>()
{
  return "turtlesim_plus_interfaces/srv/YamlReq_Request";
}

template<>
struct has_fixed_size<turtlesim_plus_interfaces::srv::YamlReq_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<turtlesim_plus_interfaces::srv::YamlReq_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<turtlesim_plus_interfaces::srv::YamlReq_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace turtlesim_plus_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const YamlReq_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: res
  {
    out << "res: ";
    rosidl_generator_traits::value_to_yaml(msg.res, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const YamlReq_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: res
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "res: ";
    rosidl_generator_traits::value_to_yaml(msg.res, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const YamlReq_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace turtlesim_plus_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use turtlesim_plus_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const turtlesim_plus_interfaces::srv::YamlReq_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  turtlesim_plus_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use turtlesim_plus_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const turtlesim_plus_interfaces::srv::YamlReq_Response & msg)
{
  return turtlesim_plus_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<turtlesim_plus_interfaces::srv::YamlReq_Response>()
{
  return "turtlesim_plus_interfaces::srv::YamlReq_Response";
}

template<>
inline const char * name<turtlesim_plus_interfaces::srv::YamlReq_Response>()
{
  return "turtlesim_plus_interfaces/srv/YamlReq_Response";
}

template<>
struct has_fixed_size<turtlesim_plus_interfaces::srv::YamlReq_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<turtlesim_plus_interfaces::srv::YamlReq_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<turtlesim_plus_interfaces::srv::YamlReq_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<turtlesim_plus_interfaces::srv::YamlReq>()
{
  return "turtlesim_plus_interfaces::srv::YamlReq";
}

template<>
inline const char * name<turtlesim_plus_interfaces::srv::YamlReq>()
{
  return "turtlesim_plus_interfaces/srv/YamlReq";
}

template<>
struct has_fixed_size<turtlesim_plus_interfaces::srv::YamlReq>
  : std::integral_constant<
    bool,
    has_fixed_size<turtlesim_plus_interfaces::srv::YamlReq_Request>::value &&
    has_fixed_size<turtlesim_plus_interfaces::srv::YamlReq_Response>::value
  >
{
};

template<>
struct has_bounded_size<turtlesim_plus_interfaces::srv::YamlReq>
  : std::integral_constant<
    bool,
    has_bounded_size<turtlesim_plus_interfaces::srv::YamlReq_Request>::value &&
    has_bounded_size<turtlesim_plus_interfaces::srv::YamlReq_Response>::value
  >
{
};

template<>
struct is_service<turtlesim_plus_interfaces::srv::YamlReq>
  : std::true_type
{
};

template<>
struct is_service_request<turtlesim_plus_interfaces::srv::YamlReq_Request>
  : std::true_type
{
};

template<>
struct is_service_response<turtlesim_plus_interfaces::srv::YamlReq_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // TURTLESIM_PLUS_INTERFACES__SRV__DETAIL__YAML_REQ__TRAITS_HPP_
