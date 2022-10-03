'''
Author       : Thyssen Wen
Date         : 2022-09-18 04:05:16
LastEditors  : Thyssen Wen
LastEditTime : 2022-09-23 08:52:54
Description  : SingleRobotRunner Runner
FilePath     : /DLAN/dlan/core/runner/single_robot_runner.py
'''
import logging
from dlan.launch import LaunchDescription
from .base_runner import BaseRunner
from ..builder import RUNNERS

@RUNNERS.register_module()
class SingleRobotRunner(BaseRunner):
    def __init__(self,
                 logger: logging.Logger,
                 server_list: list) -> None:
        super().__init__(logger, server_list)
    
    def run(self) -> None:
        self.ld = LaunchDescription(self.server_list)
