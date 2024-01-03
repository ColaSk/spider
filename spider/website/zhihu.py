# -*- encoding: utf-8 -*-
'''
@File    :   zhihu.py
@Time    :   2024/01/03 17:49:51
@Author  :   KaiXuan Sun (Sk)
@Version :   1.0
@Contact :   sunkaixuan@zhidemai.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
import requests
import json


def get_commercial_ecommerce(urls: list,
                             content_id: str,
                             content_type: str = 'article',
                             timeout: int = 3):
    """ 获取知乎组件链接跳转
    urls 是 知乎组件url列表 [https://xg.zhihu.com/plugin/01ed17143baff032f73ac1e0538875c5?BIZ=ECOMMERCE]
    content_id 专栏等id
    content_type 文章或回答类型 answer article
    """

    url = 'https://www.zhihu.com/api/v4/commercial/ecommerce'

    params = {
        "urls": urls,
        "type": content_type,
        "os": "other",
        "url_token": content_id
    }
    params_str = json.dumps(params)
    response = requests.post(url, data=params_str, content_type='application/json', timeout=timeout)
    return response


def get_linkcards(content_id: str,
                  content_type: str = 'answer',
                  timeout: int = 3):
    """ 获取回答等内部商品链接
    """

    url = f'https://www.zhihu.com/api/v4/mcn/v2/linkcards?content_type={content_type}&token={content_id}'
    response = requests.get(url, timeout=timeout)
    return response
