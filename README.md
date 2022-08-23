# CTF
지식이 늘었어요

# HTTP(Hyper Text Transfer Protocol)
## 서버와 클라이언트의 데이터 교환을 요청과 응답 형식으로 정의한 프로토콜입니다.
## 메커니즘은 클라이언트가 서버에게 요청하면 서버가 응답하는 형식
## 일반적으로 TCP/80 or TCP/8080 포트를 사용합니다.

# 네트워크 포트
## 네트워크에서 서버와 클라이언트가 정보를 교환하는 추상화된 장소를 의미한다.

# 서비스 포트
## 네트워크 포트 중 특정 서비스가 점유하고 있는 포트

# 전송 계층
## 대표적으로 TCP와 UDP가 존재
## TCP로 데이터를 전송하려는 서비스에 UDP 클라이언트가 접근하면, 데이터가 교환되지 않음
## HTTP 서비스 포트가 TCP/80이라고 하면, HTTP 서비스를 80번 포트에서 TCP로 제공하고 있다는 뜻

# HTTP 헤드
## 헤더는 필드와 값으로 구성되며 HTTP 메시지 또는 바디의 속성을 나타냄

# HTTP 요청
## 서버에게 특정 동작을 요구하는 메시지
## 서버는 해당 동작 실현 가능한지, 클라이언트가 그러한 동작을 요청할 권한이 있는지 검토 후, 적절할 때 이를 처리

# GET
## 리소스를 가져오라는 메소드
# POST
## 리소스로 데이터를 보내라는 메소드

# HTTPS(HTTP over Secure socket layer)
## TLS(Transport Layer Security) 프로토콜을 도입하여 서버와 클라이언트 사이에 오가는 모든 HTTP 메시지를 암호화

# 웹 리소스
## 웹에 갖춰진 정보 자산
### dreamhack.io/index.html 입력시 dreamhack.io에 존재하는 모든 index.html 정보를 긁어옴

# HTML
## 웹 문서의 뼈와 살을 담당
## 태그와 속성을 통한 구조화된 문서 작성을 지원합니다.

# CSS
## 웹 문서의 생김새를 지정합니다.
## 웹 리소스들의 시각화 방법을 기재한 스타일 시트입니다.

# JavaScript(JS)
## 웹 문서의 동작을 정의합니다.
## 클라이언트가 실행하는 코드라고하여 Client-Side Script라고도 부릅니다.

# Domain Name Server(DNS)
## Domain Name을 질의하고, DNS 응답한 IP Address를 사용합니다.

# 웹 렌더링
## 서버로부터 받은 리소스를 이용자에게 시각화하는 행위
## 서버의 응답을 받은 웹 브라우저는 리소스의 타입을 확인하고, 적절한 방식으로 이용자에게 전달한다.
## ex) 서버로부터 HTML / CSS를 받으면 HTML을 파싱하고 CSS를 적용해 이용자에게 보여줌

# 개발자 도구
## Elements : 페이지를 구성하는 HTML 검사
## Console : 자바 스크립트를 실행하고 결과를 확인할 수 있음
## Sources : HTML, CSS, JS 등 페이지를 구성하는 리소스를 확인하고 디버깅할 수 있음
## Network : 서버와 오가는 데이터를 확인할 수 있음
## Performance
## Memory
## Application : 쿠키를 포함해 웹 어플리케이션과 관련된 데이터를 확인할 수 있음

# 디버깅 정보
## Watch : 원하는 자바스크립트 식을 입력하면, 코드 실행 과정에서 해당 식의 값 변화를 확인할 수 있음
## Call Stack : 함수들의 호출 순서를 스택 형태로 보여준다. 예를 들어 A->B->C 순서로 함수가 호출돼 c내부의 코드를 실행하고 있다면, Call Stack의 가장 위에는 c, 가장 아래에는 A가 위치합니다.
## Scope : 정의된 모든 변수들의 값을 확인할 수 있습니다.
## Breakpoints : 브레이크포인트들을 확인하고, 각각을 활성화 또는 비활성화할 수 있다.

# 쿠키
## Key와 Value로 이뤄진 일종의 단위로, 서버가 클라이언트에게 쿠키 발급시, 클라이언트는 서버에 요청을 보낼 때마다 쿠키를 같이 전송한다.

# HTTP 프로토콜 특징
## Connectionless: 하나의 요청에 하나의 응답을 한 후 연결을 종료하는 것을 의미합니다. 특정 요청에 대한 연결은 이후의 요청과 이어지지 않고 새 요청이 있을 때 마다 항상 새로운 연결을 맺습니다.
## Stateless: 통신이 끝난 후 상태 정보를 저장하지 않는 것을 의미합니다. 이전 연결에서 사용한 데이터를 다른 연결에서 요구할 수 없습니다.

