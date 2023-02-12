from time import sleep

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