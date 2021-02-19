# -*- coding: utf-8 -*-

import time
import common
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from pandas.io.sql import execute
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import urllib.parse
from sqlalchemy import create_engine
import lrb_tags
from sqlalchemy.orm import sessionmaker


def GetStandardTimeFormat(timestamp=time.time()):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(timestamp)))


def swipe_down(browser,second):
    for i in range(int(second / 0.1)):
        js = "var q=document.documentElement.scrollTop=" + str(100 + 50 * i)
        browser.execute_script(js)
        # sleep(0.5)
    js = "var q=document.body.scrollTop=10000"
    browser.execute_script(js)
    # sleep(0.5)


def WriteLogFile(string):
    handle = open("insert_lrb_tags.sql", "a", encoding='utf-8')  # @param  mode 写入模式 r只读 w可写 a追加
    try:
        handle.write(str(string))
        handle.write("\r\n")
        handle.close()
    except Exception as e:
        print(e)


def handleTagsToTable(a_tags,mySession,refer='null'):
    tag_id = ''
    if refer == 'null':
        refer = 'index'

    for a_tag in a_tags:
        tag_name = a_tag.get_text().strip('\n').strip('\r').strip('\r\n').strip('\n\r').strip()
        a_url = a_tag.attrs['href']
        # print(a_url)

        if '/mobile/tags/' in a_url:
            tag_id = a_url.replace('/mobile/tags/', '')
            tag_id = tag_id.replace('?name=' + urllib.parse.quote(tag_name), '')
            tag_url = 'https://www.xiaohongshu.com' + a_url

            tag_id = str(tag_id)
            tag_name = str(tag_name)
            tag_url = str(tag_url)
            spider_time = str(GetStandardTimeFormat(time.time()))

            # 插入tag数据
            lt = lrb_tags.LRB_TAGS(tag_id=tag_id, tag_name=tag_name, tag_url=tag_url, spider_time=spider_time, refer=refer)
            try:
                mySession.add(lt)
                mySession.commit()
            except Exception as e:
                print(e)
    return tag_id


def makeTagsToStr(a_tags):
    tag_str = []
    for a_tag in a_tags:
        tag_name = a_tag.get_text().strip('\n').strip('\r').strip('\r\n').strip('\n\r').strip()
        a_url = a_tag.attrs['href']

        if '/mobile/tags/' in a_url:
            tag_id = a_url.replace('/mobile/tags/', '')
            tag_id = tag_id.replace('?name=' + urllib.parse.quote(tag_name), '')
            tag_str.append({"tag_id":str(tag_id),"tag_name":str(tag_name)})

    return json.dumps(tag_str, ensure_ascii=False)


def makeLinkNoteToStr(a_notes):
    note_str = []
    for a in a_notes:
        note_id = a.attrs['href'].replace('/discovery/item/', '')
        note_desc = a.select('p.desc')[0].get_text()
        note_str.append({"note_id": str(note_id), "note_desc": str(note_desc)})

    return json.dumps(note_str, ensure_ascii=False)



# 要搜索的关键字
kwd = '花西子'

# 连接数据库
engine = create_engine("mysql+pymysql://sa:DJFDmrsPkmNtmxzH#@xd-main-open.rwlb.rds.aliyuncs.com/test?charset=UTF8MB4")
# engine = create_engine("mysql+pymysql://sa:DJFDmrsPkmNtmxzH#@xd-main-c.rwlb.rds.aliyuncs.com/test?charset=UTF8MB4")
# 创建会话
session = sessionmaker(engine)
mySession = session()

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
# browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome()
WebDriverWait(browser, 10)

index_url = 'https://www.xiaohongshu.com/explore'
browser.get(index_url)
sleep(1)
swipe_down(browser, 3)

notes_element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.note-wrapper .note-column .note')))
print(notes_element)

notes_element.click()
sleep(3)

handles = browser.window_handles      # 获取当前窗口句柄集合
browser.switch_to_window(handles[0])  # 跳到第1个窗口
browser.close()

handles = browser.window_handles      # 获取当前窗口句柄集合
browser.switch_to_window(handles[0])  # 跳到第1个窗口

item_html = browser.page_source
# print(item_html)
i_html_bs = BeautifulSoup(item_html,'lxml')
a_tags = i_html_bs.select('.panel-card-wrap .keywords a.keyword')

