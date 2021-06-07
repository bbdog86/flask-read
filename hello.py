# -*- coding: utf-8 -*-
"""
Created on Mon May 10 12:34:39 2021

@author: ahdky-xxs
"""

from flask import Flask,render_template,jsonify,request,redirect
app = Flask(__name__)

DATA_DICT={
    '1':{'name':'AAA','age':44},
    '2':{'name':'bbb','age':11},
    '3':{'name':'CCC','age':54},
        }
@app.route('/index')
def index():
    data=DATA_DICT
    return render_template('index.html',data_list=data)

@app.route('/hello')
def hello():
    return 'hello world!'

@app.route('/login',methods=['GET','POST']) 
#定义视图，因为在flask中请求不会传递给视图，所以函数没有参数
def login():
    if request.method=="GET":
        return render_template('login.html')
   # return jsonify({'code':1000, 'data':[1,2,3]})
    user=request.form.get("user")
    passwd=request.form.get("pwd")
    if user=="1" and passwd=="1":
        return redirect('/index')
    err_msg="用户名或密码错误"
    return render_template('login.html',err=err_msg)
if __name__=="__main__":
    app.run()