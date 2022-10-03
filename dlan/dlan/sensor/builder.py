'''
Author       : Thyssen Wen
Date         : 2022-09-23 09:56:33
LastEditors  : Thyssen Wen
LastEditTime : 2022-09-23 09:56:40
Description  : Sensor Builder
FilePath     : /DLAN/dlan/sensor/builder.py
'''
from dlan.utils import Registry

SENSORS = Registry('sensors')


def build_sensor(cfg):
    """Build Runner."""
    return SENSORS.build(cfg)