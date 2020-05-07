from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get('http://trivago.com/')
print("Test 1: Verify Title")
title=browser.title
if title == "trivago.in - Compare hotel prices worldwie":
	print(browser.title)
else:
	print("Test 1: Verify title failed")
print("Test 2: Type a destination")
element=browser.find_element(By.XPATH,'//*[@id="querytext"]')
element.send_keys("Delhi")
element2=browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div/ul/li[1]/span')
element2.click()
browser.refresh()



