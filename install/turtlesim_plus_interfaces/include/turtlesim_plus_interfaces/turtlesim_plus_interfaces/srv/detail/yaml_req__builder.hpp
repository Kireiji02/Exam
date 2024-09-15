// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from turtlesim_plus_interfaces:srv/YamlReq.idl
// generated code does not contain a copyright notice

#ifndef TURTLESIM_PLUS_INTERFACES__SRV__DETAIL__YAML_REQ__BUILDER_HPP_
#define TURTLESIM_PLUS_INTERFACES__SRV__DETAIL__YAML_REQ__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "turtlesim_plus_interfaces/srv/detail/yaml_req__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace turtlesim_plus_interfaces
{

namespace srv
{

namespace builder
{

class Init_YamlReq_Request_req
{
public:
  Init_YamlReq_Request_req()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::turtlesim_plus_interfaces::srv::YamlReq_Request req(::turtlesim_plus_interfaces::srv::YamlReq_Request::_req_type arg)
  {
    msg_.req = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtlesim_plus_interfaces::srv::YamlReq_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtlesim_plus_interfaces::srv::YamlReq_Request>()
{
  return turtlesim_plus_interfaces::srv::builder::Init_YamlReq_Request_req();
}

}  // namespace turtlesim_plus_interfaces


namespace turtlesim_plus_interfaces
{

namespace srv
{

namespace builder
{

class Init_YamlReq_Response_res
{
public:
  Init_YamlReq_Response_res()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::turtlesim_plus_interfaces::srv::YamlReq_Response res(::turtlesim_plus_interfaces::srv::YamlReq_Response::_res_type arg)
  {
    msg_.res = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtlesim_plus_interfaces::srv::YamlReq_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtlesim_plus_interfaces::srv::YamlReq_Response>()
{
  return turtlesim_plus_interfaces::srv::builder::Init_YamlReq_Response_res();
}

}  // namespace turtlesim_plus_interfaces

#endif  // TURTLESIM_PLUS_INTERFACES__SRV__DETAIL__YAML_REQ__BUILDER_HPP_
