# setup ros environment
###
 # @Author       : Thyssen Wen
 # @Date         : 2022-09-30 08:03:05
 # @LastEditors  : Thyssen Wen
 # @LastEditTime : 2022-10-03 06:23:07
 # @Description  : file content
 # @FilePath     : /DLAN/docker/ros_entrypoint.sh
### 
#!/bin/bash
set -e

# setup ros2 environment
source "/opt/ros/$ROS_DISTRO/setup.bash" --
exec "$@"