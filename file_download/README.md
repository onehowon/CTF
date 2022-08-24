# LEVEL1 File-download-1
### 문제 정보 : File Download 취약점이 존재하는 웹 서비스입니다.
### flag.py를 다운로드 받으면 플래그를 획득할 수 있습니다.
----------------------------------------------------------------------------------------------
## STEP1 코드리뷰.
----------------------------------------------------------------------------------------------
### /upload
#### 특정 파일과 내용을 업로드 할 수 있는 구문이다.
#### with open문을 보면 디렉토리/파일이름.확장자 형태로 업로드가 가능하다.

### /read_memo()
#### 파일을 html 형태로 가져오는 함수
![image](https://user-images.githubusercontent.com/81984723/186355423-b3a96d0e-074d-4a6c-a76f-ad4f38b215b2.png)
![image](https://user-images.githubusercontent.com/81984723/186355494-b71363c6-6d58-49b7-a4f5-308361411f00.png)

## STEP2. 문제풀이
### (1) 업로드 테스트
----------------------------------------------------------------------------------------------
#### Upload my memo 메뉴에서 게시글을 업로드할 수 있다.
#### 업로드된 게시물은 리스트 형태로 홈페이지 메인에 남아 클릭시 열람이 가능한 구조이다.
#### 문제에서 flag.py를 다운 받으면 플래그를 획득할 수 있다고 했으므로 flag.py로 테스트를 진행해보았다.
![image](https://user-images.githubusercontent.com/81984723/186356647-69cde54e-487b-42c8-b001-ba0ddc13632c.png)
![image](https://user-images.githubusercontent.com/81984723/186356696-9e1d8c1b-6d90-4192-911e-26a9e0bd87c1.png)
![image](https://user-images.githubusercontent.com/81984723/186356714-3257dc11-dd7c-4876-b694-26d376c7ec0b.png)

### (2) flag.py 메모 테스트
----------------------------------------------------------------------------------------------
#### 메모를 업로드하여 flag.py를 읽으려고 했으나 디렉토리 에러가 발생하여 접근이 불가능했다.
#### 업로드한 메모 URL 형태가 name=()로 시작한다는 것을 알고 해당 URL을 통해 접근해보기로 했다.
![image](https://user-images.githubusercontent.com/81984723/186357072-a4f27bc9-0828-4337-b231-898f56eced0c.png)
![image](https://user-images.githubusercontent.com/81984723/186357088-cd80d42c-eb30-4aec-8c4a-708069cfb0da.png)

### (3) URL로 접근 및 플래그 획득
----------------------------------------------------------------------------------------------
#### 메모 업로드를 통해 접근할 때와 비교하면 URL로 직접 경로 접근을 시도하니 플래그 획득에 성공하였다.
![image](https://user-images.githubusercontent.com/81984723/186357471-e2fdc1b0-abb0-4a2a-9d02-ef82c3eec7b3.png)
![image](https://user-images.githubusercontent.com/81984723/186357510-a58b4674-30b6-4b27-8775-42879e641b00.png)