# SOP(Same Origin Policy)
## 동일 출처 정책, 현재 페이지의 출처가 아닌 다른 출처로부터 온 데이터를 읽지 못하게 하는 브라우저의 보안 메커니즘
## Same Origin : 현재 페이지와 동일한 출처
## Cross Origin : 현재 페이지와 다른 출처
## Cross Origin Resource Sharing(CORS) : 교차 출처 리소스 공유, SOP의 제한을 받지 않고 Cross Origin의 데이터를 처리할 수 있도록 해주는 메커니즘

# XSS
## 클라이언트 사이드 취약점 중 하나로, 공격자가 웹 리소스에 악성 스크립트를 삽입해 이용자의 웹 브라우저에서 해당 스크립트를 실행할 수 있습니다.
## Stored XSS : XSS에 사용되는 악성 스크립트가 서버에 저장되고 서버의 응답에 담겨오는 XSS
## Reflected XSS : XSS에 사용되는 악성 스크립트가 URL에 삽입되고 서버의 응답에 담겨오는 XSS
## DOM-based XSS : XSS에 사용되는 악성 스크립트가 URL Fragment에 삽입되는 XSS
## Universal XSS : 클라이언트의 브라우저 혹은 브라우저의 플러그인에서 발생하는 취약점으로 SOP 정책을 우회하는 XSS

## Cross Site Request Forgery (CSRF): 사이트 간 요청 위조. 이용자가 자신의 의지와는 무관하게 공격자가 의도한 행위를 특정 웹사이트에 요청하게 만드는 공격.

# 로컬호스트(Localhost)
## 로컬호스트는 컴퓨터 네트워크에서 사용하는 호스트명으로 자기자신의 컴퓨터를 의미합니다. 로컬호스트를 IPv4 방식으로 표현했을 때에는 127.0.0.1, IPv6로 표현했을 때에는 00:00:00:00:00:00:00:01로 표현합니다.

# SQL

## DDL : 데이터를 정의하기 위한 언어입니다. 데이터를 저장하기 위한 스키마, 데이터베이스의 생성/수정/삭제 등의 행위를 수행합니다.
## DML : 데이터를 조작하기 위한 언어입니다. 실제 데이터베이스 내에 존재하는 데이터에 대해 조회/저장/수정/삭제 등의 행위를 수행합니다.
## DCL : 데이터베이스의 접근 권한 등의 설정을 하기 위한 언어입니다. 데이터베이스 내에 이용자의 권한을 부여하기 위한 GRANT와 권한을 박탈하는 REVOKE가 대표적입니다.

## SQL injection: SQL 쿼리에 이용자의 입력 값을 삽입해 이용자가 원하는 쿼리를 실행할 수 있는 취약점
## Blind SQL Injection: 데이터베이스 조회 후 결과를 직접적으로 확인할 수 없는 경우 사용할 수 있는 SQL injection 공격 기법

# 비관계형 DB
## 비관계형 데이터베이스(NoSQL): SQL을 사용해 데이터를 조회/추가/삭제하는 관계형 데이터베이스(RDBMS)와 달리 SQL을 사용하지 않으며, 이에 따라 RDBMS와는 달리 복잡하지 않은 데이터를 다루는 것이 큰 특징이자 RDBMS와의 차이점
## 콜렉션(Collection): 데이터베이스의 하위에 속하는 개념

## NoSQL injection: 요청 구문에 이용자의 입력 값을 삽입해 이용자가 원하는 요청을 실행할 수 있는 취약점
## Blind NoSQL Injection: 데이터 조회 후 결과를 직접적으로 확인할 수 없는 경우 사용될 수 있는 NoSQL Injection 공격 기법

## NoSQL Injection: NoSQL DBMS가 악의적인 쿼리를 실행하게 하는 공격 기법.

## 인젝션(Injection): 악의적인 데이터를 프로그램에 입력하여 이를 시스템 명령어, 코드, 데이터베이스 쿼리 등으로 실행되게 하는 기법. 웹 애플리케이션을 대상으로 하는 인젝션 공격은 SQL Injection, command injection등이 있음.

## 커맨드 인젝션(Command Injection): 인젝션의 종류 중 하나. 시스템 명령어에 대한 인젝션을 의미함. 취약점이 발생하는 원인은 단순하지만, 매우 치명적인 공격으로 이어질 수 있음. 개발자는 이용자의 입력을 반드시 검사해야 하며, 되도록 system 함수의 사용을 자제해야 함.

## 메타 문자(Meta Character): 셸 프로그램에서 특수하게 처리하는 문자. ;를 사용하면 여러 개의 명령어를 순서대로 실행시킬 수 있음.