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
import lrb_user
import lrb_board
import get_note
from sqlalchemy.orm import sessionmaker
import urllib.parse
import optparse
from selenium.webdriver.common.action_chains  import ActionChains


# truncate table lrb_note;
# truncate table lrb_tags;
# truncate table lrb_user;
# truncate table lrb_board;

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



def createNewBrowser():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(options=options)
    # browser = webdriver.Chrome()
    WebDriverWait(browser, 10)
    sleep(3)
    return browser


def write_user_in_table(uurl,browser,mySession):
    sleep(1)
    browser.get(uurl)
    sleep(3)
    swipe_down(browser, 2)

    WebDriverWait(browser, 15).until(lambda x: x.find_element_by_css_selector('a.translation-wrapper'))
    wrapper = browser.find_element_by_css_selector('a.translation-wrapper')
    # print(wrapper)
    sleep(2)

    user_html = browser.page_source
    user_html_bs = BeautifulSoup(user_html, 'lxml')

    user_id = user_html_bs.select('a.translation-wrapper')[0].attrs['href']
    user_id = user_id.replace('/user/profile/','')  # 用户id
    nickname = user_html_bs.select('span.name-detail')[0].get_text()  # 用户昵称
    brief = user_html_bs.select('div.user-brief')[0].get_text().strip('\n').strip('\r').strip('\b').strip()  # 个人介绍
    location = user_html_bs.select('span.location-text')[0].get_text().replace(' ','')   # 位置描述


    avatar = user_html_bs.select('.author-container .lazyload-container img')[0].attrs['src']   # 用户头像
    avatarpara = urllib.parse.urlparse(avatar)
    avatar = avatarpara.scheme + "://" + avatarpara.netloc + avatarpara.path
    avatar = avatar.replace('@240w_240h_90q_1e_1c_1x.jpg','')
    avatar = avatar+"@240w_240h_90q_1e_1c_1x.jpg"
    # print(avatar)

    following = user_html_bs.select('.card-info .info .info-number')[0].get_text()   # 关注
    follower = user_html_bs.select('.card-info .info .info-number')[1].get_text()   # 粉丝
    starer = user_html_bs.select('.card-info .info .info-number')[2].get_text()   # 获赞与收藏
    if "万" in following:
        following = following.replace("万", "")
        following = float(following) * 10000
        following = str(following)
    if "万" in follower:
        follower = follower.replace("万", "")
        follower = float(follower) * 10000
        follower = str(follower)
    if "万" in starer:
        starer = starer.replace("万", "")
        starer = float(starer) * 10000
        starer = str(starer)


    spider_time = GetStandardTimeFormat(time.time())

    ln = lrb_user.LRB_USER(
        user_id=user_id,
        nickname=nickname,
        avatar=avatar,
        brief=brief,
        location=location,
        following=following,
        follower=follower,
        starer=starer,
        spider_time=spider_time,
    )
    try:
        mySession.add(ln)
        mySession.commit()
        # WriteLogFile(spider_time)
    except Exception as e:
        print(e)


    # 写入下面的专辑
    ck = browser.find_element_by_css_selector('.note-album :not(.current-type)')
    # print(ck)
    ActionChains(browser).move_to_element_with_offset(ck, 3, 3).click().perform()

    a_albums = browser.find_elements_by_css_selector('.album-wrapper .each-album')
    # print(a_albums)
    for a_album in a_albums:
        # print(a_album)
        handles = browser.window_handles      # 获取当前窗口句柄集合
        browser.switch_to_window(handles[0])  # 跳到第1个窗口

        sleep(3)
        a_album.click()

        handles = browser.window_handles      # 获取当前窗口句柄集合
        browser.switch_to_window(handles[1])  # 跳到第1个窗口

        album_html = browser.page_source
        # print(album_html)
        album_url = browser.current_url

        album_html_bs = BeautifulSoup(album_html,'lxml')
        name = album_html_bs.select('h1.album-name')[0].get_text()

        board_id = album_url.replace('https://www.xiaohongshu.com/board/','')
        details = album_html_bs.select('div.details span')
        note = details[0].get_text().replace("篇笔记","")
        follower = details[1].get_text().replace("个粉丝","")

        print(user_id)
        print(board_id)
        print(name)
        print(note)
        print(follower)
        print(spider_time)

        lb = lrb_board.LRB_BOARD(
            user_id=user_id,
            board_id=board_id,
            name=name,
            note=note,
            follower=follower,
            spider_time=spider_time,
        )
        try:
            mySession.add(lb)
            mySession.commit()
        except Exception as e:
            print(e)

        # 写入专辑里面的笔记
        al_a_notes = album_html_bs.select('.note-info a')
        for al_a_note in al_a_notes:
            print(al_a_note)
            note_url = "https://www.xiaohongshu.com"+al_a_note.attrs['href']
            print(note_url)

            get_note.write_note_in_table(note_url,user_id,board_id,browser,mySession)

        sleep(3)
        browser.close()
        # die()

    # 写入下面的笔记
    a_notes = user_html_bs.select('.note-info a')
    browser = createNewBrowser()
    for a_note in a_notes:
        print(a_note)
        note_url = "https://www.xiaohongshu.com"+a_note.attrs['href']
        print(note_url)
        get_note.write_note_in_table(note_url,user_id,'',browser,mySession)


parse = optparse.OptionParser(usage='"usage:%prog [options] arg1"', version="%prog 1.0")
parse.add_option('-u', '--user', dest='user', type='str', metavar='用户', help='请输入用户主页链接')
s_args,args = parse.parse_args()
# print(s_args)
# print(args)
# print(s_args.user)
if s_args.user == None:
    print('请输入用户主页链接')
    die()

uurl = 'https://www.xiaohongshu.com/user/profile/' + s_args.user
# print(uurl)

# 连接数据库
engine = create_engine("mysql+pymysql://"+common.MYSQL_USER+":"+common.MYSQL_PWD+"@"+common.MYSQL_HOST+"/"+common.MYSQL_DB+"?charset=UTF8MB4")
# 创建会话
session = sessionmaker(engine)
mySession = session()

browser = createNewBrowser()
write_user_in_table(uurl,browser,mySession)





