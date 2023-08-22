# -*- encoding: utf-8 -*-
'''
@File    :   meituan_wap.py
@Time    :   2023/08/21 16:08:25
@Author  :   KaiXuan Sun (Sk)
@Version :   1.0
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
import requests
from common.help.str_helper import StrEn


"""
url ex: http://meishi.meituan.com/i/deal/882854832
# TODO: 位置信息存在于cookie中 cityname ci
# !!!!封禁严重
"""


def get_deal(id: str, userid: str, token: str, cookie: str):

    url = f'https://meishi.meituan.com/i/deal/{id}?userId={userid}&token={token}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
        "Cookie": cookie,
    }
    response = requests.get(url, headers=headers)
    return response.text


def get_meta(datas: str):
    """获取数据包"""
    meta = StrEn(datas).extract('window._appState = ', ';</script>')
    return meta


def get_id_by_url(url: str):
    """截取id"""
    id = StrEn(url).extract('deal/', None)
    return id
