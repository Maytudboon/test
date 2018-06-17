# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 09:36:11 2018

@author: Will Boon
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

