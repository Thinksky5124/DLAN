'''
Author       : Thyssen Wen
Date         : 2022-09-18 04:05:16
LastEditors  : Thyssen Wen
LastEditTime : 2022-09-18 08:42:22
Description  : SingleRobotRunner Runner
FilePath     : /DLAN/dlam/core/runner/single_robot_runner.py
'''
import logging
from launch import LaunchDescription
from .base_runner import BaseRunner
from ..builder import RUNNERS

@RUNNERS.register_module()
class SingleRobotRunner(BaseRunner):
    def __init__(self,
                 logger: logging.Logger,
                 node_list: list) -> None:
        super().__init__(logger, node_list)
    
    def run(self) -> None:
        self.ld = LaunchDescription(self.node_list)
