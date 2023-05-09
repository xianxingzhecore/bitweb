
import requests
import time
import random
import fileinput
from tool import *

# https:#doc.bitbrowser.cn/api-jie-kou-wen-dang/liu-lan-qi-jie-kou


s = requests.session()
url = get_url()



def bit_list():
    headers = {'page': 0,
               "pageSize":100}
    a = s.post(f"{url}/browser/list", json=headers).json()
    # print(a)
    # print(a['data']['list'])
    return a['data']['list']



if __name__ == "__main__":
    a_list = bit_list()
    b_list = []
    for a in a_list:
        id = a['id']
        print(id)
        b_list.append(id +'\n')

    b_list=b_list[::-1]
    clear_file(r"output/id.txt")
    write_file(r"output/id.txt",b_list,'w+')