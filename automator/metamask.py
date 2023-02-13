import os
import re
import string
import errno
import sys
from collections import OrderedDict
from typing import List
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import tkinter as tk

EXTENSION_ID = 'nkbihfbeogaeaoehlefnkodbefgpgknn'
	    #		self.driver.execute_script("arguments[0].scrollIntoViewIfNeeded();", network_el);

class Metamask:
	def __init__(self, driver, browser):
		self.browser = browser
		self.driver = driver
		self.window_handle = None
		self.last_handle = None
		self.wallet_address = None

	def open_metamask(self):
		self.last_handle = self.driver.current_window_handle
		if not self.window_handle:
			self.driver.switch_to.new_window('tab')
			sleep(1)
			self.window_handle = self.driver.current_window_handle
		else:
			self.driver.switch_to.window(self.window_handle)
		self.driver.get('chrome-extension://{}/home.html'.format(EXTENSION_ID))
		sleep(7)

	def login(self, pswd):
		self.open_metamask()
		pwd_input = self.driver.find_element(By.ID, 'password')
		pwd_input.send_keys(pswd)
		sleep(1)
		login_button = self.driver.find_element(By.XPATH, '//button[@data-testid="unlock-submit"]')
		login_button.click()
		sleep(5)
		
		try:
			self.browser.click("Got it")
			sleep(1)
		except:
			print("")
		
		try:
			self.driver.find_element(By.XPATH, '//button[@data-testid="popover-close"]').click()
			sleep(1)
		except:
			print("")
						
		address = self.get_wallet_address()
		print(f'Start metamas: {address}')
		sleep(1)
		self.get_back()

	def open_popup(self):
		self.last_handle = self.driver.current_window_handle
		self.driver.switch_to.new_window('tab')
		sleep(1)
		self.driver.get('chrome-extension://{}/popup.html'.format(EXTENSION_ID))
		sleep(5)

	def close_popup(self):
		self.driver.close()
		self.get_back()
		sleep(1)

	def get_back(self):
		self.driver.switch_to.window(self.last_handle)
		self.last_handle = None
		sleep(1)

	def get_wallet_address(self):
		if self.wallet_address:
			return self.wallet_address
		root = tk.Tk()
		self.driver.find_element(By.XPATH, '//button[@data-testid="selected-account-click"]').click()
		self.wallet_address = root.clipboard_get()
		return self.wallet_address


	def change_network(self, network_name):
	    self.open_metamask()
	    self.driver.find_element(By.XPATH, '//div[@data-testid="network-display"]').click()
	    sleep(1)
	    network_el = self.driver.find_element(By.XPATH, f'//div[@data-testid="network-droppo"]//li[span="{network_name}"]')
	    network_el.click()
	    sleep(5)
	    self.get_back()

	def connect_to_website(self):
		sleep(5)
		self.open_popup()
		try:
			self.driver.find_element(By.XPATH, '//button[text()="Next"]').click()
			sleep(1)
			self.driver.find_element(By.XPATH, '//button[text()="Connect"]').click()
		except:
			print("Already connected")
		sleep(5)
		self.close_popup()

	def has_pending_transactions(self):
		try:
			pending = self.driver.find_element(By.XPATH,'//div[@class="transaction-list__pending-transactions"]//div[text()="Pending"]')
			return True
		except:
			return False

	def is_last_transaction_confirmed(self):
		return True

	def confirm_token_approval(self, value=0):
		sleep(10)
		self.open_metamask()
		try:
			#check the we confirming permission request
			self.driver.find_element(By.XPATH,'//*[contains(text(), "By granting permission")]')

			#adjust approve amount
			if value > 0:
				try:
					self.driver.find_element(By.XPATH, '//div[text()="Edit permission"]').click()
					sleep(2)
					self.browser.type(value)
					pwd_input = self.driver.find_element(By.XPATH, '//input').send_keys(str(value))
					sleep(2)
					self.driver.find_element(By.XPATH, '//button[text()="Save"]').click()
					sleep(2)
				except Exception as e:
					print(e)

			try:
				self.driver.find_element(By.XPATH, '//button[text()="Confirm"]').click()
			except:
				print("No confirm button found")
		except:
			print("Not approval window, possibly already was approved")
		while True:
			sleep(5)
			if not self.has_pending_transactions():
				break
		self.get_back()
		sleep(10)
		return self.is_last_transaction_confirmed()

	def reject_token_approval(self):
		sleep(5)
		self.open_popup()
		sleep(5)
		self.close_popup()

	def confirm_transaction(self):
		sleep(10)
		self.open_metamask()
		self.driver.find_element(By.XPATH, '//button[text()="Confirm"]').click()
		while True:
			sleep(5)
			if not self.has_pending_transactions():
				break
		self.get_back()
		sleep(20)
		return self.is_last_transaction_confirmed()

	def reject_transaction(self):
		sleep(5)
		self.open_popup()
		sleep(5)
		self.close_popup()

	def confirm_sign(self):
		sleep(10)
		self.open_metamask()
		self.driver.find_element(By.XPATH, '//div[@data-testid="signature-request-scroll-button"]').click()
		sleep(2)
		self.driver.find_element(By.XPATH, '//button[text()="Sign"]').click()
		sleep(10)
		self.get_back()
		sleep(10)

	def reject_sign(self):
		sleep(10)
		self.open_metamask()
		self.driver.find_element(By.XPATH, '//button[text()="Reject"]').click()
		sleep(10)
		self.get_back()
		sleep(10)


