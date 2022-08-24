# LEVEL1 XSS-2
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
### (2) 우회 스크립트인지, vuln에서는 alert가 실행되지 않는다.
### (3) xss1 문제와는 달리 param을 반환하지 않고 있다.
---------------------------------------------------------------------------------------------
##### @app.route("/vuln")
##### def vuln():
#####    return render_template("vuln.html")

### (1) 웹을 구성하는 CODE LINE
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
#### alert문이 작동하지 않는다. xss1에서 사용했던 script 태그가 적용이 안된다고 봐야한다.
----------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/81984723/186301696-775018f7-2286-4d1f-ab62-395465a5ad66.png)

### (2) 타 우회방법 조회
#### 버그 바운티라는 사이트를 통해 XSS의 다른 공격 구문을 파악
#### img(2) 공격 구문을 입력
----------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/81984723/186328177-db1b5f24-15fd-4a69-864d-ab7850540595.png)
![image](https://user-images.githubusercontent.com/81984723/186328349-1a88935b-205c-4e81-869c-87dceda9059c.png)

### (3) 플래그 획득
#### 공격 구문 입력 후 memo 페이지로 이동하면 플래그가 정상적으로 출력되는 것을 볼 수 있다.
----------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/81984723/186328479-fd5d67e8-fcc9-423a-bf09-92b38776b031.png)
