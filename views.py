# coding:utf-8
from run import db, app
import database
import json

HEADER = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Credentials": "true",
    "Access-Control-Allow-Origin": "*"
}
@app.route('/')
def main():
    # 主页
    return "你好，欢迎光临"

@app.route('/1')
def img():
    # 主页
    return "<img src='./static/img/1.jpg>"

@app.route('/add')
def add():
    # 增加
    stock_detail = database.StockDetail(stock_number='1234')
    db.session.add(stock_detail)
    # 事务
    db.session.commit()
    return "插入成功"

@app.route('/delete')
def delete():
    # 增加
    stock_detail = database.StockDetail(stock_number='1234')
    db.session.delete(stock_detail)
    # 事务
    db.session.commit()
    return "插入成功"


@app.route('/query')
def query():
    # 增加
    r = database.StockDetail.query.all()
    query_result = to_dict(r)
    return json.dumps(query_result), 200, HEADER


def to_dict(r):
    return [{c.name: str(getattr(x, c.name)) if getattr(x, c.name) is not None else "无" for c in x.__table__.columns} for x in r]

