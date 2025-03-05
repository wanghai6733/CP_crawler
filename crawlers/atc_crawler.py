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
    driver.set_page_load_timeout(10)

    
    # 打开目标网站
    
    
    try:
        driver.get("https://atcoder.jp/")
    except:
        # 超时后执行Javascript停止页面加载
        driver.execute_script('window.stop()')



    time.sleep(2)
    # 获取最新比赛标签
    competitions = driver.find_elements(By.XPATH,'//div[@id="contest-table-upcoming"]//tbody/tr')
    
    datalist = []
    for competition in  competitions:
        # 获取单个比赛信息
        # print(competition.find_element(By.XPATH,"./td[1]").text)
        data = {
            "比赛名称":competition.find_element(By.XPATH,"./td/small/a[contains(@href, 'contests')]").text,
            "开始时间":competition.find_element(By.XPATH,"./td/small/a/time").text,
            "OJ":"atcoder",
            "网址":competition.find_element(By.XPATH,"./td/small/a[contains(@href, 'contests')]").get_attribute("href")
        }
        # print(data)
        datalist.append(data)
    return datalist

if __name__ == "__main__":
    datalist = get_upcoming_contests()
    print(datalist)