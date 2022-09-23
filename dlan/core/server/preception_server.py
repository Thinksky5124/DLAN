'''
Author       : Thyssen Wen
Date         : 2022-09-23 08:54:27
LastEditors  : Thyssen Wen
LastEditTime : 2022-09-23 08:57:14
Description  : Preception Server Class
FilePath     : /DLAN/dlan/core/server/preception_server.py
'''
import logging
from launch import LaunchDescription
from .action_server import ActionServer
from ..builder import SERVERS

@SERVERS.register_module()
class PreceptionServer(ActionServer):
    def __init__(self,
                 logger: logging.Logger,
                 node_list: list) -> None:
        super().__init__(logger, node_list)
    
    def run(self) -> None:
        self.ld = LaunchDescription(self.node_list)
    
    def shutdown(self) -> None:
        pass