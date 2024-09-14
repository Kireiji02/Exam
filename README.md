# ROS2 Turtlesim+ Examination 1

## **Objective**
- To study the functionality of ROS2 in the following areas: Topics, Services, Parameters, Namespaces, and Launch Files.
- To enable students to design a program architecture that is both appropriate and functional.
- To help students use ROS2 as a framework for collaborative work.

## **Mission**
**Create a workspace that contains Packages for the Turtle Fun+ quest. This quest consists of 2 main parts: Teleop Turtles and Copy Turtles.**

## **Features**
-  **Teleop Keyboard Interface Control**: 
  - Direction controlled: Control the movement of "Teleop Turtle" involve with linear and angular velocity
    
  - Spawn Pizza Key: Use keyblind to drop the pizza which reffer by current postition
  - Save Path Key: Save the path from the pizza dropping position and store the data in yaml file.
  - Clear Pizza Key: Press to "eat" all the pizzas that haven't stored in yaml file (unsaved).

    _For these special keyblinds are performed to send the "flag" to "Teleop Controller" to command along thier functionality_
-  **Teleop Turtle Controller**: Receive the flag from Teleop Keyboard Interface to display the result.
    _Once the path is saved 4 times, The program won't allow you to save it more, but you still can move around or drop the pizza if it remains._
-  **Param control RQT**: Can configure the parameters through **RQT** realtime such as controller gain
  

## **Installation**

1. Create workspace
   ```bash
   mkdir ~/your_workspace
   ```
2. Clone this repository to your workspace:
   ```bash
   cd ~/your_workspace && git clone https://github.com/Kireiji02/Exam.git .
   ```
3. Build your workspace by colcon build:
   ```bash
   colcon build
   ```
4. Install keyboard and input pakages:
   ```bash
   pip install keyboard
   pip install input
   ```
5. Source the workspace:
   ```bash
   c~/your_workspace/install/setup.bash
   ```
6. Add your source command workspace into ~/.bashrc:
   ```bash
   echo "source ~/your_workspace/install/setup.bash" >> ~/.bashrc
   ```
