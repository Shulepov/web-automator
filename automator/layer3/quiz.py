from selenium.webdriver.common.by import By

#answers example [1, 2, 3, 1, 2, 5]
def do_quiz(browser, answers):
	browser.click("Start Quiz!")
	sleep(1)
	for answer in answers:
		browser.driver.find_element(By.XPATH, f'//div[@role="radiogroup"]/button[position()={answer}]').click()
		sleep(1)
		browser.click("Next Question")
		sleep(1)