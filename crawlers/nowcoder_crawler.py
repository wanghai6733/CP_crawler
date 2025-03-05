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
        driver.get("https://ac.nowcoder.com/acm/contest/vip-index")
    except:
        # 超时后执行Javascript停止页面加载
        driver.execute_script('window.stop()')



    time.sleep(2)
    # 获取最新比赛标签
    competitions = driver.find_elements(By.XPATH,'//div[@class="platform-mod js-current"]/div[position() >= 2]/div[@class="platform-item-main"]')
    
    datalist = []
    for competition in  competitions:
        # 获取单个比赛信息
        # print(competition.find_element(By.XPATH,"./td[1]").text)
        data = {
            "比赛名称":competition.find_element(By.XPATH,"./div/h4/a[contains(@href, 'contest')]").text,
            "开始时间+比赛时长（小时）":competition.find_element(By.XPATH,"./div[position()=1]/ul/li[2]").text,
            "距离开始":competition.find_element(By.XPATH,"./div[position()=2]/div").text,
            "OJ":"牛客",
            "网址":competition.find_element(By.XPATH,"./div/h4/a[contains(@href, 'contest')]").get_attribute("href")
        }
        # print(data)
        datalist.append(data)
    return datalist

if __name__ == "__main__":
    datalist = get_upcoming_contests()
    print(datalist)