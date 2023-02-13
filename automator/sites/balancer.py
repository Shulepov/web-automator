from time import sleep
from selenium.webdriver.common.by import By

class Balancer:
	def __init__(self, browser, metamask):
		self.browser = browser
		self.metamask = metamask

	def try_connect(self):
		try:
			self.browser.driver.find_element(By.XPATH, '//button[contains(.,"Connect wallet")]').click()
			sleep(2)
			self.browser.driver.find_element(By.XPATH, '//button[contains(.,"Metamask") and contains(@class,"wallet-connect-btn")]').click()
			self.metamask.connect_to_website()
			sleep(3)
		except Exception as e:
			print("Looks like already connected to balancer")

	def execute_swap(self, tokens, amount):
		currencies = self.browser.driver.find_elements(By.XPATH, '//div[contains(@class, "token-select-input")]')
		if currencies[0].text != tokens[0]:
			currencies[0].click()
			sleep(6)
			token_search = self.browser.driver.find_element(By.XPATH, '//input[@name="tokenSearchInput"]')
			token_search.send_keys(tokens[0])
			sleep(2)
			token_search.send_keys(Keys.RETURN)
			sleep(2)
		if currencies[1].text != tokens[1]:
			currencies[1].click()
			sleep(2)
			token_search = self.browser.driver.find_element(By.XPATH, '//input[@name="tokenSearchInput"]')
			token_search.send_keys(tokens[1])
			sleep(2)
			token_search.send_keys(Keys.RETURN)
			sleep(2)
		self.browser.driver.find_element(By.XPATH, '//input[@name="tokenIn"]').send_keys(amount)
		sleep(5)
		try:
			self.browser.driver.find_element(By.XPATH, '//button[contains(.,"Accept")]').click()
			sleep(2)
		except:
			print("No significant price change")
		self.browser.driver.find_element(By.XPATH, '//button[contains(.,"Preview")]').click()
		sleep(3)
		self.browser.driver.find_element(By.XPATH, '//button[contains(.,"Confirm swap")]').click()
		sleep(5)
		self.metamask.confirm_transaction()


	#ETH = 0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE
	def add_liquidity(self, token, amount):
		self.browser.driver.find_element(By.XPATH, f'//input[@name="{token}"]').send_keys(amount)
		sleep(2)
		self.browser.driver.find_element(By.XPATH, '//button[contains(.,"Preview")]').click()
		sleep(3)
		self.browser.driver.find_element(By.XPATH, '//button[contains(.,"Add liquidity")]').click()
		sleep(5)
		self.metamask.confirm_transaction()

		#stake
		self.browser.driver.find_element(By.XPATH, '//button[contains(.,"Stake this to earn extra")]').click()
		sleep(7)
		self.browser.driver.find_element(By.XPATH, '//button[contains(.,"Approve")]').click()
		sleep(5)
		self.metamask.confirm_token_approval()
		self.browser.driver.find_element(By.XPATH, '//button[contains(.,"Stake")]').click()
		sleep(5)
		self.metamask.confirm_transaction()

