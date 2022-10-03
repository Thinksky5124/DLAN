'''
Author       : Thyssen Wen
Date         : 2022-09-23 09:37:43
LastEditors  : Thyssen Wen
LastEditTime : 2022-09-23 10:00:03
Description  : Camera Sensor Class
FilePath     : /DLAN/dlan/sensor/visual/camera.py
'''
from ..builder import SENSORS
from ..base_sensor import BaseTimerSensorNode

class MonocularCamera(BaseTimerSensorNode):
    def __init__(self,
                 name: str,
                 timer_period_sec: float):
        super().__init__(name, timer_period_sec)

    def _get_image(self):
        pass

    def timer_callback(self):
        return super().timer_callback()