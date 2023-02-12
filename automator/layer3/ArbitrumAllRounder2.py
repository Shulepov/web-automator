from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from automator.sites import Uniswap
from .helpers import *

def swap_on_uniswap(layer3_window, browser, metamask):
	browser.new_tab("https://app.uniswap.org/#/swap?inputCurrency=ETH&outputCurrency=0xfc5A1A6EB076a2C7aD06eD22C90d7E710E35ad0a&exactAmount=0.0001")
	sleep(10)
	uniswap = Uniswap(browser, metamask)
	uniswap.try_connect()
	uniswap.execute_swap("0.0001")
	return_and_verify(browser, layer3_window)

def run(browser, metamask):
	browser.go_to("https://beta.layer3.xyz/challenges/arbitrum-all-rounder-ii")
	sleep(2)
	layer3_window = browser.get_current_window_handle()

	#metamask.change_network(Network.ARBITRUM)

	swap_on_gmx(layer3_window, browser, metamask)