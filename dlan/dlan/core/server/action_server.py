'''
Author       : Thyssen Wen
Date         : 2022-09-23 08:49:50
LastEditors  : Thyssen Wen
LastEditTime : 2022-09-23 08:51:29
Description  : Action Server Class
FilePath     : /DLAN/dlan/core/server/action_server.py
'''
import abc
import logging

class ActionServer(abc.ABC):
    """ActionServer class.
    All Action Server Class should inherit it.
    Args:
        logger (logging.Logger): The logger.
        node_list (list): The ROS2 launch node list.
    """
    def __init__(self,
                 logger: logging.Logger,
                 node_list: list) -> None:
        super().__init__()
        self.logger = logger
        self.node_list = node_list
    
    @abc.abstractmethod
    def run(self) -> None:
        pass

    @abc.abstractmethod
    def shutdown(self) -> None:
        pass