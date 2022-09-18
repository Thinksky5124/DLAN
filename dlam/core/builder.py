'''
Author       : Thyssen Wen
Date         : 2022-09-18 08:27:10
LastEditors  : Thyssen Wen
LastEditTime : 2022-09-18 08:29:31
Description  : Build Core
FilePath     : /DLAN/dlam/core/builder.py
'''
from mmcv.utils import Registry

RUNNERS = Registry('runners')


def build_runner(cfg):
    """Build Runner."""
    return RUNNERS.build(cfg)