# -*- encoding: utf-8 -*-
'''
@File    :   gwdang.py
@Time    :   2023/08/21 12:36:51
@Author  :   KaiXuan Sun (Sk)
@Version :   1.0
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
import requests
import time
from common.help.str_helper import StrEn
from common.help.url_helper import analysis_url_params


def taobao_url2dp(_url: str):
    """淘宝链接获取全部sku
    # 淘宝存在skuid 需要进一步转化
    # if 'tmall' in _url or 'taobao' in _url:
    """
    dps = []
    skuids = []

    dp_id = url2dp(_url)
    skuid = analysis_url_params(_url).get('skuId')

    url = f'https://www.gwdang.com/v2/trend/{dp_id}.html'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    dp_mapping = StrEn(response.text).extract('mapping=', ';')
    skuid_mapping = StrEn(response.text).extract('skuIdMapping=', ';')

    if dp_mapping and skuid_mapping:
        dp_mapping = eval(dp_mapping)
        skuid_mapping = eval(skuid_mapping)
        if skuid:
            sku_key = [key for key, sku in skuid_mapping.items() if sku == skuid][0]
            _dp_id = dp_mapping[sku_key]
            dps.append(_dp_id)
            skuids.append(skuid)
        else:
            for key, skuid in skuid_mapping.items():
                dps.append(dp_mapping[key])
                skuids.append(skuid)

    if not dps and not skuids:
        dps.append(dp_id)
        skuids.append(skuid)

    return dps, skuids


def url2dp(_url: str) -> str:
    """URL转dp"""
    ctime = int(time.time())
    url = f'https://www.gwdang.com/api/url_to_dp?url={_url}&t={ctime}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response = response.json()
    dp_id = response.get('dp_id')

    return dp_id


def get_coupon(url: str):
    """优惠券"""

    dpid = url2dp(url)

    _url = f'https://www.gwdang.com/api/coupon?dpId={dpid}'

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    response = requests.get(_url, headers=headers)
    response = response.json()
    coupon = response.get('coupon') if response.get('coupon') else 0
    return coupon


def get_dp_coupon(dp_id: str):

    url = f"https://www.gwdang.com/api/dp_coupon?dp_id={dp_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response = response.json()
    return response


def get_data(dp_id: str, coupon: str, price: int):
    """获取数据"""

    url = f'https://www.gwdang.com/trend/data_www?dp_id={dp_id}&get_coupon={coupon}&price={price}&v=2&show_prom=true'
    headers = {
        'Cookie': '__utma=188916852.1650787269.1656922104.1656922104.1656922104.1; Hm_lvt_7705e8554135f4d7b42e62562322b3ad=1692324489; fp=df00e172b83b3a2d3968939abb85e337; dfp=0H88kUZe0VJ+kUZM0H88kUZM0H82EVZM0H82kUPe0H88kUP80H88EV3+0UZi0DZ2; Hm_lpvt_7705e8554135f4d7b42e62562322b3ad=1692324523',
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    result = {}
    try:
        response = requests.get(url, headers=headers)
        result = response.json()
    except Exception as e:
        print(f"[获取数据错误]: Response: {response.text}, ERR: {e.__str__()}")
    return result
