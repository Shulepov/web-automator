from selenium.webdriver.common.by import By
from time import sleep

def chainhop_bridge(browser, metamask):
	metamask.change_network("Optimism")
	browser.new_tab("https://app.chainhop.exchange/swap/10/ETH/42161/ETH")
	sleep(5)
	try:
		browser.click(classname="connectWalletBtn")
	except:
		print("Looks like already connected to chainhop")

def run(browser, metamask):
	browser.go_to("https://beta.layer3.xyz/challenges/arbinaut-travels-radiant-plutusdao-and-stratos")
	sleep(2)
	layer3_window = browser.get_current_window_handle()

	chainhop_bridge(browser, metamask)