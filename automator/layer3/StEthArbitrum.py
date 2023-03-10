from selenium.webdriver.common.by import By
from time import sleep
from .helpers import *
from .quiz import do_quiz
from automator.sites import Balancer
from automator import Arbitrum

def quiz(browser, metamask):
    do_quiz(browser, [1, 1, 1])

def balancer_trade(layer3_window, browser, metamask):
    browser.new_tab("https://app.balancer.fi/#/arbitrum/trade")
    sleep(10)
    balancer = Balancer(browser, metamask)
    balancer.try_connect()
    balancer.execute_swap(["ETH", "wstETH"], "0.0001")
    return_and_verify(browser, layer3_window)

def balancer_pool(layer3_window, browser, metamask):
    browser.new_tab("https://app.balancer.fi/#/arbitrum/pool/0xfb5e6d0c1dfed2ba000fbc040ab8df3615ac329c000000000000000000000159/invest")
    sleep(10)
    balancer = Balancer(browser, metamask)
    balancer.add_liquidity("0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE", '0.0001')
    return_and_verify(browser, layer3_window) #liquidity
    verify(browser, layer3_window) #staking

def run(browser, metamask):
    browser.go_to("https://beta.layer3.xyz/challenges/steth-on-arbitrum")
    sleep(5)
    layer3_window = browser.get_current_window_handle()

    completed_count = completed_tasks_count(browser)
    #metamask.change_network(Arbitrum.NetworkName)

    if completed_count < 1:
        quiz(browser, metamask)
    if completed_count < 2:
        balancer_trade(layer3_window, browser, metamask)
    if completed_count < 3:
        balancer_pool(layer3_window, browser, metamask)
    
    if not is_quest_completed(browser):
        complete(browser, layer3_window)
