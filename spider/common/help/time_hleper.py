# -*- encoding: utf-8 -*-
'''
@File    :   time_hleper.py
@Time    :   2023/08/21 12:35:44
@Author  :   KaiXuan Sun (Sk)
@Version :   1.0
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
import time


def str2time(timestr: str, format: str = "%Y-%m-%d %H:%M:%S"):
    """时间字符串转时间戳"""
    time_array = time.strptime(timestr, format)
    timestamp = int(time.mktime(time_array))
    return timestamp


def times2str(times: int, format: str = "%Y-%m-%d"):
    """时间戳转字符串"""
    time_array = time.localtime(times)
    timestr = time.strftime(format, time_array)
    return timestr
