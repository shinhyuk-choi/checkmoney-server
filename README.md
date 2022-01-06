# 가계부 API 서버
> 본인의 소비내역을 기록/관리 할수있는 REST API 서버
## Member
| 이름  | github                                   |
|-------|-----------------------------------------|
|최신혁 |[shchoi94](https://github.com/shchoi94)     | 

## 내용

### **[요구사항]**
1. **(완료)** 고객은 이메일과 비밀번호 입력을 통해서 회원 가입을 할 수 있습니다. 
2. **(완료)** 고객은 회원 가입이후, 로그인과 로그아웃을 할 수 있습니다. 
3. 고객은 로그인 이후 가계부 관련 아래의 행동을 할 수 있습니다. 
    1. **(완료)** 가계부에 오늘 사용한 돈의 금액과 관련된 메모를 남길 수 있습니다. 
    2. **(완료)** 가계부에서 수정을 원하는 내역은 금액과 메모를 수정 할 수 있습니다. 
    3. **(완료)** 가계부에서 삭제를 원하는 내역은 삭제 할 수 있습니다. 
    4. **(완료)** 삭제한 내역은 언제든지 다시 복구 할 수 있어야 한다.
    5. **(완료)** 가계부에서 이제까지 기록한 가계부 리스트를 볼 수 있습니다. 
    6. **(완료)** 가계부에서 상세한 세부 내역을 볼 수 있습니다. 
4. **(완료)** 로그인하지 않은 고객은 가계부 내역에 대한 접근 제한 처리가 되어야 합니다.
### **[추가 기능사항]**
1. 고객은 가계부를 여러 개 만들 수 있습니다.
   1. 회원가입시 기본 가계부가 자동으로 생성되고 추가로 가계부를 생성할 수 있습니다.
2. 가계부내역의 카테고리를 만들 수 있습니다.
   1. 입금내역, 지출내역의 각 기본 카테고리 데이터가 존재하고, 유저는 본인만의 커스텀한 카테고리를 생성할 수 있습니다.
   
### **[구현 요구사항]**
- **(완료)** 언어에 상관없이 Docker를 기반으로 서버를 실행 할 수 있도록 작성해주세요.
- **(완료)** DB 관련 테이블에 대한 DDL 파일을 소스 디렉토리 안에 넣어주세요.
- **(진행중)** 가능하다면 테스트 케이스를 작성해주세요.
- 별도의 요구사항이 없는 것은 지원자가 판단해서 개발합니다.
- **(완료)** 토큰을 발행해서 인증을 제어하는 방식으로 구현해주세요



## 언어 및 라이브러리,DB
> Python:Django(DRF), DB: MySQL:5.7
## 모델링
![image](https://user-images.githubusercontent.com/68194553/145536499-2ee4ea68-19fd-488d-b167-3f6a34bcb59f.png)
## API

로컬 환경 실행 후   
- [수기 작성 wiki api 문서](https://github.com/shchoi94/checkmoney-server/wiki)    
- [swagger(drf_spectacular):oas3.0](http://127.0.0.1:8000/api/schema/swagger-ui/)
  - 라이브러리를 설치 연결하였으나, 문서를 완벽하게 커스텀하지 못하였습니다. 브랜치 이동 후 확인할 수 있습니다.
  ```bash
   $ git checkout feature#5
   $ docker-compose up --force-recreate --build
  ```




## 설치 및 실행 방법

1. 해당프로젝트를 clone 하고, 프로젝트 폴더로 들어간다.
    ```bash
    $ git clone https://github.com/shchoi94/checkmoney-server.git
    $ cd checkmoney-server
    ```

2. docker-compose 명령어를 이용해서 서버와 db를 실행시킨다.
    ```bash
    $ docker-compose up
    $ docker-compose up -d //백그라운드 실행
    $ docker-compose up --force-recreate --build //강제 재빌드
    ```
3. [회원가입 -> 로그인 -> 입금카테고리 생성, 소비카테고리 생성 -> 가계부 내역 생성]    
 의 흐름으로 api를 테스트 합니다.(데이터 import 자동화 및 편리성을 제공하지 못했습니다.)     
 설계 계획은 서비스 운영자가 기본 입금, 소비 카테고리를 생성해주는 것인데 미리 데이터를 만들어 놓는 부분을 빠트렸습니다.   
    
## 폴더 구조
<details>
<summary><b>내용 자세히 보기</b></summary>
<div markdown="1">
    
```bash
📦 checkmoney-server
 ┣ 📂 checkmoney
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📜 asgi.py
 ┃ ┣ 📜 settings.py
 ┃ ┗ 📜 urls.py
 ┃ ┗ 📜 wsgi.py
 ┣ 📂 cashbook
 ┃ ┣ 📂 migrations
 ┃ ┃ ┣ 📜 0001_initial.py
 ┃ ┃ ┗ 📜 __init__.py
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📜 admin.py
 ┃ ┣ 📜 apps.py
 ┃ ┣ 📜 models.py
 ┃ ┣ 📜 serializers.py
 ┃ ┣ 📜 services.py
 ┃ ┣ 📜 urls.py
 ┃ ┗ 📜 views.py
 ┣ 📂 cashbook_log
 ┃ ┣ 📂 migrations
 ┃ ┃ ┣ 📜 0001_initial.py
 ┃ ┃ ┗ 📜 __init__.py
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📜 admin.py
 ┃ ┣ 📜 apps.py
 ┃ ┣ 📜 exceptions.py
 ┃ ┣ 📜 models.py
 ┃ ┣ 📜 serializers.py
 ┃ ┣ 📜 services.py
 ┃ ┣ 📜 urls.py
 ┃ ┗ 📜 views.py
 ┣ 📂 log_category
 ┃ ┣ 📂 migrations
 ┃ ┃ ┣ 📜 0001_initial.py
 ┃ ┃ ┗ 📜 __init__.py
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📜 admin.py
 ┃ ┣ 📜 apps.py
 ┃ ┣ 📜 models.py
 ┃ ┣ 📜 serializers.py
 ┃ ┣ 📜 services.py
 ┃ ┣ 📜 urls.py
 ┃ ┗ 📜 views.py 
 ┣ 📂 users
 ┃ ┣ 📂 migrations
 ┃ ┃ ┣ 📜 0001_initial.py
 ┃ ┃ ┗ 📜 __init__.py
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📜 admin.py
 ┃ ┣ 📜 apps.py
 ┃ ┣ 📜 models.py
 ┃ ┣ 📜 serializers.py
 ┃ ┣ 📜 services.py
 ┃ ┣ 📜 urls.py
 ┃ ┗ 📜 views.py
 ┣ 📜 .gitignore
 ┣ 📜 checkmoney_ddl.sql
 ┣ 📜 docker-compose.yml
 ┣ 📜 Dockerfile-dev
 ┣ 📜 manage.py
 ┣ 📜 pytest.ini
 ┣ 📜 README.md
 ┗ 📜 requirements.txt
 ┣ 📂 test
 ┃ ┣ 📂 user
 ┃ ┃ ┣ 📜 test_e2e.py
 ┃ ┃ ┗ 📜 test_service.py
```
</div>
</details>


## 후기   
`제품의 기능을 효율적이고 확장 가능하게 만드는` 을 고민하며 설계를 해보고자 노력하였습니다.   
입금내역과 소비내역이 같은 속성도 있지만 개별적인 속성에 대해서 확장이 쉽도록 모델을 분리하여 계획하였습니다.   
(ex. 입금내역과 별개로 소비내역에만 지출방법(현금,카드,etc) 카테고리 필드를 추가)   
   
   
하지만 이로 인해 API 호출 방법이 복잡해졌고, 개발을 하는데 있어서 복잡도도 늘어났습니다.   
현재 과제정도의 규모에서는 가계부내역을 입금, 소비 내역으로 나누는 것이 얻는 것보다 잃는 것이 많았던 생각이었던 것 같습니다.      
   
감사합니다.   
