import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from pymongo import MongoClient
import time

client = MongoClient('localhost', 27017)
db = client.dbGilbert


driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.visitjeju.net/kr/detail/list?menuId=DOM_000001718001000000&cate1cd=cate0000000002#&region2cd&pageSize=2000&sortListType=reviewcnt&viewType=thumb")
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

trs = soup.select_one(
    '#content > div > div.cont_wrap > div.recommend_area > ul')

db.attr.drop()
for tr in trs:
    img = tr.select_one('li > dl > dt > a > img')['src']
    title = tr.select_one('li > dl > dt > a > p.s_tit').text
    sub_title = tr.select_one('li > dl > dt > a > p.s_theme').text
    item_tags1 = tr.select_one(
        'li > dl > dt > a > p.item_tag.prev > a:nth-child(1)')
    if item_tags1 is None:
        item_tags1 = ''
    else:
        item_tags1 = tr.select_one(
            'li > dl > dt > a > p.item_tag.prev > a:nth-child(1)').text
    item_tags2 = tr.select_one(
        'li > dl > dt > a > p.item_tag.prev > a:nth-child(2)')
    if item_tags2 is None:
        item_tags2 = 'not existed'
    else:
        item_tags2 = tr.select_one(
            'li > dl > dt > a > p.item_tag.prev > a:nth-child(2)').text
    item_tags3 = tr.select_one(
        'li > dl > dt > a > p.item_tag.prev > a:nth-child(3)')
    if item_tags3 is None:
        item_tags3 = 'not existed'
    else:
        item_tags3 = tr.select_one(
            'li > dl > dt > a > p.item_tag.prev > a:nth-child(3)').text
    sub_item_tag1 = tr.select_one(
        'li > dl > dt > a > p.item_tag.next > a:nth-child(1)')
    if sub_item_tag1 is None:
        sub_itme_tag1 = 'not existed'
    else:
        sub_item_tag1 = tr.select_one(
            'li > dl > dt > a > p.item_tag.next > a:nth-child(1)').text
    sub_item_tag2 = tr.select_one(
        'li > dl > dt > a > p.item_tag.next > a:nth-child(2)')
    if sub_item_tag2 is None:
        sub_itme_tag2 = 'not existed'
    else:
        sub_item_tag2 = tr.select_one(
            'li > dl > dt > a > p.item_tag.next > a:nth-child(2)').text
    sub_item_tag3 = tr.select_one(
        'li > dl > dt > a > p.item_tag.next > a:nth-child(3)')
    if sub_item_tag3 is None:
        sub_itme_tag3 = 'not existed'
    else:
        sub_item_tag3 = tr.select_one(
            'li > dl > dt > a > p.item_tag.next > a:nth-child(3)').text
    sub_item_tag4 = tr.select_one(
        'li > dl > dt > a > p.item_tag.next > a:nth-child(4)')
    if sub_item_tag4 is None:
        sub_itme_tag4 = 'not existed'
    else:
        sub_item_tag4 = tr.select_one(
            'li > dl > dt > a > p.item_tag.next > a:nth-child(4)').text
    sub_item_tag5 = tr.select_one(
        'li > dl > dt > a > p.item_tag.next > a:nth-child(5)')
    if sub_item_tag5 is None:
        sub_itme_tag5 = 'not existed'
    else:
        sub_item_tag5 = tr.select_one(
            'li > dl > dt > a > p.item_tag.next > a:nth-child(5)').text
    doc = {
        'title': title,
        'img': img,
        'sub_title': sub_title,
        'item_tags1': item_tags1,
        'item_tags2': item_tags2,
        'item_tags3': item_tags3,
        'sub_item_tag': sub_item_tag1,
        'sub_item_tag2': sub_item_tag2,
        'sub_item_tag3': sub_item_tag3,
        'sub_item_tag4': sub_item_tag4,
        'sub_item_tag5': sub_item_tag5
    }
    db.attr.insert_one(doc)


print('완료')

driver.quit()
