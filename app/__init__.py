#!/user/bin/env python3
#-*-coding:utf8 -*-
"""Simple hello world app"""

from flask import Flask 

app = Flask (__name__) 

from app import routes


