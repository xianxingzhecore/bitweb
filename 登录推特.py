
import time
from tool import *
from browser import *

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
         None
def login_tw(driver,ct0,token):
        try:
            driver.switch_to.window(driver.window_handles[0])
            driver.get("https://www.twitter.com")
            time.sleep(2)
            driver.delete_all_cookies()
            driver.add_cookie({"name":"ct0","value":ct0,"domain":".twitter.com"})
            driver.add_cookie({"name":"auth_token","value":token,"domain":".twitter.com"})
            
            driver.get("https://www.twitter.com")
            time.sleep(5)
            driver.get("https://www.twitter.com")
            time.sleep(8)
        except:
             pass

if __name__ == "__main__":
    tw_list = open_txt(r'./input/tw.txt')
    id_list= open_txt(r'./input/id.txt')
    for i in range(len(id_list)) :
        tw = tw_list[i]
        tw_temp = tw.split(";")

        token = tw_temp[-1]
        ct1 = _generate_fake_ct0()
        session = requests.Session()
        ct0 = _generate_ct0(session,token,ct1)
        if ct0 != None:
            id = id_list[i]
            driver = open_bit(id)
            login_tw(driver,ct0,token)
        close_bit(id)
