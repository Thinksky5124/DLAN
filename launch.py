'''
Author       : Thyssen Wen
Date         : 2022-09-19 04:43:01
LastEditors  : Thyssen Wen
LastEditTime : 2022-09-19 08:52:13
Description  : Launch
FilePath     : /DLAN/launch.py
'''
import argparse
import sys
sys.path.append("..")
from dlan.utils import (get_config)

def parse_args():
    parser = argparse.ArgumentParser("DLAN start")
    parser.add_argument('-c',
                        '--config',
                        type=str,
                        default='configs/_base_/default_runtime.py',
                        help='config file path')
    parser.add_argument('-m',
                        '--mode',
                        type=str,
                        default='slam',
                        choices=['slam', 'plan', 'an'],
                        help='launch mode')                    
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
    if args.mode in ["slam"]:
        pass
    elif args.mode in ['plan']:
        pass
    elif args.mode in ['an']:
        pass

if __name__ == '__main__':
    main()
