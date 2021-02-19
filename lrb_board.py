# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String

class LRB_BOARD(Base):
    # 表名称
    __tablename__ = 'lrb_board'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(length=40), nullable=False)
    board_id = Column(String(length=40), nullable=False)
    name = Column(String(length=60), nullable=False)
    note = Column(Integer)
    follower = Column(Integer)
    spider_time = Column(String(length=19), nullable=False)




