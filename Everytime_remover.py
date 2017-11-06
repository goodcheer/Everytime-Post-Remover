# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("Enter C for chrome , F for firefox, E for edge.\n This is Case Sensitive.")

br = input("C or F or E?: ")
path = input("Enter directory path of desired webbrowser exe file. e.g. C:/Users/hongildong/Downloads/chromedriver: ")
driver = None

if br== "C":
    driver = webdriver.Chrome(path)
if br== "F":
    driver = webdriver.Firefox(path)
if br == "E":
    driver = webdriver.edge(path)

if driver == None:
    exit()

driver.get("http://everytime.kr/login")

userid = input("ID: ")
pw = input("pw: ")
remov_num = int(input("number of posts to remove: Positive Integer"))

if remov_num >0:
    driver.find_element_by_name(name="userid").send_keys(userid)
    driver.find_element_by_name(name="password").send_keys(pw)
    driver.find_element_by_name(name="password").send_keys(Keys.RETURN)
    
    # # while True:article
    # def pageCheck(css_selector):
    #     flag = True
    #     try:
    #         elem = driver.find_element_by_css_selector(css_selector)
    #     except:
    #         flag = False
    #         print("Page not loaded Yet")
    #     return flag
    
    i= remov_num + 1
    
    while i > 0: 
        driver.get("http://everytime.kr/myarticle")
    
        driver.implicitly_wait(4)
    
        postDiv = driver.find_element_by_css_selector("div.wrap.articles")
    
    
        post = postDiv.find_element_by_css_selector(".article")
        post.click()
    
        driver.implicitly_wait(4)
        target = driver.find_element_by_css_selector(".del")
        driver.implicitly_wait(1)
        target.click()
        driver.implicitly_wait(1)
        driver.switch_to.alert.accept()
        i -= 1
        driver.implicitly_wait(10)
    
remov_num = int(input("number of comments to remove: Positive Integer"))

if remov_num >0:
    i= remov_num + 1
    
    while i > 0: 
        driver.get("http://everytime.kr/mycommentarticle")
    
        driver.implicitly_wait(4)
    
        postDiv = driver.find_element_by_css_selector("div.wrap.articles")
    
    
        post = postDiv.find_element_by_css_selector(".article")
        post.click()
    
        driver.implicitly_wait(4)
        target = driver.find_element_by_css_selector(".del")
        driver.implicitly_wait(1)
        target.click()
        driver.implicitly_wait(1)
        driver.switch_to.alert.accept()
        i -= 1
        driver.implicitly_wait(10)

    