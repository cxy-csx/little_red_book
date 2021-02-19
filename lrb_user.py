# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String

class LRB_USER(Base):
    # 表名称
    __tablename__ = 'lrb_user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(length=40), nullable=False)
    nickname = Column(String(length=50), nullable=False)
    avatar = Column(String(length=250), nullable=False)
    brief = Column(String(length=300), nullable=False)
    location = Column(String(length=30), nullable=False)
    following = Column(Integer)
    follower = Column(Integer)
    starer = Column(Integer)
    spider_time = Column(String(length=19), nullable=False)


