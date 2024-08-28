#  Spartamarket Project
Spartamarket 프로젝트는 Django 프레임워크를 기반으로 중고거래 플랫폼의 기본적인 기능을 구현한 웹 애플리케이션 개발 프로젝트입니다.

##  프로젝트 소개
중고거래 플랫폼을 레퍼런스 하여 기본적인 웹 기능을 Django 프레임워크를 이용하여 구현

##  팀소개
- 팀명: 작심삼일
  
  팀명의 뜻: 하기로 마음먹은 일이 있으면 삼일안에 끝낸다는 생각으로 하자!
- 팀장 : 김동민
- 서기 : 배민석
- 팀원 : 이서원, 박윤성

##  개발일정
- 2024.08.20.(화) ~ 2024.08.28.(수)

##  주요기능
![1](https://github.com/user-attachments/assets/7103836f-79b6-4964-a13f-0035cc080db0)

스파르타마켓의 주요 기능은 5가지로 나눌 수 있습니다.
- 회원기능
- 유저기능
- 게시기능
- 조회기능
- 검색기능

------

###  1️⃣ 회원기능
![1회원기능](https://github.com/user-attachments/assets/9f626260-ca20-4922-8e50-6603e2ffdf51)

  - 회원 가입 : 사용자는 플랫폼에 가입하여 개인 계정을 생성할 수 있습니다.
  - 회원 정보 수정 : 회원은 자신의 프로필 정보를 수정할 수 있습니다.
  - 회원 탈퇴 : 회원은 언제든지 계정을 삭제할 수 있습니다.
  - 로그인 : 기존 회원은 계정으로 로그인하여 서비스를 이용할 수 있습니다.
  - 로그아웃 : 회원은 로그인 세션을 종료할 수 있습니다.

------

 ###  2️⃣ 유저기능
![2유저기능](https://github.com/user-attachments/assets/a45cad66-66b7-485e-9cb7-4b17cf867142)
 
  - 프로필
    - 프로필 조회 : 사용자는 자신의 프로필을 확인할 수 있습니다.
    - 작성한 게시물 조회 : 자신이 등록한 게시물을 관리할 수 있습니다.
    - 찜한 게시물 조회 : 찜한 게시물을 관리할 수 있습니다.
      
  - 팔로우
    - 팔로우, 언팔로우 기능 : 다른 사용자를 팔로우하거나 언팔로우할 수 있습니다.
    - 팔로워, 팔로잉 수 조회 : 팔로워와 팔로잉 수를 확인할 수 있습니다.

------

###  3️⃣ 게시기능
![3게시기능](https://github.com/user-attachments/assets/54ef2c22-65dc-41af-89be-210aad4dd793)

  - 물품 등록 : 사용자는 판매할 물품을 등록할 수 있습니다.
    - 필수 : 제목, 내용, 가격, 해시태그(1개 이상)
    - 선택 : 사진(미입력시 기본 사진으로 대체)
      
  - 물품 수정 : 등록한 물품의 내용을 수정할 수 있으며, 권한이 없는 사용자는 수정할 수 없습니다.
  - 물품 삭제 : 물품을 삭제할 수 있으며, 권한이 없는 사용자는 삭제할 수 없습니다.

------

###  4️⃣ 조회기능
![4조회기능](https://github.com/user-attachments/assets/c34846e8-45d1-4a6c-adfb-df11915fcd2c)

  - 전체 목록 조회 : 사용자는 전체 물품 목록을 조회할 수 있습니다.
    - 정보 : 사용자는 물품의 찜수, 조회수, 해시태그 등을 확인할 수 있고 원하는 글을 찜할 수 있습니다.
    - 정렬 : 최신순, 인기도순에 따라 물품을 조회할 수 있습니다.(default는 최신순, 인기도는 찜수가 많을수록 높음)
   
  - 상세 페이지 조회 : 물품을 클릭하여 상세 페이지에서 더 자세한 정보를 확인할 수 있습니다.
    - 이미지 링크 : 이미지를 눌러 전체 이미지를 확인할 수 있습니다.
    - 작성자 링크 : 작성자를 눌러 해당 작성자의 프로필로 이동할 수 있습니다.
      
------

###  5️⃣ 검색기능
![5검색기능](https://github.com/user-attachments/assets/62a9fa52-592c-4a5f-a07d-bef4945920fb)

  - 검색 : 사용자는 검색창에 키워드를 입력하여 제목, 내용, 작성자, 해시태그 중 해당 키워드와 일치하는 게시글 목록을 확인할 수 있습니다.

------

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
|12|유저 프로필 조회|GET|/users/{username}/|
|13|프로필 유저가 등록한 게시물 조회|GET/|/users/{username}/my_product/|
|13|프로필 유저가 찜한 게시물 조회|GET|/users/{username}/like_product/|
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

