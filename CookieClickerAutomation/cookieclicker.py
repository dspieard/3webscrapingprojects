from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

s = Service("/Users/daan/Documents/projects/seleniumstuff/chromedriver")
URL = "https://orteil.dashnet.org/cookieclicker/"
driver = webdriver.Chrome(service=s)
driver.get(URL)

driver.implicitly_wait(5)

big_cookie = driver.find_element(By.ID,"bigCookie")
total_cookies = driver.find_element(By.ID,"cookies")

actions = ActionChains(driver)

while True:
	actions.click(big_cookie)
	actions.perform()
	cookies = total_cookies.text.split(" ")[0]
	cookies = cookies.replace(",", "")
	cookies = cookies.replace(".", "")
	cookies = int(cookies)
	upgrades = [driver.find_element(By.ID,"productPrice" + str(i)) for i in range(1, -1, -1)]
	for upgrade in upgrades:
		print(upgrade.text)
		price = upgrade.text
		price = price.replace(",", "")
		price = price.replace(".", "")
		price = int(price)
		if price <= cookies:
			upgrade_actions = ActionChains(driver)
			upgrade_actions.move_to_element(upgrade)
			upgrade_actions.click()
			upgrade_actions.perform()
		