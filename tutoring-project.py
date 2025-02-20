from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://docs.google.com/spreadsheets/d/1PbOt5R7eOe_4FNOogczsUG_TfCy8zg6FY34NfFy37T8/edit?gid=0#gid=0")

<<<<<<< HEAD
ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys(Keys.ARROW_DOWN).key_up(Keys.CONTROL).key_up(Keys.SHIFT).perform()

df = pd.read_clipboard()

print (df["Student Id"].uique())
=======
ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys(Keys.ARROW_DOWN).key_up(Keys.SHIFT).send_keys("c").key_up(Keys.CONTROL).perform()

df = pd.read_clipboard()
>>>>>>> 896d38fff1754ed2aa698c7a0bf7f770621e86c7
