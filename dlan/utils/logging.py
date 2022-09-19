'''
Author       : Thyssen Wen
Date         : 2022-09-17 16:42:06
LastEditors  : Thyssen Wen
LastEditTime : 2022-09-19 08:53:04
Description  : logging module
FilePath     : /DLAN/dlan/utils/logging.py
'''
import os
import logging as py_logging
import rclpy.logging as ros_logging
from rclpy.logging import LoggingSeverity as ROS_LoggingSeverity


logger_initialized: dict = {}

def setup_logger(name, log_dir=None, log_level='info', logging_pkg='py'):
    assert logging_pkg in ['py', 'ros']
    assert log_level in ['debug', 'info', 'warning', 'error', 'fatal']

    if logging_pkg in ['py']:
        logger = py_logging.getLogger(name)
        if log_level == 'debug':
            log_level = py_logging.DEBUG
        elif log_level == 'info':
            log_level = py_logging.INFO
        elif log_level == 'warning':
            log_level = py_logging.WARN
        elif log_level == 'error':
            log_level = py_logging.ERROR
        elif log_level == 'fatal':
            log_level = py_logging.FATAL
        # handle duplicate logs to the console
        # Starting in 1.8.0, PyTorch DDP attaches a StreamHandler <stderr> (NOTSET)
        # to the root logger. As logger.propagate is True by default, this root
        # level handler causes logging messages from rank>0 processes to
        # unexpectedly show up on the console, creating much unwanted clutter.
        # To fix this issue, we set the root logger's StreamHandler, if any, to log
        # at the ERROR level.
        for handler in logger.root.handlers:
            if type(handler) is py_logging.StreamHandler:
                handler.setLevel(py_logging.ERROR)

        stream_handler = py_logging.StreamHandler()
        handlers = [stream_handler]

        # only rank 0 will add a FileHandler
        if log_dir is not None:
            if not os.path.isabs(log_dir):
                filename = os.path.join(os.getcwd(), log_dir, name + '.log')

            # PathManager.mkdirs(os.path.dirname(filename))
            os.makedirs(os.path.dirname(filename), exist_ok=True)
        else:
            raise NotImplementedError("You should assign logging file path")

        file_handler = py_logging.FileHandler(filename, 'w')
        handlers.append(file_handler)

        formatter = py_logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        for handler in handlers:
            handler.setFormatter(formatter)
            handler.setLevel(log_level)
            logger.addHandler(handler)
            logger.setLevel(log_level)
        
        logger_initialized[name] = logger
    elif logging_pkg in ['ros']:
        logger = ros_logging.get_logger(name)
        if log_level == 'debug':
            log_level = ROS_LoggingSeverity.DEBUG
        elif log_level == 'info':
            log_level = ROS_LoggingSeverity.INFO
        elif log_level == 'warning':
            log_level = ROS_LoggingSeverity.WARN
        elif log_level == 'error':
            log_level = ROS_LoggingSeverity.ERROR
        elif log_level == 'fatal':
            log_level = ROS_LoggingSeverity.FATAL
        logger.set_level(log_level)
        logger_initialized[name] = logger

    return logger


def get_logger(name):
    if name in logger_initialized.keys():
        return logger_initialized[name]
    else:
        logger = setup_logger(name=name, log_dir=os.environ.get('ROS_LOG_DIR'))
        return logger