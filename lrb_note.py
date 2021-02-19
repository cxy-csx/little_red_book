# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String, Text

class LRB_NOTE(Base):
    # 表名称
    __tablename__ = 'lrb_note'

    id = Column(Integer, primary_key=True, autoincrement=True)
    note_id = Column(String(length=30), nullable=False)
    note_url = Column(String(length=150), nullable=False)
    title = Column(String(length=80), nullable=False)
    video_poster = Column(String(length=120), nullable=False)
    video_src = Column(String(length=250), nullable=False)
    images_lists = Column(Text)
    content = Column(Text)
    like_num = Column(Integer)
    comment_num = Column(Integer)
    star_num = Column(Integer)
    publish_date = Column(String(length=20), nullable=False)
    author_name = Column(String(length=50), nullable=False)
    author_image = Column(String(length=200), nullable=False)
    author_id = Column(String(length=30), nullable=False)
    description = Column(String(length=300), nullable=False)
    board_id = Column(String(length=30), nullable=False)
    tag_str = Column(Text)
    note_str = Column(Text)
    comment_str = Column(Text)
    spider_time = Column(String(length=19), nullable=False)


