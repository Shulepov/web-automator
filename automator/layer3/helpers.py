from time import sleep
from automator import Alchemy, network_to_alchemy_network
from automator.sites import Uniswap

def verify(browser, layer3_window):
	sleep(1)
	browser.click(text="Verify")
	sleep(5)

def complete(browser, layer3_window):
	browser.click(text="Complete")

def return_and_verify(browser, layer3_window):
	browser.close_current_tab()
	browser.switch_to_window(layer3_window)
	sleep(1)
	browser.click(text="Verify")
	sleep(5)

def wrap_eth_if_needed(browser, metamask, network, weth_addr, amount):
	wallet_addr = metamask.get_wallet_address()
	alchemy = Alchemy()
	weth_balance = alchemy.get_token_balance(network_to_alchemy_network(network), wallet_addr, weth_addr)
	print(f'Current weth balance: {weth_balance}')
	if weth_balance < float(amount):
		print("Not enough weth: need to swap")
		uniswap = Uniswap(browser, metamask)
		uniswap.wrap_eth(weth_addr, amount)
		sleep(10)
		browser.driver.refresh()