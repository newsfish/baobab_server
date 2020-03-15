# coding:utf-8
from run import db


# 货物详情
class BabyStatistics(db.Model):
    __tablename__ = 'baby_statistics'
    # 操作id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 宝宝名字
    baby_name = db.Column(db.String(500))
    # 行为
    action = db.Column(db.String(500))
    # 喂奶量
    amount = db.Column(db.Integer)
    # 日期
    datetime = db.Column(db.DateTime)

class BabyInfo(db.Model):
    __tablename__ = 'baby_info'
    # 宝宝id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    baby_name = db.Column(db.String)

class BabyAction(db.Model):
    __tablename__ = 'baby_action'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)