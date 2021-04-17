#!/user/bin/env python3
#-*-coding:utf8 -*-
""" HTTP route definitions"""

from app import app # From our app package import the app variable

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/about")
def about():
    me = {
        "firstname": "Trey",
        "hobbies": "DIY stuff",
        "last_name": "Cessor"
    }
    return me 