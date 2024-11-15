from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 打开网页
driver.get('https://www.douban.com/')
driver.maximize_window()

"""
# 通过id定位
driver.switch_to.frame("输入id")
# 通过iframe下标定位
driver.switch_to.frame(1)
# 通过元素定位
"""
driver.switch_to.frame(driver.find_element(By.XPATH, "//div/iframe[@frameborder='0']"))     # 切换iframe
driver.find_element(By.XPATH, "//li[text()='密码登录']").click()
driver.find_element(By.XPATH, "//input[@id='username']").click()
driver.find_element(By.XPATH, "//input[@id='username']").send_keys('13670810125')
driver.find_element(By.XPATH, "//input[@id='password']").click()
driver.find_element(By.XPATH, "//input[@id='password']").send_keys('douban123..')
driver.find_element(By.XPATH, "//a[text()='登录豆瓣']").click()