# print(a_tags)
# print(a_tags[0])

tag_id = handleTagsToTable(a_tags,mySession)

# 取出最后一个tag_id做关键字搜索
new_url = 'https://www.xiaohongshu.com/mobile/tags/'+tag_id+'?name='+urllib.parse.quote(kwd)
print(new_url)

browser.get(new_url)
sleep(2)
swipe_down(browser, 2)

kwd_tag_html = browser.page_source
# print(kwd_tag_html)

# 把标签页的推荐标签写入表中
kwd_tag_html_bs = BeautifulSoup(kwd_tag_html,'lxml')
kwd_a_tags = kwd_tag_html_bs.select('.recommend-keywords a')

handleTagsToTable(kwd_a_tags,mySession,kwd)

# 循环笔记列表的瀑布流
a_notes = kwd_tag_html_bs.select('.note-list-wrap .note-wrapper .note .note-info a')
# print(a_notes)
for a_note in a_notes:
    print('========================================================')
    print(a_note)
    print(a_note.get_text())
    note_url = "https://www.xiaohongshu.com"+a_note.attrs['href']
    browser.get(note_url)
    note_html = browser.page_source
    note_html_bs = BeautifulSoup(note_html, 'lxml')

    title = note_html_bs.select('h1.title')[0].get_text().strip('\n').strip('\r').strip('\b').strip() # 标题

    video_poster = video_src = images_lists = ''
    try:
        video = note_html_bs.select('.videoframe video')[0]
        video_poster = "https:" + video.attrs['poster']
        video_poster = video_poster.replace("?imageView2/2/w/1080/format/jpg", "")  # 视频封面
        video_src = video.attrs['src']
        video_src = video_src.replace("amp;", "")   # 视频链接

    except Exception as e:
        # 没有视频的情况下获取图片数组
        img_boxes = note_html_bs.select('.small-pic .each .img')
        images_list = []
        for img_box in img_boxes:
            one_img = img_box.attrs['style']
            one_img = one_img.replace("background-image:url(","")
            one_img = one_img.replace("?imageView2/2/w/100/h/100/q/75","")
            images_list.append(one_img)
        images_lists = json.dumps(images_list, ensure_ascii=False) # 图片

    content = note_html_bs.select('main .content')[0].get_text().strip('\n').strip('\r').strip('\b').strip()
    content = content.replace("-", "\n") # 正文

    like_num = note_html_bs.select('.operation-block .like')[0].get_text()        # 点赞数
    comment_num = note_html_bs.select('.operation-block .comment')[0].get_text()  # 评论数
    star_num = note_html_bs.select('.operation-block .star')[0].get_text()        # 收藏数
    if "万" in like_num:
        like_num = like_num.replace("万", "")
        like_num = float(like_num) * 10000
        like_num = str(like_num)
    if "万" in comment_num:
        comment_num = comment_num.replace("万", "")
        comment_num = float(comment_num) * 10000
        comment_num = str(comment_num)
    if "万" in star_num:
        star_num = star_num.replace("万", "")
        star_num = float(star_num) * 10000
        star_num = str(star_num)

    publish_date = note_html_bs.select('.publish-date span')[0].get_text()        # 发表时间
    publish_date = publish_date.replace("发布于 ", "")

    scripts = note_html_bs.select('script')
    description = author_name = author_image = author_url = ''
    for script in scripts:
        print(script)
        if script.has_attr('type') and script.attrs['type'] == 'application/ld+json':
            script.get_text()
            script_json = json.loads(script.get_text())
            author_name = script_json['author']['name']     # 作者名字
            author_image = script_json['author']['image']   # 作者头像
            author_url = script_json['author']['url']       # 作者主页
            description = script_json['description']        # 简短介绍

    tag_str = note_html_bs.select('.panel-card-wrap .keywords a')
    tag_str = makeTagsToStr(tag_str)  # 相关标签列表

    # 相关笔记列表
    note_str = note_html_bs.select('.panel-card .panel-list a')
    note_str = makeLinkNoteToStr(note_str)  # 相关标签列表

    print(title)
    print(video_poster)
    print(video_src)
    print(images_lists)
    print(content)
    print(like_num)
    print(comment_num)
    print(star_num)
    print(publish_date)
    print(author_name)
    print(author_image)
    print(author_url)
    print(description)
    print(tag_str)
    print(note_str)

    die()


