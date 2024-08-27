#  spartamarket Project

##  프로젝트 소개
중고거래 플랫폼을 레퍼런스 하여 기본적인 웹 기능을 Django 프레임워크를 이용하여 구현

##  팀소개
- 팀명: 작심삼일
  
  팀명의 뜻: 하기로 마음먹은 일이 있으면 삼일안에 끝낸다는 생각으로 하자!
- 팀장 : 김동민
- 서기 : 배민석
- 팀원 : 이서원, 박윤성

##  개발일정
- 2024.08.20(화) ~ 2024.08.28(수)

##  주요기능

- 회원 기능
  - 회원 가입
  - 회원 정보 수정
  - 회원 탈퇴
  - 로그인
  - 로그아웃
 
- 유저 기능
  - 프로필
    - 프로필 조회
    - 작성한 게시물 조회
    - 찜한 게시물 조회
  - 팔로우
    - 팔로우, 언팔로우 기능
    - 팔로워, 팔로잉 수 조회

- 게시 기능
  - 물품 등록
    - (필수) 제목, 내용, 가격, 해시태그(1개 이상)
    - (선택) 사진
  - 물품 조회
    - 전체 목록 조회
      - 찜수, 조회수
    - 정렬(최신순, 인기도순)
 
      default는 최신순이고, 인기도는 찜수가 많을수록 높다
    - 검색 : 물품에 제목, 내용, 유저이름이 포함되어 있으면 검색됨
  - 물품 수정
  - 물품 삭제
  - 상세 페이지 조회
  - 찜


## ️ 개발환경

✔️ Language : Python 3.10.11

✔️ IDE : Visual Studio Code

✔️ Framework : Django 4.2

✔️  DBMS : SQLite

##  API 명세서
|Index|기능|method type|API Path|
|---|---|---|------|
|1|MAIN|GET|/index/|
|2|로그인 페이지 이동|GET|/accounts/login/|
|3|로그인 수행|POST|/accounts/login/|
|4|로그아웃 수행|POST|/accounts/logout/|
|5|회원가입 페이지 이동|GET|/accounts/signup/|
|6|회원가입 수행|POST|/accounts/signup/|
|7|회원탈퇴 수행|POST|/accounts/delete/|
|8|회원정보수정 페이지 이동|GET|/accounts/update/|
|9|회원정보수정 수행|POST|/accounts/update/|
|10|비밀번호수정 페이지 이동|GET|/accounts/password/|
|11|비밀번호수정 수행|POST|/accounts/password/|
|12|유저 프로필 조회|GET|users/{username}/|
|13|프로필 유저가 등록한 게시물 조회|GET|users/{username}/my_product/|
|13|프로필 유저가 찜한 게시물 조회|GET|users/{username}/like_product/|
|14|유저 팔로우|POST|/users/{user_id}/follow/|
|15|전체 물품 페이지 조회|GET|/products/|
|16|물품 상세 페이지 조회|GET|/products/{product_id}/|
|17|물품 등록 페이지 이동|GET|/products/create/|
|18|물품 등록 수행|POST|/products/create/|
|19|물품 수정 페이지 이동|GET|/products/{product_id}/update/|
|20|물품 수정 수행|POST|/products/{product_id}/update/|
|21|물품 삭제 수행|POST|/products/{product_id}/delete/|
|22|검색 물품 조회|GET|/products/search/|
|23|찜하기 기능|POST|/products/{product_id}/like/|

##  ERD
![ER다이어그램](https://github.com/rabongee/django_project_spartamarket/blob/dev/ER%EB%8B%A4%EC%9D%B4%EC%96%B4%EA%B7%B8%EB%9E%A8.png)

##  프로젝트 파일 구조
SPARTAMARKET

│

├── accounts

├── media

├── products

├── spartamarket

├── static

├── templates

├── users

├── manage.py
