# -*- encoding: utf-8 -*-
'''
@File    :   sundan.py
@Time    :   2023/08/18 16:23:59
@Author  :   KaiXuan Sun (Sk)
@Version :   1.0
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib

import hashlib


def get_sign(goodsid, timestamp):
    """顺电sign生成
        function getGoodsParameter(data) {
        return {
            url: '/app/happinesswebsite/goods/goodsParameter',
            method: 'post',
            data: data,
            arr: ['goodsId']
        };
        }

        arr.forEach(function (key) {
            str += config.data[key];
        });
        str += data.timestamp;
        str += 'md5Key';
        data.sign = MD5(str);
    """
    key = 'md5Key'
    str = goodsid + timestamp + key
    md5obj = hashlib.md5(str.encode("utf-8"))
    return md5obj.hexdigest()
