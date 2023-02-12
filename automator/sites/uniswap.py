from time import sleep
from selenium.webdriver.common.by import By

class Uniswap:
	def __init__(self, browser, metamask):
		self.browser = browser
		self.metamask = metamask

	def check_warnings(self):
		try:
			browser.driver.find_element(By.XPATH, '//button[contains(.,"I understand")]').click()
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
			print(e)
			print("Looks like wallet already connected to uniswap")

	def execute_swap(self, amount):
		url = self.browser.get_current_url()
		url += "&exactAmount=" + amount
		self.browser.go_to(url)
		sleep(10)
		self.browser.driver.find_element(By.ID, 'swap-button').click()
		sleep(2)
		self.browser.driver.find_element(By.ID, 'confirm-swap-or-send').click()
		sleep(10)
		self.metamask.confirm_transaction()


