# -*- coding:utf-8 -*-
######################################################
#        > File Name: flask_client.py
#      > Author: GuoXiaoNao
#     > Mail: 250919354@qq.com
#     > Created Time: Mon 20 May 2019 11:52:00 AM CST
######################################################

from flask import Flask, send_file

app = Flask(__name__)


@app.route('/index')
def index():
    # 首页
    return send_file('templates/index.html')


@app.route('/login')
def login():
    # 登录
    return send_file('templates/login.html')


# #http://127.0.0.1:5000/register
@app.route('/register')
def register():
    # 注册
    return send_file('templates/register.html')


# #http://127.0.0.1:5000/用户名/info
@app.route('/<username>/info')
def info(username):
    # 个人信息
    return send_file('templates/about.html')


@app.route('/<username>/change_info')
def change_info(username):
    # 修改个人信息
    return send_file('templates/change_info.html')


@app.route('/<username>/topic/release')
def topic_release(username):
    # 发表博客
    return send_file('templates/release.html')


@app.route('/<username>/topics')
def topics(username):
    # 个人博客列表
    return send_file('templates/list.html')


@app.route('/<username>/topics/detail/<t_id>')
def topics_detail(username, t_id):
    # 博客内容详情
    return send_file('templates/detail.html')


if __name__ == '__main__':
    app.run(debug=True)
