'''
Author       : Thyssen Wen
Date         : 2022-09-18 03:51:34
LastEditors  : Thyssen Wen
LastEditTime : 2022-09-23 08:52:43
Description  : Base Classs for Runner
FilePath     : /DLAN/dlan/core/runner/base_runner.py
'''
import abc
import logging

class BaseRunner(abc.ABC):
    """Base Runner class.
    All Runner Class should inherit it.
    Args:
        logger (logging.Logger): The logger.
        server_list (list): The ROS2 launch node list.
    """
    def __init__(self,
                 logger: logging.Logger,
                 server_list: list) -> None:
        super().__init__()
        self.logger = logger
        self.server_list = server_list
    
    @abc.abstractmethod
    def run(self) -> None:
        pass