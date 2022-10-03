'''
Author       : Thyssen Wen
Date         : 2022-09-23 09:38:15
LastEditors  : Thyssen Wen
LastEditTime : 2022-09-23 10:19:57
Description  : BaseTimerSensorNode Class
FilePath     : /DLAN/dlan/sensor/base_sensor.py
'''
from abc import abstractmethod
from rclpy.node import Node

class BaseTimerSensorNode(Node):
    def __init__(self,
                 name : str,
                 timer_period_sec : float,
                 publisher_args : dict):
        super().__init__(name)
        self.publisher = self.create_publisher(**publisher_args)
        self.timer = self.create_timer(timer_period_sec, self.timer_callback)
    
    @abstractmethod
    def _get_msg(self):
        raise NotImplementedError("You Should overwrite timer_callback method!")

    def timer_callback(self):
        self.publisher.publish(self._get_msg())