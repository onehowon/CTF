# LEVEL1 XSS-2
### 문제 정보 : 여러 기능과 입력받은 URL을 확인하는 봇이 구현된 서비스입니다.
XSS 취약점을 이용해 플래그를 획득하세요. 플래그는 flag.txt, FLAG 변수에 있습니다.
----------------------------------------------------------------------------------------------
## STEP1 코드리뷰.
----------------------------------------------------------------------------------------------
##### from flask import Flask, request, render_template
##### from selenium import webdriver
##### import urllib
##### import os
----------------------------------------------------------------------------------------------
### (1) 플래그는 txt 확장자로 웹 내에 저장 되어 있음을 알 수 있는 구문이다.
---------------------------------------------------------------------------------------------
##### app = Flask(__name__)
##### app.secret_key = os.urandom(32)
---------------------------------------------------------------------------------------------
### (2) users 내에 있는 계정은 총 guest와 admin 두개가 존재한다. admin으로 로그인하면 flag가 나오는 것을 알 수 있다.
---------------------------------------------------------------------------------------------
##### try:
#####    FLAG = open("./flag.txt", "r").read()
#####except:
#####    FLAG = "[**FLAG**]"
---------------------------------------------------------------------------------------------
### (1) session_storage 식별자의 정보는 root 내부 /admin에 들어가 있음을 확인할 수 있다.
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

----------------------------------------------------------------------------------------------
### (1)Application 항목에 있는 세션 아이디를 이용하여 admin 계정의 session 값을 알아낼 수 있다.
### (2)admin 계정을 통해서만 flag 값을 추출할 수 있음을 알 수 있다.
---------------------------------------------------------------------------------------------
##### def check_xss(param, cookie={"name": "name", "value": "value"}):
#####    url = f"http://127.0.0.1:8000/vuln?param={urllib.parse.quote(param)}"
#####    return read_url(url, cookie)

----------------------------------------------------------------------------------------------
### (1) 위 코드를 통해 쿠키 값에서 알아낸 세션 아이디를 가지고 변조하여 admin 계정의 패스워드를 알아낼 수 있다.
##### @app.route("/")
##### def index():
#####    return render_template("index.html")


##### @app.route("/vuln")
##### def vuln():
#####    return render_template("vuln.html")


##### @app.route("/flag", methods=["GET", "POST"])
##### def flag():
#####    if request.method == "GET":
#####        return render_template("flag.html")
#####    elif request.method == "POST":
#####        param = request.form.get("param")
#####        if not check_xss(param, {"name": "flag", "value": FLAG.strip()}):
#####            return '<script>alert("wrong??");history.go(-1);</script>'

#####        return '<script>alert("good");history.go(-1);</script>'


##### memo_text = ""


##### @app.route("/memo")
##### def memo():
#####    global memo_text
#####    text = request.args.get("memo", "")
#####    memo_text += text + "\n"
#####    return render_template("memo.html", memo=memo_text)


##### app.run(host="0.0.0.0", port=8000)

----------------------------------------------------------------------------------------------
### (1) 웹을 구성하는 CODE LINE
----------------------------------------------------------------------------------------------

## STEP3. 문제풀이
----------------------------------------------------------------------------------------------
### (1)게스트 로그인 화면
#### guest로 로그인 할시 플래그는 출력되지 않으나, Application 항목 내 쿠키값을 들어가면 guest라는 쿠키값으로 들어가 있음을 알 수 있다.
----------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/81984723/186299049-df2464f1-5947-4496-a068-05423389fb2c.png)
![image](https://user-images.githubusercontent.com/81984723/186299240-ae52002d-dcd8-438d-86bf-325e4f6213ca.png)

----------------------------------------------------------------------------------------------
### (2) 쿠키값 변조
#### Value 항목의 guest 값을 admin으로 바꿔주면 성공적으로 쿠키값을 변조하여 admin 계정으로 로그인이 가능해진다.
----------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/81984723/186299438-4f716a05-9bb3-4499-bdef-b23a31460fb3.png)
----------------------------------------------------------------------------------------------
