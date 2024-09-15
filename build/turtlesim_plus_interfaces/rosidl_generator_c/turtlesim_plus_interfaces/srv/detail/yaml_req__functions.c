// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from turtlesim_plus_interfaces:srv/YamlReq.idl
// generated code does not contain a copyright notice
#include "turtlesim_plus_interfaces/srv/detail/yaml_req__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

bool
turtlesim_plus_interfaces__srv__YamlReq_Request__init(turtlesim_plus_interfaces__srv__YamlReq_Request * msg)
{
  if (!msg) {
    return false;
  }
  // req
  return true;
}

void
turtlesim_plus_interfaces__srv__YamlReq_Request__fini(turtlesim_plus_interfaces__srv__YamlReq_Request * msg)
{
  if (!msg) {
    return;
  }
  // req
}

bool
turtlesim_plus_interfaces__srv__YamlReq_Request__are_equal(const turtlesim_plus_interfaces__srv__YamlReq_Request * lhs, const turtlesim_plus_interfaces__srv__YamlReq_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // req
  if (lhs->req != rhs->req) {
    return false;
  }
  return true;
}

bool
turtlesim_plus_interfaces__srv__YamlReq_Request__copy(
  const turtlesim_plus_interfaces__srv__YamlReq_Request * input,
  turtlesim_plus_interfaces__srv__YamlReq_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // req
  output->req = input->req;
  return true;
}

