#基于Python和Flask的Web应用程序基础代码，直接粘到py文件中即可：

from flask import Flask,render_template,request #引入flask，固定写法不用动
import pymssql
app=Flask(__name__) #初始化app，固定写法不用动

@app.route('/') #设置路由，即访问该函数的url地址，如“/”，意思是域名或IP地址根目录，比如：http://localhost/访问的是下面定义的index()函数
def login(): #函数名称，可自定义，为方便记忆可以与路由名称一致
    return render_template('login.html') #这是flask访问静态页面的方法，即执行index()函数即打开index.html静态网页，注意index.html一定要放在templates目录下，其他静态内容如js、css、图片等放在static目录下。

@app.route('/greeting', methods=['POST']) #设置另一个路由，即访问该函数的url地址，如“/greeting”，意思是域名或IP地址+路由名称，比如本路由的访问地址就是：http://localhost/greeting，访问的是下面定义的greeting()函数。methods=['POST']代表接受前端提交过来的数据的方法，仅有GET和POST两种，感兴趣的同学可搜索一下GET和POST的区别，不写methods默认为GET
def greeting(): #函数名称，可自定义，为方便记忆可以与路由名称一致
    account = request.form.get('account')  #如果前端用的是POST方法传数据过来，就用form.get获取值，引号内是提交过来的参数名称
    password = request.form.get('password')
    connect = pymssql.connect("47.92.235.218","xinguan","Hr5i_3kRw","wangliang")
    if connect:
        cursor = connect.cursor()
        sql = "select * from T00_Users where UAccount='"+ a1 +"' and UPassword='" + a2 +"'"
        cursor.execute(sql)
        row = cursor.fetchone()
        if row:
            return "登录成功"
        else:
            return "登陆失败"
    else:
        return "登陆失败"
   
    if (a1 == '1')&(a2 == '123456'):
        return "登录成功" 
    else:
        return "登录失败"  #返回name变量的值，前端会收到 #return a1 + a2  #返回name变量的值，前端会收到

if __name__=='__main__': #运行程序，固定写法不用动
    app.run(host="127.0.0.1",port=80)