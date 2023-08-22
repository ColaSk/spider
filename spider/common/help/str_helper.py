# -*- encoding: utf-8 -*-
'''
@File    :   str_helper.py
@Time    :   2023/08/18 16:36:27
@Author  :   KaiXuan Sun (Sk)
@Version :   1.0
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
import re


class StrEn(str):
    """字符串功能增强"""

    def extract(self, start: str, end: str = None):
        """截取字符串"""

        start_mate = re.search(start, self)
        start_span = start_mate.span()

        if not start_mate:
            return

        string = self[start_span[1]:]
        end_span = (len(string), len(string))
        if end:
            end_mate = re.search(end, string)
            if not end_mate:
                return
            end_span = end_mate.span()

        return self[start_span[1]:(start_span[1] + end_span[0])]

    def extract_num_en_chchar(self):
        """提取数字、英文、汉字
        排除特殊字符
        """
        return re.sub(
            u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])",
            "",
            self)
