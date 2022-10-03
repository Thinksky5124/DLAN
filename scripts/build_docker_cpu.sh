###
 # @Author       : Thyssen Wen
 # @Date         : 2022-09-30 08:31:01
 # @LastEditors  : Thyssen Wen
 # @LastEditTime : 2022-09-30 12:24:26
 # @Description  : Build Docker Images Only CPU script
 # @FilePath     : /DLAN/scripts/build_docker_cpu.sh
### 

docker build -t ros2-humble-cpu:1.0 -f docker/Dockerfile.cpu .