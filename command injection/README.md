# LEVEL1 Command-Injection-1
### 문제 정보 : 특정 Host에 ping 패킷을 보내는 서비스입니다.
### Command Injection을 통해 플래그를 획득하세요. 플래그는 flag.py에 있습니다.
----------------------------------------------------------------------------------------------
## STEP1 코드리뷰.
----------------------------------------------------------------------------------------------
### /ping
#### cmd 부분을 보면 ping을 입력하는 명령어 구문을 활용하는 구문인 것 같다.
#### 올바르지 못한 목적지로 핑을 보낼 경우 Timeout 구문이나 알 수 없는 오류가 발생한다.
![image](https://user-images.githubusercontent.com/81984723/186346884-f8dc4805-0e8f-434b-b036-f4eb3bf4cffb.png)
----------------------------------------------------------------------------------------------

## STEP2. 문제풀이
### (1) 핑 테스트
----------------------------------------------------------------------------------------------
#### 구글 DNS 주소로 핑 테스트를 해본 결과 3개의 핑 전송 출력값을 얻을 수 있다.
#### 코드 리뷰에서 cmd 구문을 보면 {host} 부분에 어떤 값을 넣을 수 있는데 커맨드 인젝션 수행시에는 대체적으로 [];ls 처럼 입력값 뒤에 세미콜론을 붙이고 명령어를 연속으로 수행할 수 있다.
![image](https://user-images.githubusercontent.com/81984723/186347261-43870518-e65a-4de6-8d5a-1a640dba4740.png)
![image](https://user-images.githubusercontent.com/81984723/186347282-88730980-8f9f-465d-bcb0-99823e368e14.png)

### (2) 명령어 테스트
----------------------------------------------------------------------------------------------
#### 해당 핑사이트에서는 그림(1)과 같이 명령어가 수행되지 않고 입력값을 검증하는 절차가 있는 듯 했다.
#### 구글링 해보니 html 파일 내 호스트 값을 정규표현식으로 검증하는 예제가 있어 정규표현식에 대해 알아보았다.
#### [정규표현식](https://regexr.com/)
![image](https://user-images.githubusercontent.com/81984723/186347928-136b192a-61da-482d-945d-22cd6746e96f.png)
![image](https://user-images.githubusercontent.com/81984723/186347717-1554ea59-82dc-4358-a705-9b295687ffe2.png)

### (3) 개발자 도구에서 정규표현식 배제
----------------------------------------------------------------------------------------------
#### 핑 사이트에서는 특수문자 자체가 사용이 안된다는 것을 확인하여 html 코드에서 정규표현식 구문 자체를 배제 해버리기로 했다. 그림(1)과 같이 빨간색 밑줄 친 부분을 임의로 삭제하면 된다.
#### 배제 후 ping을 보내려고 하니 cmd 기능에 있는 ping -c 3에 ""(쌍따옴표) 구문을 사용해야 오류가 발생하지 않기 때문에 그림(2)와 같이 입력값을 넣으니 flag.py가 해당 경로에 있다는 것을 알 수 있었다.
![image](https://user-images.githubusercontent.com/81984723/186348876-4a4aa67b-8c5b-4ed1-8770-ce6779d154bb.png)
![image](https://user-images.githubusercontent.com/81984723/186349080-cc0c31a2-6e80-4396-a639-95b852c3c4a8.png)
![image](https://user-images.githubusercontent.com/81984723/186349107-eea42d5d-9f77-4628-b0c2-b15f9dafca9b.png)

### (4) 플래그 출력
----------------------------------------------------------------------------------------------
#### cat 구문을 사용해 flag.py를 추출한 결과
![image](https://user-images.githubusercontent.com/81984723/186349710-f734eb2a-0c91-4a70-8af7-4a65d29df790.png)
