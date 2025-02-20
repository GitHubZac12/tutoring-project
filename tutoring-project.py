from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pandas as pd


driver = webdriver.Chrome()
driver.get("https://docs.google.com/spreadsheets/d/1PbOt5R7eOe_4FNOogczsUG_TfCy8zg6FY34NfFy37T8/edit?gid=0#gid=0")

ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_RIGHT).send_keys(Keys.SHIFT).send_keys("c").perform()
df = pd.read_clipboard()

#hello
print (df)
2+2
