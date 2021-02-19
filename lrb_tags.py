# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String

class LRB_TAGS(Base):
    # 表名称
    __tablename__ = 'lrb_tags'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tag_id = Column(String(length=30), nullable=False)
    tag_name = Column(String(length=80), nullable=False)
    tag_url = Column(String(length=400), nullable=False)
    refer = Column(String(length=40), nullable=False)
    spider_time = Column(String(length=19), nullable=False)






