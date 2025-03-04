from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
import time

def get_upcoming_contests():

    # 获取配置driver
    driver = webdriver.Edge()
    # driver = webdriver.Edge(options=options)
    driver.implicitly_wait(2)
    driver.set_page_load_timeout(5)

    
    # 打开目标网站
    
    
    try:
        driver.get("https://leetcode.cn/contest/")
    except:
        # 超时后执行Javascript停止页面加载
        driver.execute_script('window.stop()')



    # time.sleep(2)

    datalist = []
    try:
        competition = driver.find_element(By.XPATH,'//div[@class="contest-upcoming bright-title"]')
        data = {
            "比赛名称":competition.find_element(By.XPATH,'./div[@class="card-title text-white"]').text,
            "开始时间":competition.find_element(By.XPATH,'./div[@class="time"]').text,
            "比赛时长":competition.find_element(By.XPATH,'./div[@class="intro hidden-xs"]').text,
            "距离开始":competition.find_element(By.XPATH,'.//div[@class="card-footer"]').text
        }
        # print(data)
        datalist.append(data)
    except Exception as e:
        print(e)
    
    try:
        competition = driver.find_element(By.XPATH,'//div[@class="contest-card contest-panel biweekly-contest bright-title"]/div[@class="biweekly-ongoing"]')
        data = {
            "比赛名称":competition.find_element(By.XPATH,'./div[@class="title"]').text,
            "开始时间":competition.find_element(By.XPATH,'.//div[@class="contest-time"]/span[1]').text + competition.find_element(By.XPATH,'.//div[@class="contest-time"]/span[2]').text,
            "距离开始":competition.find_element(By.XPATH,'./div[@class="card-footer"]/span').text
        }
        # print(data)
        datalist.append(data)
    except Exception as e:
        print(e)

    return datalist

if __name__ == "__main__":
    datalist = get_upcoming_contests()
    print(datalist)