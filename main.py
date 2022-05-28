from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import datetime
import urllib
import requests
import os
import re

# 浏览器驱动
driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe')

# 创建文件夹
main = r"E:\Blockchain Lab\会议论文\CCS\2021"
if not os.path.exists(main):
    os.mkdir(main)

for j in range(0, 100):
    # proceeding会议地址
    driver.get("https://dl.acm.org/doi/proceedings/10.1145/3460120")

    # 获取session
    elem = driver.find_element_by_id("heading" + str(j + 1))
    if j != 0:
        elem.click()
    print(elem.get_attribute("innerText"))

    # 创建子文件夹
    result = re.sub(r'[\\/:*?"<>|]', ' ', elem.get_attribute("innerText"))
    print(result)
    dir = main + "\\" + result
    if not os.path.exists(dir):
        os.mkdir(dir)
    # 休眠
    sleep(5)
    # 获取pdf链接
    elementllist = driver.find_elements(By.CLASS_NAME, "red")
    pdfurllist = []
    for element in elementllist:
        pdfurllist.append(element.get_attribute('href'))
    print(pdfurllist)

    # 获取论文title与链接
    # elements = elem.find_elements_by_class_name("issue-item")
    # print(elements)
    # for e in elements:
    #     try:
    #         print("try")
    #         #链接存在
    #         href = e.find_elements_by_class_name("red")
    #         #找title
    #         titles = e.find_elements_by_class_name("issue-item__title")
    #         t = ele.find_element_by_tag_name("a")
    #         #绑定
    #         print(zip(t,href))
    #     except Exception as e:
    #         continue

    pdfname = []
    titles = driver.find_elements_by_class_name("issue-item__title")
    for ele in titles:
        title = ele.find_element_by_tag_name("a")
        pdfname.append(title.text)
        print(title.text)
    print(pdfname)

    i = 0
    k = 0
    for url in pdfurllist:
        if url != None:
            k = k + 1
            # 去除session1a重复项
            if k > 3 or j == 0:
                i = i + 1
                print(i)
                driver.get(url)
                # headers = {'User-Agent': 'Mozilla/5.0 3578.98 Safari/537.36'}
                pdf = driver.current_url
                print(pdf)
                # url = urllib.request.Request(url = pdf,headers = headers)
                # 处理特殊字符
                name = re.sub(r'[\\/:*?"<>|]', ' ', pdfname[k-1])
                print(name)
                urlfile = requests.get(url)
                with open(dir + "\\" + name + ".pdf", 'wb+') as f:
                    f.write(urlfile.content)
                sleep(1)
driver.close()
