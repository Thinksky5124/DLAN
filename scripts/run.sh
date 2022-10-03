###
 # @Author       : Thyssen Wen
 # @Date         : 2022-09-18 03:45:46
 # @LastEditors  : Thyssen Wen
 # @LastEditTime : 2022-10-03 06:16:48
 # @Description  : Run Docker Container
 # @FilePath     : /DLAN/scripts/run.sh
### 
docker run -d -it \
    -v $(pwd):/root/src \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -e DISPLAY=unix$DISPLAY \
    -e GDK_SCALE \
    -e GDK_DPI_SCALE \
    --name ros2 \
    ros2-humble-cpu:1.0