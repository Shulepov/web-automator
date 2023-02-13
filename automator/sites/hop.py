from time import sleep
from selenium.webdriver.common.by import By

class Hop:
    def __init__(self, browser, metamask):
        self.browser = browser
        self.metamask = metamask

    def try_connect(self):
        try:
            self.browser.driver.find_element(By.XPATH, '//button[span="Connect a Wallet"]').click()
            sleep(2)
            self.browser.driver.find_element(By.XPATH, '//button[span[text()="MetaMask"]]').click()
            sleep(10)
            self.metamask.connect_to_website()
        except Exception as e:
            print(e)
            print("Looks like wallet already connected to Hop")

    #provide liquidy using token 1 or token 2 ? (first field or second)
    def provide_liquidity(self, amount, token_idx=1, stake=True):
        self.browser.type(amount, classname="jss108", number=token_idx)
        sleep(4)
        self.browser.driver.find_element(By.XPATH, '//button[span="Preview"]').click()
        sleep(6)
        dep_btn = self.browser.driver.find_element(By.XPATH, '//div[contains(@class,"giEcUF")]/button[span="Deposit"]')
        dep_and_stake_btn = self.browser.driver.find_element(By.XPATH, '//button[span="Deposit + Stake"]')
        provide_dtn = dep_and_stake_btn if stake else dep_btn
        provide_dtn.click()

        try:
            self.metamask.confirm_token_approval(float(amount) * 10)
            sleep(5)
        except:
            print("")
        self.metamask.confirm_transaction()
        sleep(5)
        if stake:
            try:
                self.metamask.confirm_token_approval()
                sleep(5)
            except:
                print("")
            self.metamask.confirm_transaction()