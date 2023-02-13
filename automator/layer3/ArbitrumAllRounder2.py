from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from automator.sites import Uniswap, Hop, Balancer, Gmx
from automator import Arbitrum
from .helpers import *

def swap_on_uniswap_to_gmx(layer3_window, browser, metamask):
    browser.new_tab("https://app.uniswap.org/#/swap?inputCurrency=ETH&outputCurrency=0xfc5A1A6EB076a2C7aD06eD22C90d7E710E35ad0a")
    sleep(10)
    uniswap = Uniswap(browser, metamask)
    uniswap.try_connect()
    uniswap.execute_swap("0.00001")
    return_and_verify(browser, layer3_window)

def stake_gmx_on_gmx(layer3_window, browser, metamask):
    browser.new_tab("https://app.gmx.io/#/earn")
    sleep(10)
    gmx = Gmx(browser, metamask)
    gmx.try_connect()
    gmx.stake_gmx('0.0001')
    return_and_verify(browser, layer3_window)

def liquidity_on_hop(layer3_window, browser, metamask):
    browser.new_tab("https://app.hop.exchange/#/pool/deposit?token=ETH&sourceNetwork=arbitrum")
    sleep(10)
    hop = Hop(browser, metamask)
    hop.try_connect()

    wrap_eth_if_needed(browser, metamask, Arbitrum.NetworkName, Arbitrum.Token.WETH, '0.00002')

    hop.provide_liquidity('0.00001', 1, stake=False)
    return_and_verify(browser, layer3_window)

def liquidity_on_balancer(layer3_window, browser, metamask):
    browser.new_tab("https://app.balancer.fi/#/arbitrum/pool/0xfb5e6d0c1dfed2ba000fbc040ab8df3615ac329c000000000000000000000159/invest")
    sleep(10)
    balancer = Balancer(browser, metamask)
    balancer.try_connect()
    balancer.add_liquidity(Balancer.ETH, '0.00001', stake=True)
    return_and_verify(browser, layer3_window)
    verify(browser, layer3_window)

def liquidity_on_balancer_just_complete(layer3_window, browser, metamask):
    verify(browser, layer3_window)
    verify(browser, layer3_window)

def run(browser, metamask):
    browser.go_to("https://beta.layer3.xyz/challenges/arbitrum-all-rounder-ii")
    sleep(5)
    layer3_window = browser.get_current_window_handle()
    completed_count = completed_tasks_count(browser)

    #metamask.change_network(Arbitrum.NetworkName)

    if completed_count < 1:
        swap_on_uniswap_to_gmx(layer3_window, browser, metamask)
    if completed_count < 2:
        stake_gmx_on_gmx(layer3_window, browser, metamask)
    if completed_count < 3:
        liquidity_on_hop(layer3_window, browser, metamask)

    if completed_count < 4:
        #liquidity_on_balancer(layer3_window, browser, metamask)
        liquidity_on_balancer_just_complete(layer3_window, browser, metamask)

    sleep(10)
    if not is_quest_completed(browser):
        complete(browser, layer3_window)


