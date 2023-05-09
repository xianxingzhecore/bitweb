
import requests
import time
import random
import fileinput
from tool import *

# https:#doc.bitbrowser.cn/api-jie-kou-wen-dang/liu-lan-qi-jie-kou


s = requests.session()
url = get_url()



def bit_proxy(id,proxy):
    if proxy == "":
        # 不设置代理
        headers = {'ids': [id],
                "ipCheckService":"ip-api",
                "proxyMethod":2,
                "proxyType":"noproxy"
                }
    else:
        proxy_temp = proxy.split(":")
        host = proxy_temp[0]
        port = proxy_temp[1]
        proxyUserName = proxy_temp[2]
        proxyPassword = proxy_temp[3]
        # 设置代理socket5
        headers = {'ids': [id],
                "ipCheckService":"ip-api",
                "proxyMethod":2,
                "proxyType":"socks5",
                "host":host,
                "port":port,
                "proxyUserName":proxyUserName,
                "proxyPassword":proxyPassword,
                }
    a = s.post(f"{url}/browser/proxy/update", json=headers).json()
    # print(a)
    # print(a['data']['list'])
    return a



if __name__ == "__main__":
    id_list = open_txt(r'input/id.txt')
    proxy_list = open_txt(r'input/proxy.txt')
    for a in range(len(id_list)):
        msg = bit_proxy(id_list[a],proxy_list[a])
        print(msg)