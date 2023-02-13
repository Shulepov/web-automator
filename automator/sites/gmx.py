from time import sleep
from selenium.webdriver.common.by import By

class Gmx:
	def __init__(self, browser, metamask):
		self.browser = browser
		self.metamask = metamask

	def try_connect(self):
		try:
			self.browser.click(text="Connect Wallet", classname="connect-wallet-btn")
			sleep(2)
			self.browser.click(text="Metamask", classname="MetaMask-btn")
			self.metamask.connect_to_website()
		except:
			print("Looks like wallet already connected to GMX")

	def buy_glp(self, amount):
		self.browser.type(amount, classname="Exchange-swap-input")
		sleep(7)
		self.browser.click(classname="Exchange-swap-button")
		sleep(7)
		self.metamask.confirm_transaction()