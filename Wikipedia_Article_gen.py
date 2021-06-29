from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

counts = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
print(counts.text)
driver.save_screenshot("sc.png")
counts.click()
driver.save_screenshot("sc2.png")
search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# First import the keys class and select the methods i.e buttons

driver.refresh()
driver.maximize_window()