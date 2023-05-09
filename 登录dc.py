
import time
from tool import *
from browser import *

def login_dc(driver,token):
        driver.get("https://discord.com/login")
        token = '(function() {window.t = %s;window.localStorage = document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage;window.setInterval(() => window.localStorage.token = `"${window.t}"`); window.location.reload();})();'% ('"' + token + '"')
        time.sleep(2)
        driver.execute_script(token)
        time.sleep(2)
        driver.get("https://discord.com/login")
        time.sleep(2)


if __name__ == "__main__":
    dc_list = open_txt(r'./input/dc.txt')
    id_list= open_txt(r'./input/id.txt')
    for i in range(len(id_list)) :
        dc_temp = dc_list[i].split("----")
        token = dc_temp[0]
        id = id_list[i]
        driver = open_bit(id)
        login_dc(driver,token)
