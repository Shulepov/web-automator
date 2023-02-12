from time import sleep

def run(browser, metamask):
	browser.go_to("https://beta.layer3.xyz")
	sleep(6)
	try:
		browser.click("gm 👋")
		sleep(2)
	except:
		print("No gm")
