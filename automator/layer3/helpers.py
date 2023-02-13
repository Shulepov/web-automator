from time import sleep
from automator import Alchemy, network_to_alchemy_network
from automator.sites import Uniswap
from selenium.webdriver.common.by import By

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

def is_quest_completed(browser):
	try:
		browser.driver.find_element(By.XPATH, '//button[contains(text(),"Completed")]')
		return True
	except:
		return False

def completed_tasks_count(browser):
	try:
		uncompleted = browser.driver.find_element(By.XPATH, '//div[contains(@class,"c-PJLV-icSBVGD-css")]')
		completed = uncompleted.find_elements(By.XPATH, '/preceding-sibling::div')
		return len(completed)
	except:
		#if all completed
		completed = browser.driver.find_elements(By.XPATH, '//div[contains(@class,"c-PJLV-ibOGAhC-css")]')
		return len(completed)