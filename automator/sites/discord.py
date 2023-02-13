from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Discord:
    def __init__(self, browser):
        self.browser = browser
        self.prev_window = None
        self.discord_window = None

    def open(self, link):
        if not self.prev_window:
            self.prev_window = self.browser.get_current_window_handle()
        if not self.discord_window:
            self.browser.new_tab(link)
            sleep(3)
            self.discord_window = self.browser.get_current_window_handle()
        else:
            self.browser.go_to(link)
        sleep(10)
    
    def close(self):
        self.discord_window = None
        self.browser.close_current_tab()
        self.browser.switch_to_window(self.prev_window)
        self.prev_window = None

    def accept_invite(self):
        return None

    def send_message(self, channel, message):
        self.open(channel)
        input = self.browser.driver.find_element(By.XPATH, '//div[@role="textbox"]')
        input.click()
        input.send_keys(message)
        sleep(2)
        input.send_keys(Keys.RETURN)
        sleep(5)
        
        

