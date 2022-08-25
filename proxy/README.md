# LEVEL1 proxy-1
### 문제 정보 : Raw Socket Sender가 구현된 서비스입니다.
### 요구하는 조건을 맞춰 플래그를 획득하세요. 플래그는 flag.txt, FLAG 변수에 있습니다.
----------------------------------------------------------------------------------------------
## STEP1 코드리뷰.
----------------------------------------------------------------------------------------------
### def문 확인
#### request.remote_addr=127.0.0.1 : 클라이언트가 ip가 127.0.0.1인지 확인
#### request.headers.get('user..) : 유저 에이전트 헤더값이 Admin Broweser인지 확인
#### request.headers.get('dreamhack..) : 드림핵유저라는 헤더 값이 admin인지 확인
#### request.cookies.get('admin') : admin이라는 쿠키값이 true인지 확인
#### request.form.get('userid') : POST 바디의 userid값이 admin 파라미터인지 확인
![image](https://user-images.githubusercontent.com/81984723/186549092-eb591ecd-1d20-458a-bb2c-d5e799c005c8.png)
![image](https://user-images.githubusercontent.com/81984723/186549118-7435ab12-5ba4-4479-8e0b-abd2d23727ea.png)

## STEP2. 문제풀이
### (1) 데이터 전송 테스트
----------------------------------------------------------------------------------------------
#### 소켓 페이지에서 임의의 데이터를 전송해보았다.
#### 오류가 발생하는 것을 알 수 있었다.
#### 위에서 설명한 코드리뷰에서 admin 값을 얻으려면 POST 요청을 보낼 때 조건들에 다 부합해야 되기 때문에 데이터를 전송할 때 이를 참고하여 전송을 해보기로 했다.
![image](https://user-images.githubusercontent.com/81984723/186549576-8e000ec9-58b9-4d6e-ad24-31496b17f39c.png)
![image](https://user-images.githubusercontent.com/81984723/186549611-3d2c2f39-bd19-4e14-8c2e-acc188edeac6.png)


### (2) 알맞은 데이터로 전송
----------------------------------------------------------------------------------------------
#### * 포트가 8000번인 이유는 플라스크에서 8000번으로 실행한다.
#### Admin id라는 에러가 발생한 이유는 POST 데이터가 userid=admin 조건에 부합하지 않아서라고 한다. 포스트 패킷 전송을 위해서는 특정 헤더가 추가 돼야하므로 구글링을 통해 살펴본바 추가해야할 헤더를 알아냈다.
![image](https://user-images.githubusercontent.com/81984723/186549733-783da55b-4682-4c08-930b-2091ea3910fa.png)
![image](https://user-images.githubusercontent.com/81984723/186549843-7e1d5e8c-39ca-4648-9060-fa470f1b16b2.png)


### (3) 플래그 획득
----------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/81984723/186550098-b07b98f1-59b5-4b6a-a427-86c7601ed4e2.png)
