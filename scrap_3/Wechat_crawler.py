import requests
import re
import xlwt
from selenium import webdriver

url ="https://weixin.sogou.com/weixin?query=%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86&_sug_type_=&s_from=input&_sug_=y&type=1&page=1&ie=utf8"

browser = webdriver.Chrome()
browser.get(url)
html=browser.page_source
browser.implicitly_wait(5)
datalist=[]
workbook = xlwt.Workbook(encoding="utf_8")
Wechat_sheet = workbook.add_sheet("Wechat",cell_overwrite_ok=True)
col = ('公众号名称', '公众号', '公众号简介', '公众号照片')  # 元组 列的信息
for x in range(0, 4):
    Wechat_sheet.write(0, x, col[x])
row=1
while True:
    WechatName=browser.find_elements_by_xpath('//p[@class="tit"]/a') #公众号名称
    Wechatid=browser.find_elements_by_xpath('//label[@name="em_weixinhao"]')#公众号
    Wechatinfo=browser.find_elements_by_xpath('//dl[1]')#公众号介绍
    pat ='<img src="(.*?)"'
    WechatPic=re.compile(pat).findall(html)#公众号头像

    for i in range(len(WechatName)):
        data=[]
        # print(WechatName[i].text)
        # print(Wechatid[i].text)
        # print(Wechatinfo[i].text)
        # print("https:"+WechatPic[i])
        data.append(WechatName[i].text)
        data.append(Wechatid[i].text)
        data.append(Wechatinfo[i].text)
        data.append("https:"+WechatPic[i])
        for l in range(4):
            Wechat_sheet.write(row,l,data[l])
        row+=1
    try:
        if browser.find_element_by_xpath('//a[@id="sogou_next"]'):
            browser.find_element_by_xpath('//a[@id="sogou_next"]').click()
    except Exception as err:
        browser.quit()
        workbook.save("微信公众号.xls")
        break




