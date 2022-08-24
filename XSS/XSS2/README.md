# LEVEL1 XSS-1
### 문제 정보 : 여러 기능과 입력받은 URL을 확인하는 봇이 구현된 서비스입니다. XSS 취약점을 이용해 플래그를 획득하세요. 플래그는 flag.txt, FLAG 변수에 있습니다.
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
### (2) read_url 함수를 통해 쿠키가 생성되지만 도메인 주소와 우리가 부여받은 주소가 다르기에 쿠키 값을 확인하려면 해당 함수 도메인을 통해 확인해야 한다.
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
##### def check_xss(param, cookie={"name": "name", "value": "value"}):
#####    url = f"http://127.0.0.1:8000/vuln?param={urllib.parse.quote(param)}"
#####    return read_url(url, cookie)

### (1) 웹을 구성하는 CODE LINE
----------------------------------------------------------------------------------------------
##### @app.route("/")
##### def index():
#####    return render_template("index.html")


### (1) 웹을 구성하는 CODE LINE
### (2) vuln 함수에 필터링이 없기 때문에 XSS 시도가 가능하다.
---------------------------------------------------------------------------------------------
##### @app.route("/vuln")
##### def vuln():
#####    param = request.args.get("param", "")
#####    return param

### (1) 웹을 구성하는 CODE LINE
### (2) check_xss 구문을 통해 입력한 URL을 불러들어온다는 것을 알 수 있다.
----------------------------------------------------------------------------------------------
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

### (1) 웹을 구성하는 CODE LINE
### (2) memo 구문은 플래그에 입력한 값이 적절한 값일시에 플래그를 출력해준다.
----------------------------------------------------------------------------------------------
##### @app.route("/memo")
##### def memo():
#####    global memo_text
#####    text = request.args.get("memo", "")
#####    memo_text += text + "\n"
#####    return render_template("memo.html", memo=memo_text)


##### app.run(host="0.0.0.0", port=8000)

## STEP3. 문제풀이
### (1) vuln 페이지 확인
#### alert문이 작동한다.
----------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/81984723/186329369-0a32280b-cce4-4b9c-ad6a-ab55a88ed66b.png)

### (2) check_xss 함수에 포커스를 맞춘 공략
#### 플래그 함수 이후 check_xss 함수로 넘어가고, 플래그 입력란의 도메인이 127.0.0.1에 기반하므로 쿠키값을 참조하는 공격 명령어를 넣으면 플래그를 얻을 수 있다.
----------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/81984723/186329455-c1a0604d-fc25-4e71-b321-01ab13deaa1c.png)

### (3) 플래그 획득
#### 공격 구문 입력 후 memo 페이지로 이동하면 플래그가 정상적으로 출력되는 것을 볼 수 있다.
----------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/81984723/186329626-eb8ada6b-5c05-4dd9-af58-7c1b70fc811d.png)
