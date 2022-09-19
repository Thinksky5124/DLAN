'''
Author       : Thyssen Wen
Date         : 2022-09-18 08:27:10
LastEditors  : Thyssen Wen
LastEditTime : 2022-09-19 07:13:25
Description  : Build Core
FilePath     : /DLAN/dlan/core/builder.py
'''
from dlan.utils import Registry

RUNNERS = Registry('runners')


def build_runner(cfg):
    """Build Runner."""
    return RUNNERS.build(cfg)