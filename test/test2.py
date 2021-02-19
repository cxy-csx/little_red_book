# -*- coding: utf-8 -*-

import common
from sqlalchemy import create_engine
import lrb_tags
from sqlalchemy.orm import sessionmaker

# 连接数据库
engine = create_engine("mysql+pymysql://sa:DJFDmrsPkmNtmxzH#@xd-main-open.rwlb.rds.aliyuncs.com/test?charset=UTF8MB4")
# engine = create_engine("mysql+pymysql://sa:DJFDmrsPkmNtmxzH#@xd-main-c.rwlb.rds.aliyuncs.com/test?charset=UTF8MB4")
# 创建会话
session = sessionmaker(engine)
mySession = session()

# 查询结果集
# result = mySession.query(lrb_tags.LRB_TAGS).all()
# print(result[0])
# print(result[0].tag_id)
# print(result[0].tag_name)
# print(result[0].tag_url)
# print(result[0].spider_time)


data = {}
data['tag_id'] = '123456'
data['tag_name'] = '发斯蒂芬阿斯蒂芬'
data['tag_url'] = 'aa东方大厦阿斯蒂芬地方a安撫地方幹活啊a海付貴海付貴好丹非aa'
data['spider_time'] = '2020-11-23 09:09:09'

# lt = lrb_tags.LRB_TAGS(*data)
lt = lrb_tags.LRB_TAGS(tag_id=data['tag_id'],tag_name=data['tag_name'],tag_url=data['tag_url'],spider_time=data['spider_time'])
mySession.add(lt)
mySession.commit()



