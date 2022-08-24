# LEVEL1 CSRF-2
### 문제 정보 : 여러 기능과 입력받은 URL을 확인하는 봇이 구현된 서비스입니다. CSRF 취약점을 이용해 플래그를 획득하세요.
----------------------------------------------------------------------------------------------
## STEP1 코드리뷰.
----------------------------------------------------------------------------------------------
##### from flask import Flask, request, render_template
##### from selenium import webdriver
##### import urllib
##### import os


---------------------------------------------------------------------------------------------
##### app = Flask(__name__)
##### app.secret_key = os.urandom(32)
---------------------------------------------------------------------------------------------


### (1) txt 확장자로 flag가 저장 되어 있다.
---------------------------------------------------------------------------------------------
#####  try:
#####    FLAG = open("./flag.txt", "r").read()
##### except:
#####    FLAG = "[**FLAG**]"

### (1) 계정은 guest와 admin 두개이다.
---------------------------------------------------------------------------------------------
##### users = {
#####    'guest': 'guest',
#####    'admin': FLAG
##### }


### (1) 웹 구현을 위한 셀레늄 모듈을 활용한 구문이다.
---------------------------------------------------------------------------------------------
##### def read_url(url, cookie={"name": "name", "value": "value"}):
#####    cookie.update({"domain": "127.0.0.1"})
#####    try:
#####        options = webdriver.ChromeOptions()
#####        for _ in [
#####            "headless",
#####            "window-size=1920x1080",
#####            "disable-gpu",
#####            "no-sandbox",
#####            "disable-dev-shm-usage",
#####        ]:
#####            options.add_argument(_)
#####        driver = webdriver.Chrome("/chromedriver", options=options)
#####        driver.implicitly_wait(3)
#####        driver.set_page_load_timeout(3)
#####        driver.get("http://127.0.0.1:8000/")
#####        driver.add_cookie(cookie)
#####        driver.get(url)
#####    except Exception as e:
#####        driver.quit()
#####        # return str(e)
#####        return False
#####    driver.quit()
#####    return True


### (1) 파라미터 값 구문
---------------------------------------------------------------------------------------------
##### def check_csrf(param, cookie={"name": "name", "value": "value"}):
#####    url = f"http://127.0.0.1:8000/vuln?param={urllib.parse.quote(param)}"
#####    return read_url(url, cookie)

### (1) 웹을 구성하는 CODE LINE
----------------------------------------------------------------------------------------------
##### @app.route("/")
##### def index():
#####    session_id = request.cookies.get('sessionid', None)
#####    try:
#####        username = session_storage[session_id]
#####    except KeyError:
#####        return render_template('index.html', text='please login')

#####    return render_template('index.html', text=f'Hello {username}, {"flag is " + FLAG if username == "admin" else "you are not an admin"}')


### (1) 웹을 구성하는 CODE LINE
### (2) 이번 문제에서도 vuln 사이트는 script 구문이 막혀 필요 없을 것 같다.
---------------------------------------------------------------------------------------------
##### @app.route("/vuln")
##### def vuln():
#####    param = request.args.get("param", "").lower()
#####    xss_filter = ["frame", "script", "on"]
#####    for _ in xss_filter:
#####        param = param.replace(_, "*")
#####    return param

### (1) 웹을 구성하는 CODE LINE
----------------------------------------------------------------------------------------------
##### @app.route("/flag", methods=["GET", "POST"])
##### def flag():
#####    if request.method == "GET":
#####        return render_template("flag.html")
#####    elif request.method == "POST":
#####        param = request.form.get("param", "")
#####        session_id = os.urandom(16).hex()
#####       session_storage[session_id] = 'admin'
#####        if not check_csrf(param, {"name":"sessionid", "value": session_id}):
#####            return '<script>alert("wrong??");history.go(-1);</script>'

#####        return '<script>alert("good");history.go(-1);</script>'

### (1) 웹을 구성하는 CODE LINE
### (2) 로그인 화면을 구상하는 구문으로 admin으로 로그인해야만 플래그 값을 준다.
----------------------------------------------------------------------------------------------
##### @app.route('/login', methods=['GET', 'POST'])
##### def login():
#####    if request.method == 'GET':
#####        return render_template('login.html')
#####    elif request.method == 'POST':
#####        username = request.form.get('username')
#####        password = request.form.get('password')
#####        try:
#####            pw = users[username]
#####        except:
#####            return '<script>alert("not found user");history.go(-1);</script>'
#####        if pw == password:
#####            resp = make_response(redirect(url_for('index')) )
#####            session_id = os.urandom(8).hex()
#####            session_storage[session_id] = username
#####            resp.set_cookie('sessionid', session_id)
#####            return resp 
#####        return '<script>alert("wrong password");history.go(-1);</script>'

### (1) change_password : pw 입력란에 비밀번호를 변경할 수 있는 함수
### (2) 위 로그인 창과 같이 admin 계정을 얻을 수 있는 파라미터 값을 보내야 할 듯하다.
----------------------------------------------------------------------------------------------
##### @app.route("/change_password")
##### def change_password():
#####    pw = request.args.get("pw", "")
#####    session_id = request.cookies.get('sessionid', None)
#####    try:
#####        username = session_storage[session_id]
#####    except KeyError:
#####        return render_template('index.html', text='please login')

#####    users[username] = pw
#####    return 'Done'

##### app.run(host="0.0.0.0", port=8000)

## STEP3. 문제풀이
### (1) 세션 접속
#### guest 계정을 통해 세션에 접근해야한다.(change_password를 활용하기 위해서는 sessionID가 필요하기 때문에)
----------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/81984723/186336759-f50be938-e2a6-4045-8732-db895588f90d.png)

### (2) 공격 코드 짜기
#### CSRF-1과 같이 HTML의 이미지 태그를 통해 접근하기로 하였다.
#### change_password란 뒤에는 패스워드를 admin으로 변경하겠다는 파라미터를 전달한다.
----------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/81984723/186337146-38a53461-1034-43d2-9c4d-7fa8e3810c3f.png)


### (3) 계정 확인 및 플래그 획득
----------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/81984723/186337228-68cbb26a-957f-4b93-98be-ddc5d77d7982.png)
![image](https://user-images.githubusercontent.com/81984723/186337265-73f8d0c9-7774-4d96-878e-fc46ebd24585.png)
