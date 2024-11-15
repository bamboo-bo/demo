from selenium import webdriver
from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# url = 'https://www.uump4.cc/'
# driver.get(url)
# driver.maximize_window()
# driver.implicitly_wait(10)      # 智能等待10s


# 登录网站
def login(driver, login_path, user, password):
    # login_path = "//a[text()=' 登录']"
    # user = "jasonnn"
    # password = "youyou123.."
    driver.find_element(By.XPATH, login_path).click()
    driver.find_element(By.ID, 'email').click()
    driver.find_element(By.ID, 'email').send_keys(user)
    driver.find_element(By.ID, 'password').click()
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'submit').click()


# 筛选影片
def select_movie(driver, movie_path, area, time, kind, mark):
    # movie_path = "//a[text()=' 电影']"
    # area = "//a[text()='欧美']"
    # time = "//a[text()='2020']"
    # kind = "//a[text()='纪录']"
    # mark = "//a[text()='纯净版']"
    driver.find_element(By.XPATH, movie_path).click()
    driver.find_element(By.XPATH, area).click()
    driver.find_element(By.XPATH, time).click()
    driver.find_element(By.XPATH, kind).click()
    driver.find_element(By.XPATH, mark).click()


# 搜索功能
def search_movie(driver, search_path, name):
    # name = "天若有情"
    # search_path = "//input[@name='keyword']"
    driver.find_element(By.XPATH, search_path).click()
    driver.find_element(By.XPATH, search_path).send_keys(name)
    driver.find_element(By.XPATH, search_path).submit()


# 登出功能
def logout(driver, logout_path):
    # logout_path = "//a[text()=' 退出']"
    driver.find_element(By.XPATH, logout_path).click()


