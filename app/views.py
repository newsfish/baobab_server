from app import app
from flask import render_template
import datetime


@app.route('/')
@app.route('/index')
def admin():
    now = datetime.datetime.now()
    month = now.strftime("%b")
    date = now.strftime("%d")
    today = {"month": month, "date": date}
    return render_template("index.html",
                           date=today)
