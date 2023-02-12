from time import sleep
from automator.sites import Sushiswap
from automator import Network
from .helpers import *

def do_gmx(layer3_window, browser, metamask):
	browser.new_tab("https://app.gmx.io/#/buy_glp")
	sleep(10)
	try:
		browser.click(text="Connect Wallet", classname="connect-wallet-btn")
		sleep(2)
		browser.click(text="Metamask", classname="MetaMask-btn")
		metamask.connect_to_website()
	except:
		print("Looks like wallet already connected to GMX")

	browser.type("0.0001", classname="Exchange-swap-input")
	sleep(7)
	browser.click(classname="Exchange-swap-button")
	sleep(7)
	metamask.confirm_transaction()
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
	sleep(2)
	layer3_window = browser.get_current_window_handle()

	metamask.change_network(Network.ARBITRUM)

	do_gmx(layer3_window, browser, metamask)
	do_sushi(layer3_window, browser, metamask)

	sleep(10)
	complete()

	



    