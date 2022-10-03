###
 # @Author       : Thyssen Wen
 # @Date         : 2022-09-30 08:31:01
 # @LastEditors  : Thyssen Wen
 # @LastEditTime : 2022-09-30 12:40:58
 # @Description  : Build Docker Images Only CUDA script
 # @FilePath     : /DLAN/scripts/build_docker_cuda.sh
### 

docker build -t ros2-humble-cuda:1.0 -f docker/Dockerfile.cuda .
