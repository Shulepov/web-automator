from time import sleep
from selenium.webdriver.common.by import By

class Uniswap:
	def __init__(self, browser, metamask):
		self.browser = browser
		self.metamask = metamask

	def check_warnings(self):
		try:
			self.browser.driver.find_element(By.XPATH, '//button[text()="I understand"]').click()
			sleep(2)
		except:
			print("There weren't any warnings")

	def try_connect(self):
		self.check_warnings()
		try:
			self.browser.driver.find_element(By.XPATH, '//button[@data-testid="navbar-connect-wallet"]').click()
			sleep(2)
			self.browser.driver.find_element(By.ID, 'metamask').click()
			sleep(2)
			self.metamask.connect_to_website()
			sleep(5)
		except Exception as e:
			print("Looks like wallet already connected to uniswap")

	def execute_swap(self, amount):
		#setup slippage
		settings_btn = self.browser.driver.find_element(By.ID, 'open-settings-dialog-button')
		settings_btn.click()
		settings = self.browser.driver.find_element(By.XPATH, '//div[div[text()="Settings"]]')
		sleep(1)
		settings.find_element(By.XPATH, './/input').send_keys(1)
		sleep(1)
		settings_btn.click()

		self.browser.type(amount, classname="token-amount-input")
		sleep(7)
		self.browser.driver.find_element(By.ID, 'swap-button').click()
		sleep(2)
		self.browser.driver.find_element(By.ID, 'confirm-swap-or-send').click()
		sleep(10)
		#self.metamask.confirm_transaction()

	def wrap_eth(self, weth_addr, amount):
		prev_window = self.browser.get_current_window_handle()
		url = f'https://app.uniswap.org/#/swap?inputCurrency=ETH&outputCurrency={weth_addr}'
		self.browser.new_tab(url)
		sleep(10)
		self.try_connect()
		self.browser.type(amount, classname="token-amount-input")
		sleep(7)
		self.browser.driver.find_element(By.XPATH, '//button[text()="Wrap"]').click()
		sleep(5)
		self.metamask.confirm_transaction()
		self.browser.close_current_tab()
		self.browser.switch_to_window(prev_window)
		sleep(2)



