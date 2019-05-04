from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://jaikun12.github.io/simple-task-app/?fbclid=IwAR1rlhsxD8pZVAsjdmpUPetBwOZSCEP1dossHILhkmPYCxcwQ9XWrKa_3Cg")

tasks = driver.find_element_by_id("task-input")
tasks.clear()
tasks.send_keys("1")
tasks.send_keys(Keys.RETURN)
tasks.send_keys("2")
tasks.send_keys(Keys.RETURN)
tasks.send_keys("3")
tasks.send_keys(Keys.RETURN)
tasks.send_keys("4")
tasks.send_keys(Keys.RETURN)
tasks.send_keys("5")
tasks.send_keys(Keys.RETURN)
tasks.send_keys("6")
tasks.send_keys(Keys.RETURN)
tasks.send_keys("7")
tasks.send_keys(Keys.RETURN)
tasks.send_keys("8")
tasks.send_keys(Keys.RETURN)
tasks.send_keys("9")
tasks.send_keys(Keys.RETURN)
tasks.send_keys("10")
tasks.send_keys(Keys.RETURN)


# links = driver.find_elements_by_id("task-list")
links = driver.find_elements_by_tag_name("li")
print(len(links))
