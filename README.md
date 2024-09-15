ROS2 Turtlesim+ Examination 1

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
-  **Copy Turtle**: Spawn 4 turtles with the specific name to complete thier mission
  
## **System Architecture**
![archsys](https://cdn.discordapp.com/attachments/1036539347777900635/1284697389659066482/Exam_page-0003.jpg?ex=66e7932e&is=66e641ae&hm=b5949eb0102dcfbce3c77dbe325bcc8a1a10aed98306122bf7b5eb64304553fd&)

![archsys2](https://cdn.discordapp.com/attachments/1036539347777900635/1284697390095269968/Exam_page-0002.jpg?ex=66e7932e&is=66e641ae&hm=5456b609a23f2b945f4f27f2c35ae16452d758ef387550b90fce83e89074e495&)

![archsys3](https://cdn.discordapp.com/attachments/1036539347777900635/1284697390535802940/Exam_page-0001.jpg?ex=66e7932e&is=66e641ae&hm=7d6e362d8c9445556d4ec0b9ea3ad199f658a54c2bb5c47a92f6379241caa0b4&)


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
## Usage
- This package provides you `teleop_turtle.py` that control by keyboard input and 1 launch file `god_turtle.lauunch.py`. Contains with  `controller.py` use to diplay the output and compute the path, `copy_turtle.py` spawn 4 turtles to copy the path that was saved to yaml from `teleop_turtle` and distribute the position data to these turtles and `scheduler_node.py` is the node that be used to publish the state of `copy_turtle.py` that complete thier own mission and `controller_node.py` that show the status of itself (e.g pizza remaining, count of save, etc..)
- ##**Don't forget to change YAML path in copy_turtle.py to your own path**

  ### 1.) Launch the `god_turtle.lauunch.py`
   ```bash
   ros2 launch god_turtle god_turtle.lauunch.py
   ```
   ### 2.) Run the `teleop_turtle.py` to control Teleop Turtle
   ```bash
   ros2 run god_turtle teleop_turtle.py
   
   ```
   ![teleopinterface](https://cdn.discordapp.com/attachments/1024674136758431752/1284653235877056543/image.png?ex=66e76a0f&is=66e6188f&hm=e0fd3f2f76b81f614ae65281782b43b9eec0a6f1478940a08d249cb4ce99a02c&)
  ![teleopturtle](https://cdn.discordapp.com/attachments/1024674136758431752/1284654197471449229/image.png?ex=66e76af4&is=66e61974&hm=fb5cb29c398c88b7ff0a335a06185ccc4178b5531522ffeefc730841d327e92a&)

  ### 3.) Parameter Configuration
  ```bash
   rqt
   
   ```
  ![dclrprm](https://cdn.discordapp.com/attachments/1024674136758431752/1284656084103069726/image.png?ex=66e76cb6&is=66e61b36&hm=520fd17b7e996939c32fd0670ddd0232894338535e98cff2fa57d10175e3fee7&)

  ## Authors
  - Manasawin Anekvisudwong 65340500049
  - Karanyaphas Chitsuebsai 65340500065
