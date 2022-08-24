# LEVEL1 CSRF-1
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


### (1) 웹 구현을 위한 셀레늄 모듈을 활용한 구문이다.
### (2) 페이지는 XSS 페이지와 별 차이가 없다.
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


### (1) url 구문에서 param에 알맞은 값을 입력해야만 flag를 준다.
---------------------------------------------------------------------------------------------
##### def check_csrf(param, cookie={"name": "name", "value": "value"}):
#####    url = f"http://127.0.0.1:8000/vuln?param={urllib.parse.quote(param)}"
#####    return read_url(url, cookie)

### (1) 웹을 구성하는 CODE LINE
----------------------------------------------------------------------------------------------
##### @app.route("/")
##### def index():
#####    return render_template("index.html")


### (1) 웹을 구성하는 CODE LINE
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
#####        if not check_csrf(param):
#####            return '<script>alert("wrong??");history.go(-1);</script>'

#####        return '<script>alert("good");history.go(-1);</script>


##### memo_text = ""

### (1) 웹을 구성하는 CODE LINE
----------------------------------------------------------------------------------------------
##### @app.route("/memo")
##### def memo():
#####    global memo_text
#####    text = request.args.get("memo", None)
#####    if text:
#####        memo_text += text
#####    return render_template("memo.html", memo=memo_text)

### (1) 웹을 구성하는 CODE LINE
### (2) 메모에 플래그를 작성하는 기능을 가진 함수로 주어진 도메인으로 접속하지 않을시 Access Denied, 유저id로 로그인하지 않을시 Access Denied2가 출력된다.
### (3) 전역 변수인 memo_text에 의해 메모에 플래그 값이 출력된다.
----------------------------------------------------------------------------------------------
##### @app.route("/admin/notice_flag")
##### def admin_notice_flag():
#####    global memo_text
#####    if request.remote_addr != "127.0.0.1":
#####        return "Access Denied"
#####    if request.args.get("userid", "") != "admin":
#####        return "Access Denied 2"
#####    memo_text += f"[Notice] flag is {FLAG}\n"
#####    return "Ok"


##### app.run(host="0.0.0.0", port=8000)

## STEP3. 문제풀이
### (1) vuln 페이지 확인
#### vuln 페이지는 파라미터에 스크립트 alert를 넣어 서버에 요청을 보냈으나 alert(1)이 페이지에 출력 되었다.
#### notice_flag 함수에 따르면 플래그 획득을 위해서는 127.0.0.1 도메인으로 접근을 해야 하므로 vuln 페이지의 파라미터를 이용해 접근을 시도해보았다.
#### 플래그가 나오지 않는 점을 보아 vuln 페이지로 접근하는 것은 아니라는 결론에 도달했다.
----------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/81984723/186331013-100182f6-6b18-4273-ae0c-2a75089f6776.png)
![image](https://user-images.githubusercontent.com/81984723/186331340-4840fc1a-8e2e-47d1-9492-0e1134243a7a.png)
![image](https://user-images.githubusercontent.com/81984723/186331417-a95bf8b7-ba25-4e21-9465-7674e18bf5eb.png)


### (2) 코드 재분석
#### vuln 페이지 코드를 보면, xss_filter 라는 기능이 있다. 해당 기능이 script문을 필터링 하고 있었기에 XSS를 시도해도 먹히질 않는 것이었다.
#### admin_notice_flag 함수는 유저명이 admin일 경우에만 memo_text 전역 변수에 flag를 넣어준다고 했었기에 flag 페이지에 이미지 태그를 이용해 src 속성에 admin_notice_flag 페이지를 요청하는 것이 바람직해보였다.
#### read_url 함수를 잘 이용하면 셀레늄 모듈이 admin_notice_flag 페이지로 이동시켜줄 것이라 예상했다.
----------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/81984723/186331636-3442317b-2eca-4511-8b13-1a630edd91e8.png)
![image](https://user-images.githubusercontent.com/81984723/186331904-69b8aa50-2992-421f-b2e0-36bec4dfb857.png)


### (3) 플래그 페이지를 통한 접근
#### 플래그 페이지의 URL의 admin/notice_flag 구문을 이용해 세션값을 admin으로 임의설정하여 이미지 태그로 접근해보았다.
----------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/81984723/186332230-ddfd01f6-9fad-4532-a2d3-57ef5f91fb16.png)
![image](https://user-images.githubusercontent.com/81984723/186332339-2f812294-3d77-4804-ab19-37320e127634.png)

### (4) 플래그 획득
----------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/81984723/186332414-3cd5c648-3e7b-4b69-9b9c-b50300590807.png)

