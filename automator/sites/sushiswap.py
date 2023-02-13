from time import sleep
from selenium.webdriver.common.by import By

class Sushiswap:
    def __init__(self, browser, metamask):
        self.browser = browser
        self.metamask = metamask

    def try_connect(self):
        try:
            self.browser.click(id="connect-wallet")
            sleep(1)
            self.browser.driver.find_element(By.XPATH, '//div[@role="button" and div/div[@id="wallet-option-MetaMask"]]').click()
            self.metamask.connect_to_website()    
            sleep(5)
        except Exception as e:
            print("Looks like wallet already connected to sushi")

    def execute_swap(self, amount):
        url = self.browser.get_current_url()
        url += "&exactAmount=" + amount
        self.browser.go_to(url)
        sleep(10)
        try:
             self.browser.driver.find_element(By.XPATH, '//button[contains(text(),"Approve")]').click()
             self.metamask.confirm_token_approval(float(amount) * 5)
        except:
            print("Looks like token already approved")
        self.browser.driver.find_element(By.ID, 'swap-button').click()
        sleep(5)
        self.browser.driver.find_element(By.ID, 'confirm-swap-or-send').click()
        sleep(10)
        self.metamask.confirm_transaction()


