from selenium import webdriver
import urllib.request # 헤더 모듈
import time
from selenium.webdriver.common.action_chains import ActionChains

# 헤더
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36')]
urllib.request.install_opener(opener)

# 크롬
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.safemap.go.kr/main/smap.do?flag=2#majorCont02")
driver.refresh()


# Click Actions
action = ActionChains(driver)

click_security = driver.find_element_by_xpath('//*[@id="tabBox"]/ul/li[2]/a')
click_minimum = driver.find_element_by_xpath('//*[@id="map-right-panels"]/div[5]/div[1]/button[2]')
click_env = driver.find_element_by_xpath('//*[@id="cpted_fake"]')

action.double_click(click_security).perform()
action.click(click_env).perform()
for i in range(4):
    action.double_click(click_minimum).perform()

time.sleep(5)


# Scrapping Contents
for b in range(6):
    if b != 5: 
        for p in range(10):
            for i in range(10):
                contents = driver.find_element_by_xpath('//*[@id="map-right-panels"]/div[3]/div[2]/div[1]/ul/li[{}]/a'.format(i+1))
                print(contents.text)
            click_page = driver.find_element_by_xpath('//*[@id="pageNavigation"]/ul/li[3]/ul/li[{}]'.format(p+1))
            action.click(click_page).perform()
            print('*'*70)
            time.sleep(1)
        click_bigpage = driver.find_element_by_xpath('//*[@id="pageNavigation"]/ul/li[5]/a')
        action.click(click_bigpage).perform()
    else:
        for p in range(10):
            if p != 9:
                for i in range(10):
                    contents = driver.find_element_by_xpath('//*[@id="map-right-panels"]/div[3]/div[2]/div[1]/ul/li[{}]/a'.format(i+1))
                    print(contents.text)
                click_page = driver.find_element_by_xpath('//*[@id="pageNavigation"]/ul/li[3]/ul/li[{}]'.format(p+1))
                action.click(click_page).perform()
            else:
                for i in range(6):
                    contents = driver.find_element_by_xpath('//*[@id="map-right-panels"]/div[3]/div[2]/div[1]/ul/li[{}]/a'.format(i+1))
                    print(contents.text)
            print('*'*70)
            time.sleep(1)
    time.sleep(1)

driver.close()