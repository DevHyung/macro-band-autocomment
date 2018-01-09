from selenium import webdriver
from bs4 import BeautifulSoup
from CONFIG import *
import time

#driver.find_element_by_xpath('').click()
#driver.find_element_by_xpath('').send_keys()
if __name__ == "__main__":
    print("_______________________________________________")
    print("*** Made By Pakr HyungJune copyright @ DevHyung")
    print("_______________________________________________")
    dir = './chromedriver'
    driver = webdriver.Chrome(dir)

    #Login
    driver.get("https://band.us/home")
    driver.find_element_by_xpath('//*[@id="header"]/div/div/div/a[3]').click()
    driver.find_element_by_xpath('//*[@id="login_list"]/li[3]/a/span').click()
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(BAND_ID)
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys(BAND_PW)
    driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
    print(">>> Login Success !")
    driver.get(BAND_URL)
    time.sleep(2)
    bs4 = BeautifulSoup(driver.page_source,'lxml')
    postlist = bs4.find_all("div",{"data-viewname" : "DPostListView"})
    for tmp in postlist:
        print( tmp.get_text())