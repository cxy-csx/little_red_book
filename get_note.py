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
import lrb_note
import lrb_tags
from sqlalchemy.orm import sessionmaker
import urllib.parse


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
    handle = open("1.html", "a", encoding='utf-8')  # @param  mode 写入模式 r只读 w可写 a追加
    try:
        handle.write(str(string))
        handle.write("\r\n")
        handle.close()
    except Exception as e:
        print(e)


def handleTagsToTable(a_tags,mySession):
    tag_id = ''

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
            lt = lrb_tags.LRB_TAGS(tag_id=tag_id, tag_name=tag_name, tag_url=tag_url, spider_time=spider_time, refer='')
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


def makeCommentToStr(comment_box):
    comment_str = []
    for comment_one in comment_box:
        comment_text = comment_one.select('p.content')[0].get_text() # 评论内容
        nickname = comment_one.select('h4.user-nickname a')[0].get_text() # 评论者昵称
        userid = comment_one.select('h4.user-nickname a')[0].attrs['href'].replace('/user/profile/', '') # 评论者id
        publish_time = comment_one.select('.publish-time')[0].get_text() # 评论日期
        avatar = comment_one.select('img')[0].attrs['src'] # 评论者头像
        try:
            like_num = comment_one.select('span.like-sum')[0].get_text() # 点赞数目
        except Exception:
            like_num = 0
        # print('======================')
        # print(comment_text)
        # print(nickname)
        # print(userid)
        # print(publish_time)
        # print(avatar)
        # print(like_num)
        comment_str.append({"comment_text": str(comment_text), "nickname": str(nickname), "userid": str(userid), "publish_time": str(publish_time), "avatar": str(avatar), "like_num": str(like_num)})
    return json.dumps(comment_str, ensure_ascii=False)




# # 要搜索的关键字
# # kwd = '花西子'
#
# # 连接数据库
# engine = create_engine("mysql+pymysql://sa:DJFDmrsPkmNtmxzH#@xd-main-open.rwlb.rds.aliyuncs.com/test?charset=UTF8MB4")
# # engine = create_engine("mysql+pymysql://sa:DJFDmrsPkmNtmxzH#@xd-main-c.rwlb.rds.aliyuncs.com/test?charset=UTF8MB4")
# # 创建会话
# session = sessionmaker(engine)
# mySession = session()
#
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-gpu')
# options.add_argument('--disable-dev-shm-usage')
#
# # 普通PC chorme
# # user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
#
#
# # PC微信
# user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1316.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat"
#
# # IOS微信
# # user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.1(0x18000123) NetType/WIFI Language/zh_CN"
#
# # 安卓微信
# # user_agent = "Mozilla/5.0 (Linux; Android 10; NOH-AN00 Build/HUAWEINOH-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045513 Mobile Safari/537.36 MMWEBID/8741 MicroMessenger/8.0.1840(0x28000037) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64"
#
# options.add_argument("user-agent="+user_agent)
# browser = webdriver.Chrome(options=options)
# # browser = webdriver.Chrome()
#
# WebDriverWait(browser, 10)
# sleep(3)
# # browser.get('https://www.xiaohongshu.com/')
# # sleep(3)
# # browser.get('https://www.xiaohongshu.com/explore')


def write_note_in_table(note_url,user_id,board_id,browser,mySession):
    # note_url = "https://www.xiaohongshu.com"+a_note.attrs['href']

    para = urllib.parse.urlparse(note_url)
    note_url = para.scheme+"://"+para.netloc+para.path

    browser.get(note_url)

    note_id = note_url.replace("https://www.xiaohongshu.com/discovery/item/", "")
    note_id = note_id.replace("http://www.xiaohongshu.com/discovery/item/", "")

    sleep(3)
    swipe_down(browser,2)

    # browser.get_screenshot_as_file('/home/spider/GoodsSpider-master/little_red_book/screenshot.png')

    try:
        WebDriverWait(browser, 15).until(lambda x: x.find_element_by_css_selector('h1.title'))
    except Exception as e:
        return False

    h1title = browser.find_element_by_css_selector('h1.title')
    print(h1title)

    note_html = browser.page_source
    # print(note_html)
    # WriteLogFile(note_html)

    # print(a_tags)
    # print(a_tags[0])

    note_html_bs = BeautifulSoup(note_html, 'lxml')
    a_tags = note_html_bs.select('.panel-card-wrap .keywords a.keyword')
    handleTagsToTable(a_tags,mySession)

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

    # 正文
    content_ps = note_html_bs.select('main .content p')
    content = ''
    for content_p in content_ps:
        content = content + content_p.get_text() + "\n"
    # print(content)

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
    description = author_name = author_image = author_id = ''
    for script in scripts:
        # print(script)
        if script.has_attr('type') and script.attrs['type'] == 'application/ld+json' and script.get_text() != '':
            print(script.get_text())
            script_json = json.loads(script.get_text())
            author_name = script_json['author']['name']     # 作者名字
            author_image = script_json['author']['image']   # 作者头像
            author_id = script_json['author']['url']
            author_id = author_id.replace("https://www.xiaohongshu.com/user/profile/", "")  # 作者id
            description = script_json['description']        # 简短介绍

    tag_str = note_html_bs.select('.panel-card-wrap .keywords a')
    tag_str = makeTagsToStr(tag_str)  # 相关标签列表

    # 相关笔记列表
    note_str = note_html_bs.select('.panel-card .panel-list a')
    note_str = makeLinkNoteToStr(note_str)  # 相关标签列表

    # 评论列表
    comment_box = note_html_bs.select('.all-tip .content div.comment')
    comment_str = makeCommentToStr(comment_box)  # 相关标签列表
    spider_time = GetStandardTimeFormat(time.time())

    # print(note_id)
    # print(note_url)
    # print(title)
    # print(video_poster)
    # print(video_src)
    # print(images_lists)
    # print(content)
    # print(like_num)
    # print(comment_num)
    # print(star_num)
    # print(publish_date)
    # print(author_name)
    # print(author_image)
    # print(author_id)
    # print(description)
    # print(tag_str)
    # print(note_str)
    # print(comment_str)
    # print(spider_time)

    # 插入数据
    ln = lrb_note.LRB_NOTE(
        note_id=note_id,
        note_url=note_url,
        title=title,
        video_poster=video_poster,
        video_src=video_src,
        images_lists=images_lists,
        content=content,
        like_num=like_num,
        comment_num=comment_num,
        star_num=star_num,
        publish_date=publish_date,
        author_name=author_name,
        author_image=author_image,
        author_id=user_id,
        description=description,
        board_id=board_id,
        tag_str=tag_str,
        note_str=note_str,
        comment_str=comment_str,
        spider_time=spider_time
    )
    try:
        mySession.add(ln)
        mySession.commit()
    except Exception as e:
        print(e)


# note_url = 'https://www.xiaohongshu.com/discovery/item/5feb0dc8000000000100a1e4?xhsshare=CopyLink&appuid=5f2bce6100000000010092f0&apptime=1611209987'
# write_note_in_table(note_url, browser, mySession)
#
# note_url = 'https://www.xiaohongshu.com/discovery/item/5ddb9d1e0000000001003926'
# write_note_in_table(note_url, browser, mySession)
#
# note_url = 'https://www.xiaohongshu.com/discovery/item/60091c610000000001004585'
# write_note_in_table(note_url, browser, mySession)







