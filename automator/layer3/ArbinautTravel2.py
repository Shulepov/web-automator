from selenium.webdriver.common.by import By
from time import sleep
from .helpers import *

def chainhop_bridge(browser, metamask):
    metamask.change_network("Optimism")
    browser.new_tab("https://app.chainhop.exchange/swap/10/ETH/42161/ETH")
    sleep(5)
    try:
        browser.click(classname="connectWalletBtn")
    except:
        print("Looks like already connected to chainhop")

def run(browser, metamask):
    browser.go_to("https://beta.layer3.xyz/challenges/arbinaut-travels-radiant-plutusdao-and-stratos")
    sleep(5)
    layer3_window = browser.get_current_window_handle()
    completed_count = completed_tasks_count(browser)

    if completed_count < 1:
        chainhop_bridge(browser, metamask)