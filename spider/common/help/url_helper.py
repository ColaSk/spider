# -*- encoding: utf-8 -*-
'''
@File    :   url_helper.py
@Time    :   2023/08/18 16:35:43
@Author  :   KaiXuan Sun (Sk)
@Version :   1.0
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib


def analysis_url_params(url: str) -> dict:
    """url params 参数解析
    xxx/xxx?a=1&b=2c=&d=4
    """
    _params = {}

    if '?' not in url:
        return _params

    params = url.split('?')[-1]
    if not params:
        return _params

    params_split = params.split('&')

    for p in params_split:
        p_ = p.split('=')
        if len(p_) != 2:
            continue
        _params[p_[0]] = p_[1]

    return _params
