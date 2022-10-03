'''
Author       : Thyssen Wen
Date         : 2022-09-18 08:27:10
LastEditors  : Thyssen Wen
LastEditTime : 2022-09-23 08:55:15
Description  : Build Core
FilePath     : /DLAN/dlan/core/builder.py
'''
from dlan.utils import Registry

RUNNERS = Registry('runners')
SERVERS = Registry('server')


def build_runner(cfg):
    """Build Runner."""
    return RUNNERS.build(cfg)

def build_server(cfg):
    """Build Runner."""
    return SERVERS.build(cfg)