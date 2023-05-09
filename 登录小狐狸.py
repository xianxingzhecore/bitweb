
import time
from tool import *
from browser import *
from selenium.webdriver.common.by import By

def metamaskSetup(driver,recoveryPhrase,password):
    try:
        driver.switch_to.window(driver.window_handles[-1])
        driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/welcome")
        time.sleep(0.5)
        # driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/welcome")
        # time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,'button[data-testid="onboarding-import-wallet"]').click()
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR,'button[data-testid="metametrics-i-agree"]').click()
        time.sleep(0.5)
        # driver.find_element(By.CSS_SELECTOR,'button[data-testid="first-time-flow__button"]').click()
        # driver.find_element(By.CSS_SELECTOR,'button[data-testid="page-container-footer-next"]').click()
        # driver.find_element(By.CSS_SELECTOR,'button[data-testid="import-wallet-button"]').click()
        # driver.find_element(By.CSS_SELECTOR,'button[class="btn-primary"]').click()

        recoveryPhrases = recoveryPhrase.split(" ")
        for i in range(12):
            driver.find_element(By.CSS_SELECTOR,'input[data-testid="import-srp__srp-word-{0}"]'.format(i)).send_keys(recoveryPhrases[i])
        driver.find_element(By.CSS_SELECTOR,'button[data-testid="import-srp-confirm"]').click()
        driver.find_element(By.CSS_SELECTOR,'input[data-testid="create-password-new"]').send_keys(password)
        driver.find_element(By.CSS_SELECTOR,'input[data-testid="create-password-confirm"]').send_keys(password)

        driver.find_element(By.CSS_SELECTOR,'input[data-testid="create-password-terms"]').click()
        driver.find_element(By.CSS_SELECTOR,'.btn-primary').click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,'.btn-primary').click()
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR,'button[data-testid="pin-extension-next"]').click()
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR,'button[data-testid="pin-extension-done"]').click()
        time.sleep(3)
        print("成功登录小狐狸")

    except:
        pass


if __name__ == "__main__":
    wallet_list = open_txt(r'./input/wallet.txt')
    id_list= open_txt(r'./input/id.txt')
    pwd = input("输入要设置的密码（必须大于八位）：")
    for i in range(len(id_list)) :
        wallet_list_temp = wallet_list[i].split(";")
        recoveryPhrase = wallet_list_temp[1]
        id = id_list[i]
        driver = open_bit(id)
        metamaskSetup(driver,recoveryPhrase,pwd)
        close_bit(id)
