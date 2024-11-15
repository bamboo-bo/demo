from selenium import webdriver
from selenium.webdriver.common.by import By
from test_data import data
from common import youyou

driver = webdriver.Chrome()
driver.get(data.url["url"])
driver.maximize_window()
driver.implicitly_wait(10)  # 智能等待10s

youyou.login(driver, data.login["path"], data.info["user"], data.info["password"])
youyou.search_movie(driver, data.search["path"], data.movie_name["name"])
youyou.logout(driver, data.logout["path"])
