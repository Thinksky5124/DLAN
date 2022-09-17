'''
Author       : Thyssen Wen
Date         : 2022-09-17 16:23:38
LastEditors  : Thyssen Wen
LastEditTime : 2022-09-17 20:02:23
Description  : program start entry
FilePath     : /DLAN/main.py
'''
import argparse
# from dlam.apis.automatic_navigation import a
# from dlam.apis.planner import b
# from dlam.apis.slam import c

from dlam.utils import get_config

def parse_args():
    parser = argparse.ArgumentParser("DLAN start")
    parser.add_argument('-c',
                        '--config',
                        type=str,
                        default='configs/example.yaml',
                        help='config file path')
    parser.add_argument('-o',
                        '--override',
                        action='append',
                        default=[],
                        help='config options to be overridden')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    cfg = get_config(args.config, overrides=args.override)

if __name__ == '__main__':
    main()