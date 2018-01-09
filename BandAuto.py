#facebook login vers
from selenium import webdriver
from bs4 import BeautifulSoup
from CONFIG import *
import time


if __name__ == "__main__":
    print("_______________________________________________")
    print("*** Made By Pakr HyungJune copyright @ DevHyung")
    print("_______________________________________________")
    ###
    dir = './chromedriver'
    prev_article = -1
    f = open("option.txt", 'r')
    option = f.readlines()
    keyword = option[2].strip().split(',')
    type = option[6].strip()
    BAND_URL = option[10].strip()
    reple = option[14].strip()
    cycle = float(option[18].strip())
    BAND_ID = option[22].strip()
    BAND_PW = option[26].strip()
    ###
    driver = webdriver.Chrome(dir)
    #Login
    driver.get("https://band.us/home")
    print(">>> Login ... ",end='')
    driver.find_element_by_xpath('//*[@id="header"]/div/div/div/a[3]').click()
    driver.find_element_by_xpath('//*[@id="login_list"]/li[3]/a/span').click()
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(BAND_ID)
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys(BAND_PW)
    driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
    print("  Success !")
    driver.get(BAND_URL)
    time.sleep(3)
    print(">>> 감시중")
    while True:
        time.sleep(cycle)
        bs4 = BeautifulSoup(driver.page_source,'lxml')
        postlist = bs4.find("a",class_="gSrOnly")['href']
        #print("마지막: ",postlist['href'])
        if prev_article == -1:
            prev_article = postlist
        if prev_article != postlist:
            prev_article = postlist
            now = time.localtime()
            s = "\t>>>%04d%02d%02d_%02d시%02d분%02d초 새글등록" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min,now.tm_sec)
            print(s)
            text = bs4.find('div',class_='_textRegion')
            if type == 'or':
                for key in keyword:
                    if key in text.get_text():
                        driver.get('https://band.us'+postlist)
                        try:
                            time.sleep(0.5)
                            driver.find_element_by_tag_name('textarea').send_keys(reple)
                        except:
                            time.sleep(0.5)
                            driver.find_element_by_tag_name('textarea').send_keys(reple)
                        driver.find_element_by_xpath('//*[@id="content"]/div/section/div/div/div[5]/div[2]/div/div/div[4]/button').click()
                        driver.get(BAND_URL)
                        print("\t\t>>> find keyword !!!!!!!! ")
                        print("\t\t>>> https://band.us"+postlist)
                        break
            else:
                flag = True
                for key in keyword:
                    if str(text).find(key) == -1: #없
                        flag = False
                        break
                if flag:
                    driver.get('https://band.us' + postlist)
                    try:
                        time.sleep(0.5)
                        driver.find_element_by_tag_name('textarea').send_keys(reple)
                    except:
                        time.sleep(0.5)
                        driver.find_element_by_tag_name('textarea').send_keys(reple)
                    driver.find_element_by_xpath(
                        '//*[@id="content"]/div/section/div/div/div[5]/div[2]/div/div/div[4]/button').click()
                    driver.get(BAND_URL)
                    print("\t\t>>> find keyword !!!!!!!! ")
                    print("\t\t>>> https://band.us" + postlist)
        driver.refresh()