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

    def stake_gmx(self, amount):
        gmx_card = self.browser.driver.find_element(By.XPATH, '//div[@class="StakeV2-content"]//div[contains(@class,"StakeV2-gmx-card")]')
        gmx_card.find_element(By.XPATH, '//button[text()="Stake"]').click()
        self.browser.driver.find_element(By.XPATH, '//input[contains(@class,"Exchange-swap-input")]').send_keys(amount)

        btn = self.browser.driver.find_element(By.XPATH, '//button[contains(@class,"Exchange-swap-button")]')
        if 'Approve' in btn.text:
            btn.click()
            self.metamask.confirm_token_approval(float(amount) * 5)
        
        self.browser.driver.find_element(By.XPATH, '//button[contains(@class,"Exchange-swap-button")]').click()
        sleep(7)
        self.metamask.confirm_transaction()

