import os
import requests
from tool import *

def _generate_fake_ct0() :
    """Generate the ct0 token. Used for advertising."""
    return hex(int.from_bytes(os.urandom(16), "big"))[2:]


def _generate_ct0(seesion,token,ct0):
    try:
        headers = {
            "authority": "twitter.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
        }
        cookies = {
            "auth_token": token,
            "ct0": ct0,
        }
        url = "https://twitter.com/i/release_notes"
        response = seesion.get(url, headers=headers, cookies=cookies)
        return response.cookies.get("ct0")
    except:
        return None

if __name__ == "__main__":
    clear_file(r"output/new_ac.txt")
    ac_list = open_txt(r'./input/temp.txt')
    
    for ac in ac_list:
        ac_temp = ac.split(";")
        name = ac_temp[0]
        print(name)
        token = ac_temp[-1]
        ct1 = _generate_fake_ct0()
        session = requests.Session()
        ct0 = _generate_ct0(session,token,ct1)
        if ct0 != None:
            line = "{};;;;{};{}\n".format(name,token,ct0)
            write_file(r"output/new_ac.txt",[line],'a+')
        else:
            print("{}----失败".format(name))

