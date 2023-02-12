from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from .helpers import *

def quiz(browser, metamask):
	browser.click("Start Quiz!")
	sleep(1)
	browser.driver.find_element(By.XPATH, '//div[@role="radiogroup"]/button[position()=1]').click()
	sleep(1)
	browser.click("Next Question")
	sleep(1)
	browser.driver.find_element(By.XPATH, '//div[@role="radiogroup"]/button[position()=1]').click()
	sleep(1)
	browser.click("Next Question")
	sleep(1)
	browser.driver.find_element(By.XPATH, '//div[@role="radiogroup"]/button[position()=1]').click()
	sleep(1)
	browser.click("Next Question")
	sleep(1)

def balancer_trade(layer3_window, browser, metamask):
	browser.new_tab("https://app.balancer.fi/#/arbitrum/trade")
	sleep(10)

	try:
		browser.driver.find_element(By.XPATH, '//button[contains(.,"Connect wallet")]').click()
		sleep(2)
		browser.driver.find_element(By.XPATH, '//button[contains(.,"Metamask") and contains(@class,"wallet-connect-btn")]').click()
		metamask.connect_to_website()
		sleep(3)
	except Exception as e:
		print(e)
		print("Looks like already connected to balancer")

	currencies = browser.driver.find_elements(By.XPATH, '//div[contains(@class, "token-select-input")]')
	if currencies[0].text != "ETH":
		currencies[0].click()
		sleep(6)
		token_search = browser.driver.find_element(By.XPATH, '//input[@name="tokenSearchInput"]')
		token_search.send_keys('ETH')
		sleep(2)
		token_search.send_keys(Keys.RETURN)
		sleep(2)
	if currencies[1].text != 'wstETH':
		currencies[1].click()
		sleep(2)
		token_search = browser.driver.find_element(By.XPATH, '//input[@name="tokenSearchInput"]')
		token_search.send_keys('wstETH')
		sleep(2)
		token_search.send_keys(Keys.RETURN)
		sleep(2)
	browser.driver.find_element(By.XPATH, '//input[@name="tokenIn"]').send_keys('0.0001')
	sleep(5)
	try:
		browser.driver.find_element(By.XPATH, '//button[contains(.,"Accept")]').click()
		sleep(2)
	except:
		print("No significant price change")
	browser.driver.find_element(By.XPATH, '//button[contains(.,"Preview")]').click()
	sleep(3)
	browser.driver.find_element(By.XPATH, '//button[contains(.,"Confirm swap")]').click()
	sleep(5)
	metamask.confirm_transaction()

	return_and_verify(browser, layer3_window)

def balancer_pool(layer3_window, browser, metamask):
	browser.new_tab("https://app.balancer.fi/#/arbitrum/pool/0xfb5e6d0c1dfed2ba000fbc040ab8df3615ac329c000000000000000000000159/invest")
	sleep(10)
	#0xEeee... - it's Token for ETH ()
	browser.driver.find_element(By.XPATH, '//input[@name="0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"]').send_keys('0.0001')
	sleep(2)
	browser.driver.find_element(By.XPATH, '//button[contains(.,"Preview")]').click()
	sleep(3)
	browser.driver.find_element(By.XPATH, '//button[contains(.,"Add liquidity")]').click()
	sleep(5)
	metamask.confirm_transaction()

	#stake
	browser.driver.find_element(By.XPATH, '//button[contains(.,"Stake this to earn extra")]').click()
	sleep(7)
	browser.driver.find_element(By.XPATH, '//button[contains(.,"Approve")]').click()
	sleep(5)
	metamask.confirm_token_approval()
	browser.driver.find_element(By.XPATH, '//button[contains(.,"Stake")]').click()
	sleep(5)
	metamask.confirm_transaction()

	return_and_verify(browser, layer3_window) #liquidity
	verify(browser, layer3_window) #staking

def run(browser, metamask):
	browser.go_to("https://beta.layer3.xyz/challenges/steth-on-arbitrum")
	sleep(2)
	layer3_window = browser.get_current_window_handle()

	#metamask.change_network(Network.ARBITRUM)

	quiz(browser, metamask)
	balancer_trade(layer3_window, browser, metamask)
	balancer_pool(layer3_window, browser, metamask)
	complete()
