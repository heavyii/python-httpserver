#!/usr/bin/env python
from bottle import get, post, request, run, static_file, redirect
import json

"""
@apiDefine jsonRequest
@apiHeader {String} Content-Type=application/json
"""

## 首页
@get('/')
def index():
    redirect('/static/index.html')

## 静态文件
@get('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static_file')


"""
@apiDescription 这是测试例子的描述
@api {post} /hello/:name 测试例子
@apiName name
@apiGroup 测试
@apiUse jsonRequest

@apiParam {String} [lastName] your lastName
@apiParam {String} [middleName] your middleName
"""
@post('/hello')
@post('/hello/<name>')
def hello(name = "tom"):
    # 路由参数name（可选）， post提交的参数在request.json
    # 返回用json.dumps
    return json.dumps({ 'name': name, 'request-Parameters': request.json })

run(host='localhost', port=8080)