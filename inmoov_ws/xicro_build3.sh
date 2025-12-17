

cd ~/inmoov_ws


####################################################################
# Subsystem 3 (Head)
cp src/Xicro/xicro_pkg/config/setup_xicro_subsystem3.yaml src/Xicro/xicro_pkg/config/setup_xicro.yaml
colcon build 
#source install/setup.bash

ros2 run xicro_pkg generate_library.py -mcu_type arduino

ros2 run xicro_pkg generate_xicro_node.py -mcu_type arduino
