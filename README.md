

```
mkdir -p launch_ws/src
cd launch_ws/src
git clone https://github.com/mjcarroll/launch_parameters_example
cd ../..
```


```
colcon build
source install/setup.zsh
```


Vanilla
```
$ ros2 run py_launch_example main_node
[INFO] [1701213362.616670225] [minimal_param_node]: (Constructor) Hello world!
[INFO] [1701213363.611654226] [minimal_param_node]: (Timer) world!
```

CLI args
```
$ ros2 run py_launch_example main_node --ros-args -p arg_name:=foo
[INFO] [1701213415.656371416] [minimal_param_node]: (Constructor) Hello foo!
[INFO] [1701213416.651601786] [minimal_param_node]: (Timer) foo!
```

Launch (no args)
```
$ ros2 launch py_launch_example main.launch.py
[INFO] [launch]: All log files can be found below /home/mjcarroll/.ros/log/2023-11-28-17-18-13-882225-dalinar-101035
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [main_node-1]: process started with pid [101036]
[main_node-1] [INFO] [1701213494.117770195] [xxx.main]: (Constructor) Hello foobar!
[main_node-1] [INFO] [1701213495.112674600] [xxx.main]: (Timer) foobar!
```

Launch (args)
```
ros2 launch py_launch_example main.launch.py arg_name:=mjcarroll
[INFO] [launch]: All log files can be found below /home/mjcarroll/.ros/log/2023-11-28-17-19-06-580096-dalinar-101127
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [main_node-1]: process started with pid [101128]
[main_node-1] [INFO] [1701213546.823260468] [xxx.main]: (Constructor) Hello mjcarroll!
[main_node-1] [INFO] [1701213547.816441799] [xxx.main]: (Timer) mjcarroll!
```



