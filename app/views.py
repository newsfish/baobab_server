# coding:utf-8
from app import app
from flask import render_template
import datetime
from database import *


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    now = datetime.datetime.now()
    month = now.strftime("%b")
    date = now.strftime("%d")
    today = {"month": month, "date": date}
    return render_template("index.html", date=today)

@app.route('/stock_details.html')
@app.route('/stock_details')
def stock_detail():
    return render_template("stock_details.html")

# 订单管理页面
@app.route('/order.html')
def order():
    return render_template("order.html")

# 订单增加页面
@app.route('/add_order.html')
def add_order():
    return render_template("add_order.html")

