# -*- coding: utf-8 -*-
"""
Created on Mon May 10 12:34:39 2021

@author: ahdky-xxs
"""

from flask import Flask,render_template,jsonify,request,redirect,url_for
app = Flask(__name__)

DATA_DICT={
    1:{'name':'AAA','age':44},
    2:{'name':'bbb','age':11},
    3:{'name':'CCC','age':54},
        }
@app.route('/index',endpoint="idx")#通过url_for为路由命名别名
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
    user=request.form.get("user") #post方法接收参数值
    passwd=request.form.get("pwd")
    if user=="1" and passwd=="1":
        return redirect('/index')
    err_msg="用户名或密码错误"
    return render_template('login.html',err=err_msg)

@app.route('/edit',methods=['GET','POST'])
def edit():
    nid=request.args.get('nid')
    nid=int(nid)
    if request.method=='GET':
        info=DATA_DICT[nid]
        return render_template('edit.html',info=info)

    DATA_DICT[nid]['name']=request.form.get('user')
    DATA_DICT[nid]['age']=request.form.get('age')
    return redirect('index')

@app.route('/delete/<int:nid>',methods=['GET','POST'])
def delete(nid):
    #nid=request.args.get('nid')
    del DATA_DICT[nid]
    #return redirect("/index")
    return redirect(url_for("idx"))
if __name__=="__main__":
    app.run()
    
