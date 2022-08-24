# LEVEL1 cookie
### 문제 정보 : 쿠키로 인증 상태를 관리하는 간단한 로그인 서비스입니다. admin 계정으로 로그인에 성공하면 플래그를 획득할 수 있습니다.

## STEP1 코드리뷰.
#!/usr/bin/python3
##### from flask import Flask, request, render_template, make_response, redirect, url_for

##### app = Flask(__name__)
----------------------------------------------------------------------------------------------
### (1) 플래그는 txt 확장자로 웹 내에 저장 되어 있음을 알 수 있는 구문이다.
---------------------------------------------------------------------------------------------
##### try:
#####     FLAG = open('./flag.txt', 'r').read()
##### except:
#####     FLAG = '[**FLAG**]'

### (2) users 내에 있는 계정은 총 guest와 admin 두개가 존재한다. admin으로 로그인하면 flag가 나오는 것을 알 수 있다.
##### users = {
#####     'guest': 'guest',
#####     'user': 'user1234',
#####     'admin': FLAG
##### }
 ---------------------------------------------------------------------------------------------
### (1) session_storage 식별자의 정보는 root 내부 /admin에 들어가 있음을 확인할 수 있다.
---------------------------------------------------------------------------------------------
##### session_storage = {
##### }

----------------------------------------------------------------------------------------------
### (1)Application 항목에 있는 세션 아이디를 이용하여 admin 계정의 session 값을 알아낼 수 있다.
### (2)admin 계정을 통해서만 flag 값을 추출할 수 있음을 알 수 있다.
---------------------------------------------------------------------------------------------
##### @app.route('/')
##### def index():
#####     session_id = request.cookies.get('sessionid', None)
#####     try:
#####         # get username from session_storage 
#####         username = session_storage[session_id]
#####     except KeyError:
#####         return render_template('index.html')

#####     return render_template('index.html', text=f'Hello {username}, {"flag is " + FLAG if username == "admin" else "you are not admin"}')

----------------------------------------------------------------------------------------------
### (1) 위 코드를 통해 쿠키 값에서 알아낸 세션 아이디를 가지고 변조하여 admin 계정의 패스워드를 알아낼 수 있다.
##### @app.route('/login', methods=['GET', 'POST'])
##### def login():
#####     if request.method == 'GET':
#####         return render_template('login.html')
#####     elif request.method == 'POST':
#####         username = request.form.get('username')
#####         password = request.form.get('password')
#####         try:
#####             # you cannot know admin's pw 
#####             pw = users[username]
#####         except:
#####             return '<script>alert("not found user");history.go(-1);</script>'
#####        if pw == password:
#####            resp = make_response(redirect(url_for('index')) )
#####            session_id = os.urandom(32).hex()
#####             session_storage[session_id] = username
#####             resp.set_cookie('sessionid', session_id)
#####             return resp 
#####         return '<script>alert("wrong password");history.go(-1);</script>'

----------------------------------------------------------------------------------------------
### 
##### @app.route('/admin')
##### def admin():
#####     # what is it? Does this page tell you session? 
#####     # It is weird... TODO: the developer should add a routine for checking privilege 
#####     return session_storage

----------------------------------------------------------------------------------------------
##### if __name__ == '__main__':
#####     import os
#####     # create admin sessionid and save it to our storage
#####     # and also you cannot reveal admin's sesseionid by brute forcing!!! haha
#####     session_storage[os.urandom(32).hex()] = 'admin'
#####     print(session_storage)
#####     app.run(host='0.0.0.0', port=8000)

