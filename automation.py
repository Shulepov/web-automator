from time import sleep

from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from automator import Browser
from automator import Metamask
import json

from automator.layer3 import Gm,ArbinautTravel,StEthArbitrum,ArbitrumAllRounder2

def get_driver(cdir, profile):
    o = webdriver.ChromeOptions()
    o.add_argument(f'--user-data-dir={cdir}')
    o.add_argument(f'--profile-directory={profile}')
    o.add_argument('--no-sandbox')
    o.add_argument("--disable-setuid-sandbox")
    o.add_argument("--disable-popup-blocking")
    return Browser(show_window=True, options=o)

print("hello")
if __name__ == '__main__':
    f = open ('config.json', "r")
    config = json.load(f)
    f.close() 

    for profile in config['chrome_profiles']:
        chrome = get_driver(config['chrome_dir'], profile)
    
        mmask = Metamask(chrome.driver, chrome)
        mmask.login(config['metamask'])
    
        Gm.run(chrome, mmask)
        ArbinautTravel.run(chrome, mmask)
        #StEthArbitrum.run(chrome, mmask)
        #ArbitrumAllRounder2.run(chrome, mmask)

        sleep(30)
        chrome.driver.quit()

    while True:
        sleep(100)