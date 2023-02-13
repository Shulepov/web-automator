from time import sleep
from selenium.webdriver.common.by import By

class Twitter:
    def __init__(self, browser):
        self.browser = browser
        self.prev_window = None
        self.twitter_window = None

    def open_tab(self, link):
        if not self.prev_window:
            self.prev_window = self.browser.get_current_window_handle()
        if not self.twitter_window:
            self.browser.new_tab(link)
            sleep(3)
            self.twitter_window = self.browser.get_current_window_handle()
        else:
            self.browser.go_to(link)
        sleep(10)

    def close(self):
        self.twitter_window = None
        self.browser.close_current_tab()
        self.browser.switch_to_window(self.prev_window)
        self.prev_window = None

    def follow(self, profile):
        if 'http' not in profile:
            profile = "https://twitter.com/" + profile
        self.open_tab(profile)
        try:
            btn_xpath = '//div[@role="button" and contains(@data-testid,"follow") and .//span[contains(text(),"Follow")]]'
            self.browser.driver.find_element(By.XPATH, btn_xpath).click()
            sleep(5)
        except:
            print("May be already followed")

    def like_retweet(self, post, like=True, retweet=True):
        self.open_tab(post)
        if like:
            try:
                btn_xpath = '//div[@role="button" and @data-testid="like"]'
                self.browser.driver.find_element(By.XPATH, btn_xpath).click()
                sleep(3)
            except:
                print("May be already liked")
        if retweet:
            try:
                btn_xpath = '//div[@role="button" and @data-testid="retweet"]'
                self.browser.driver.find_element(By.XPATH, btn_xpath).click()
                sleep(1)
                self.browser.driver.find_element(By.XPATH, '//div[@data-testid="retweetConfirm"]').click()
                sleep(3)
            except:
                print("May be already retweeted")

    def like(self, post):
        self.like_retweet(post, retweet=False)

    def retweet(self, post):
        self.like_retweet(post, like=False)

