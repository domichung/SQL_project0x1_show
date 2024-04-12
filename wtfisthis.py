#!/usr/bin/env python3
# coding=utf-8
# -*- coding: UTF-8 -*-
from flask import Flask, request, render_template, redirect ,url_for ,session
import domi_classinfo

app = Flask(__name__)
app.secret_key = 'show_key'  

#路由

@app.route('/')
def index():
    return render_template('menu.html')
    
@app.route('/second')
def rou_second():
    a = domi_classinfo.list_all_grade(1)
    b = domi_classinfo.list_all_grade(2)
    return render_template('second.html', a = a , b = b)
#腳本

#這裡是要抓 你html 裡面action 裡面的東西
@app.route('/menuaaaaa', methods=['POST'])
def script_menu():

    go_login = request.form.get("inside")

    if go_login:
        return redirect('/second')

if __name__ == '__main__':
    app.run(debug=True)
