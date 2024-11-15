from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()     # 与Chrome浏览器建立会话请求
url = 'https://www.yinhuadm.cc/'    # 设置URL
driver.get(url)     # 浏览器访问url
driver.maximize_window()    # 最大化浏览器窗口

# driver.find_element(By._, '') 根据标签名以及标签属性来寻找元素
# driver.find_element(By.NAME,'wd').click() 寻找带NAME属性且值为wd的元素，并点击它
# click() 点击元素，send_keys('xx') 输入值，submit() 提交(类似于回车效果)
driver.find_element(By.NAME,'wd').click()
driver.find_element(By.NAME,'wd').send_keys('斗罗大陆')
driver.find_element(By.NAME,'wd').submit()
# driver.quit()       # 退出浏览器