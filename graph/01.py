import os
import requests
from neomodel import db
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import shutil

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox') #让chrome在root权限下跑
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

urllist=[]#链接列表
tageturl = 'http://xzspcx.mnr.gov.cn/front/queryList' #爬取实体数据链接
browser.get(tageturl)
time.sleep(5)
for i in range(1):
    pages = browser.find_elements(By.XPATH,"//tr[@bgcolor='#FFFFFF']//a")  # 要爬取的class
    for page in pages:
        urllist.append(page.get_attribute('href'))
    aElement = browser.find_element(By.XPATH,"//a[@id='nextPage']")
    aElement.click()

names=[]#存储项目名称
for ur in urllist:#遍历url列表
    browser.get(ur)
    time.sleep(5)
    page0=browser.find_elements(By.XPATH,".//td[@class='result_title']")
    page1=browser.find_elements(By.XPATH,".//td[@class='result_title']/following-sibling::td[1]")
    for i in range(len(page0)):
        if page0[i].get_attribute('textContent')=='项目名称:':
            names.append(page1[i].get_attribute('textContent').strip())


browser.close()  # 关闭浏览器页面
#data=pd.DataFrame({'name':names})
#data.to_csv("test.csv",index=False,sep=',')


'''
oldseg_path = "H:\\python文件\\ziran\\graph\\test.csv"
newseg_path = "C:\\Program Files (x86)\\neo4j-community-4.1.10\\import"
old_segname = os.path.join(oldseg_path)
newseg_name = os.path.join(newseg_path)
shutil.copy2(old_segname, newseg_name)
'''

#db.cypher_query(query='LOAD CSV WITH HEADERS  FROM "file:///test.csv" AS line MERGE (p:土地供应项目{name:line.name})')
