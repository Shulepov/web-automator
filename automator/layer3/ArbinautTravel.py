from time import sleep
from automator.sites import Sushiswap
from automator.sites import Gmx
from automator import Arbitrum
from .helpers import *

def do_gmx(layer3_window, browser, metamask):
    browser.new_tab("https://app.gmx.io/#/buy_glp")
    sleep(10)
    gmx = Gmx(browser, metamask)
    gmx.try_connect()
    gmx.buy_glp('0.0001')
    return_and_verify(browser, layer3_window)

def do_sushi(layer3_window, browser, metamask):
    browser.new_tab("https://app.sushi.com/swap?inputCurrency=ETH&outputCurrency=0x539bdE0d7Dbd336b79148AA742883198BBF60342&chainId=42161")
    sleep(10)
    sushi = Sushiswap(browser, metamask)
    sushi.try_connect()
    sushi.execute_swap("0.0001")
    return_and_verify(browser, layer3_window)

def run(browser, metamask):
    browser.go_to("https://beta.layer3.xyz/challenges/arbinaut-travels-gmx-treasuredao-and-vesta")
    sleep(5)
    layer3_window = browser.get_current_window_handle()
    completed_count = completed_tasks_count(browser)

    metamask.change_network(Arbitrum.NetworkName)
    
    if completed_count < 1:
        do_gmx(layer3_window, browser, metamask)
    if completed_count < 2:
        do_sushi(layer3_window, browser, metamask)

    sleep(10)
    if not is_quest_completed(browser):
        complete(browser, layer3_window)

    



    