turtlesim_plus_interfaces__srv__YamlReq_Request *
turtlesim_plus_interfaces__srv__YamlReq_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  turtlesim_plus_interfaces__srv__YamlReq_Request * msg = (turtlesim_plus_interfaces__srv__YamlReq_Request *)allocator.allocate(sizeof(turtlesim_plus_interfaces__srv__YamlReq_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(turtlesim_plus_interfaces__srv__YamlReq_Request));
  bool success = turtlesim_plus_interfaces__srv__YamlReq_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
turtlesim_plus_interfaces__srv__YamlReq_Request__destroy(turtlesim_plus_interfaces__srv__YamlReq_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    turtlesim_plus_interfaces__srv__YamlReq_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
turtlesim_plus_interfaces__srv__YamlReq_Request__Sequence__init(turtlesim_plus_interfaces__srv__YamlReq_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  turtlesim_plus_interfaces__srv__YamlReq_Request * data = NULL;

  if (size) {
    data = (turtlesim_plus_interfaces__srv__YamlReq_Request *)allocator.zero_allocate(size, sizeof(turtlesim_plus_interfaces__srv__YamlReq_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = turtlesim_plus_interfaces__srv__YamlReq_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        turtlesim_plus_interfaces__srv__YamlReq_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
turtlesim_plus_interfaces__srv__YamlReq_Request__Sequence__fini(turtlesim_plus_interfaces__srv__YamlReq_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      turtlesim_plus_interfaces__srv__YamlReq_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

turtlesim_plus_interfaces__srv__YamlReq_Request__Sequence *
turtlesim_plus_interfaces__srv__YamlReq_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  turtlesim_plus_interfaces__srv__YamlReq_Request__Sequence * array = (turtlesim_plus_interfaces__srv__YamlReq_Request__Sequence *)allocator.allocate(sizeof(turtlesim_plus_interfaces__srv__YamlReq_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = turtlesim_plus_interfaces__srv__YamlReq_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
turtlesim_plus_interfaces__srv__YamlReq_Request__Sequence__destroy(turtlesim_plus_interfaces__srv__YamlReq_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    turtlesim_plus_interfaces__srv__YamlReq_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
turtlesim_plus_interfaces__srv__YamlReq_Request__Sequence__are_equal(const turtlesim_plus_interfaces__srv__YamlReq_Request__Sequence * lhs, const turtlesim_plus_interfaces__srv__YamlReq_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!turtlesim_plus_interfaces__srv__YamlReq_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
turtlesim_plus_interfaces__srv__YamlReq_Request__Sequence__copy(
  const turtlesim_plus_interfaces__srv__YamlReq_Request__Sequence * input,
  turtlesim_plus_interfaces__srv__YamlReq_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(turtlesim_plus_interfaces__srv__YamlReq_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    turtlesim_plus_interfaces__srv__YamlReq_Request * data =
      (turtlesim_plus_interfaces__srv__YamlReq_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!turtlesim_plus_interfaces__srv__YamlReq_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          turtlesim_plus_interfaces__srv__YamlReq_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!turtlesim_plus_interfaces__srv__YamlReq_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
turtlesim_plus_interfaces__srv__YamlReq_Response__init(turtlesim_plus_interfaces__srv__YamlReq_Response * msg)
{
  if (!msg) {
    return false;
  }
  // res
  return true;
}

void
turtlesim_plus_interfaces__srv__YamlReq_Response__fini(turtlesim_plus_interfaces__srv__YamlReq_Response * msg)
{
  if (!msg) {
    return;
  }
  // res
}

bool
turtlesim_plus_interfaces__srv__YamlReq_Response__are_equal(const turtlesim_plus_interfaces__srv__YamlReq_Response * lhs, const turtlesim_plus_interfaces__srv__YamlReq_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // res
  if (lhs->res != rhs->res) {
    return false;
  }
  return true;
}

bool
turtlesim_plus_interfaces__srv__YamlReq_Response__copy(
  const turtlesim_plus_interfaces__srv__YamlReq_Response * input,
  turtlesim_plus_interfaces__srv__YamlReq_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // res
  output->res = input->res;
  return true;
}

turtlesim_plus_interfaces__srv__YamlReq_Response *
turtlesim_plus_interfaces__srv__YamlReq_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  turtlesim_plus_interfaces__srv__YamlReq_Response * msg = (turtlesim_plus_interfaces__srv__YamlReq_Response *)allocator.allocate(sizeof(turtlesim_plus_interfaces__srv__YamlReq_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(turtlesim_plus_interfaces__srv__YamlReq_Response));
  bool success = turtlesim_plus_interfaces__srv__YamlReq_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
turtlesim_plus_interfaces__srv__YamlReq_Response__destroy(turtlesim_plus_interfaces__srv__YamlReq_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    turtlesim_plus_interfaces__srv__YamlReq_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
turtlesim_plus_interfaces__srv__YamlReq_Response__Sequence__init(turtlesim_plus_interfaces__srv__YamlReq_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  turtlesim_plus_interfaces__srv__YamlReq_Response * data = NULL;

  if (size) {
    data = (turtlesim_plus_interfaces__srv__YamlReq_Response *)allocator.zero_allocate(size, sizeof(turtlesim_plus_interfaces__srv__YamlReq_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = turtlesim_plus_interfaces__srv__YamlReq_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        turtlesim_plus_interfaces__srv__YamlReq_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
turtlesim_plus_interfaces__srv__YamlReq_Response__Sequence__fini(turtlesim_plus_interfaces__srv__YamlReq_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      turtlesim_plus_interfaces__srv__YamlReq_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

turtlesim_plus_interfaces__srv__YamlReq_Response__Sequence *
turtlesim_plus_interfaces__srv__YamlReq_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  turtlesim_plus_interfaces__srv__YamlReq_Response__Sequence * array = (turtlesim_plus_interfaces__srv__YamlReq_Response__Sequence *)allocator.allocate(sizeof(turtlesim_plus_interfaces__srv__YamlReq_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = turtlesim_plus_interfaces__srv__YamlReq_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
turtlesim_plus_interfaces__srv__YamlReq_Response__Sequence__destroy(turtlesim_plus_interfaces__srv__YamlReq_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    turtlesim_plus_interfaces__srv__YamlReq_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
turtlesim_plus_interfaces__srv__YamlReq_Response__Sequence__are_equal(const turtlesim_plus_interfaces__srv__YamlReq_Response__Sequence * lhs, const turtlesim_plus_interfaces__srv__YamlReq_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!turtlesim_plus_interfaces__srv__YamlReq_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
turtlesim_plus_interfaces__srv__YamlReq_Response__Sequence__copy(
  const turtlesim_plus_interfaces__srv__YamlReq_Response__Sequence * input,
  turtlesim_plus_interfaces__srv__YamlReq_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(turtlesim_plus_interfaces__srv__YamlReq_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    turtlesim_plus_interfaces__srv__YamlReq_Response * data =
      (turtlesim_plus_interfaces__srv__YamlReq_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!turtlesim_plus_interfaces__srv__YamlReq_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          turtlesim_plus_interfaces__srv__YamlReq_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!turtlesim_plus_interfaces__srv__YamlReq_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
