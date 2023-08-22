# -*- encoding: utf-8 -*-
'''
@File    :   enum_helper.py
@Time    :   2023/08/22 10:43:27
@Author  :   KaiXuan Sun (Sk)
@Version :   1.0
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib

from enum import Enum as _Enum
from typing import List
from types import DynamicClassAttribute

"""
自定义Enums类
# 增强了enums的功能
"""


# 枚举工具
class Enum(_Enum):

    __enumtag__ = {}

    @DynamicClassAttribute
    def tag_(self):
        """获取属性tag值"""
        return self.__enumtag__.get(self.name, self.name)

    @classmethod
    def tag(cls, value, default: str = '') -> str:
        """根据值获取设置的tag"""
        for _, val in enumerate(cls):
            if value == val.value:
                return cls.__enumtag__.get(val.name, val.name)
        return default

    @classmethod
    def tags(cls) -> list:
        """获取所有标签数据"""
        return [
            cls.__enumtag__.get(val.name, val.name)
            for _, val in enumerate(cls)
        ]

    @classmethod
    def values(cls) -> list:
        """获取所有枚举数据"""
        return [val.value for _, val in enumerate(cls)]

    @classmethod
    def enums(cls) -> List[dict]:
        """ 获取所有枚举属性"""

        return [{
            "name": val.name,
            "value": val.value,
            "tag": cls.__enumtag__.get(val.name, val.name)
        } for _, val in enumerate(cls)]
