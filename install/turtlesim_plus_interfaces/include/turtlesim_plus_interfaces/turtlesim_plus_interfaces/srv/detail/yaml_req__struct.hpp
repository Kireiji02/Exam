// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from turtlesim_plus_interfaces:srv/YamlReq.idl
// generated code does not contain a copyright notice

#ifndef TURTLESIM_PLUS_INTERFACES__SRV__DETAIL__YAML_REQ__STRUCT_HPP_
#define TURTLESIM_PLUS_INTERFACES__SRV__DETAIL__YAML_REQ__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__turtlesim_plus_interfaces__srv__YamlReq_Request __attribute__((deprecated))
#else
# define DEPRECATED__turtlesim_plus_interfaces__srv__YamlReq_Request __declspec(deprecated)
#endif

namespace turtlesim_plus_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct YamlReq_Request_
{
  using Type = YamlReq_Request_<ContainerAllocator>;

  explicit YamlReq_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->req = false;
    }
  }

  explicit YamlReq_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->req = false;
    }
  }

  // field types and members
  using _req_type =
    bool;
  _req_type req;

  // setters for named parameter idiom
  Type & set__req(
    const bool & _arg)
  {
    this->req = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    turtlesim_plus_interfaces::srv::YamlReq_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const turtlesim_plus_interfaces::srv::YamlReq_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<turtlesim_plus_interfaces::srv::YamlReq_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<turtlesim_plus_interfaces::srv::YamlReq_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      turtlesim_plus_interfaces::srv::YamlReq_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<turtlesim_plus_interfaces::srv::YamlReq_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      turtlesim_plus_interfaces::srv::YamlReq_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<turtlesim_plus_interfaces::srv::YamlReq_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<turtlesim_plus_interfaces::srv::YamlReq_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<turtlesim_plus_interfaces::srv::YamlReq_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__turtlesim_plus_interfaces__srv__YamlReq_Request
    std::shared_ptr<turtlesim_plus_interfaces::srv::YamlReq_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__turtlesim_plus_interfaces__srv__YamlReq_Request
    std::shared_ptr<turtlesim_plus_interfaces::srv::YamlReq_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const YamlReq_Request_ & other) const
  {
    if (this->req != other.req) {
      return false;
    }
    return true;
  }
  bool operator!=(const YamlReq_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct YamlReq_Request_

// alias to use template instance with default allocator
using YamlReq_Request =
  turtlesim_plus_interfaces::srv::YamlReq_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace turtlesim_plus_interfaces


#ifndef _WIN32
# define DEPRECATED__turtlesim_plus_interfaces__srv__YamlReq_Response __attribute__((deprecated))
#else
# define DEPRECATED__turtlesim_plus_interfaces__srv__YamlReq_Response __declspec(deprecated)
#endif

namespace turtlesim_plus_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct YamlReq_Response_
{
  using Type = YamlReq_Response_<ContainerAllocator>;

  explicit YamlReq_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->res = false;
    }
  }

  explicit YamlReq_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->res = false;
    }
  }

  // field types and members
  using _res_type =
    bool;
  _res_type res;

  // setters for named parameter idiom
  Type & set__res(
    const bool & _arg)
  {
    this->res = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    turtlesim_plus_interfaces::srv::YamlReq_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const turtlesim_plus_interfaces::srv::YamlReq_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<turtlesim_plus_interfaces::srv::YamlReq_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<turtlesim_plus_interfaces::srv::YamlReq_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      turtlesim_plus_interfaces::srv::YamlReq_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<turtlesim_plus_interfaces::srv::YamlReq_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      turtlesim_plus_interfaces::srv::YamlReq_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<turtlesim_plus_interfaces::srv::YamlReq_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<turtlesim_plus_interfaces::srv::YamlReq_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<turtlesim_plus_interfaces::srv::YamlReq_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__turtlesim_plus_interfaces__srv__YamlReq_Response
    std::shared_ptr<turtlesim_plus_interfaces::srv::YamlReq_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__turtlesim_plus_interfaces__srv__YamlReq_Response
    std::shared_ptr<turtlesim_plus_interfaces::srv::YamlReq_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const YamlReq_Response_ & other) const
  {
    if (this->res != other.res) {
      return false;
    }
    return true;
  }
  bool operator!=(const YamlReq_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct YamlReq_Response_

// alias to use template instance with default allocator
using YamlReq_Response =
  turtlesim_plus_interfaces::srv::YamlReq_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace turtlesim_plus_interfaces

namespace turtlesim_plus_interfaces
{

namespace srv
{

struct YamlReq
{
  using Request = turtlesim_plus_interfaces::srv::YamlReq_Request;
  using Response = turtlesim_plus_interfaces::srv::YamlReq_Response;
};

}  // namespace srv

}  // namespace turtlesim_plus_interfaces

#endif  // TURTLESIM_PLUS_INTERFACES__SRV__DETAIL__YAML_REQ__STRUCT_HPP_
