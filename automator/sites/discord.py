from time import sleep
from selenium.webdriver.common.by import By

class Discord:
    def __init__(self, browser):
       self.browser = browser
       self.prev_window = None
       self.discord_window = None

    def accept_invite(self):
       return None