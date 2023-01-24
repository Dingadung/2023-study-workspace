# 과제 2: Django App file 역할 정리

## 1. __**init__**.py

- init.py란 폴더(디렉터리, 파일이 위치한 경로)가 패키지로 인식되도록 하는 역할을 한다.
    
    **→** 쉽게 말하면 우리가 패키지의 모듈을 추가할 때 사용하는 from, import를 이 경로에 사용할 수 있다
    
- 이름 그대로 패키지를 초기화하는 역할을 한다.

## 2. admin.py

- admin.py는 장고 어드민에 어떤 모델(테이블)을 출력할 것인지를 기록한다.
    
    **→** 반영된 Resource 모델을 장고 어드민 페이지에 출력하는 역할을 한다.
    

## 3. apps.py

- 앱에 대한 기본 설정 정보를 담고 있는 파일

## 4. models.py

- 모델에 대한 정보를 정의하고 저장하는 파일, 테이블 생성 및 테이블 필드가 정의된 파일

## 5. test.py

- test case를 다루는 파일

## 6. views.py

- 앱에 대한 뷰를 설정

# 과제 3: Django app 생성 - 질문 정리

1. 가격이 음수로 생성될 경우, 오류가나며 object가 생성되지 않습니다.
2. 제목이 100글자로 글자수 제한이 되어 있는 경우, 100글자 이상 적는 것이 아예 불가능합니다.
3. 서버를 재시작하더라도, 등록한 값들은 남아있습니다.

# 과제 4: API 생성 Github 제출
https://github.com/Dingadung/backend-week3

## API 생성 전, 모르는 개념 정리하기

### JSON

> JavaScript Object Notation라는 의미의 축약어로 데이터를 저장하거나 전송할 때 많이 사용되는 **경량의 DATA 교환 형식으로,** JSON은 ****데이터 포맷일 뿐이며 어떠한 통신 방법도, 프로그래밍 문법도 아닌 단순히 데이터를 표시하는 **표현 방법**일 뿐이다.
> 

특징

1. 서버와 클라이언트 간의 교류에서 일반적으로 많이 사용된다.
2. 자바스크립트 객체 표기법과 아주 유사하다.
3. 자바스크립트를 이용하여 JSON 형식의 문서를 쉽게 자바스크립트 객체로 변환할 수 있는 이점이 있다.
4. **JSON 문서 형식은 자바스크립트 객체의 형식을 기반으로 만들어졌다.**
5. 자바스크립트의 문법과 굉장히 유사하지만 **텍스트 형식일 뿐**이다.
6. 다른 프로그래밍 언어를 이용해서도 쉽게 만들 수 있다.
7. 특정 언어에 종속되지 않으며, 대부분의 프로그래밍 언어에서 JSON 포맷의 데이터를 핸들링 할 수 있는 라이브러리를 제공한다.

### HTTP method (GET, PUT, POST, DELETE)

1. GET: 리소스 조회
2. PUT: 리소스를 대체(덮어쓰기), 해당 리소스가 없으면 생성
3. POST: 요청 데이터 처리, 주로 등록에 사용
4. DELETE: 리소스 삭제
5. PATCH: 리소스 부분 변경(PUT이 전체변경, PATCH는 일부 변경)

### RESTful

1. **REST**
    
    (Representational State Transfer)의 약자로 자원을 이름으로 구분하여 해당 자원의 상태를 주고받는 모든 것을 의미한다.
    
    - HTTP URI(Uniform Resource Identifier)를 통해 자원(Resource)을 명시하고,
    - HTTP Method(POST, GET, PUT, DELETE, PATCH 등)를 통해
    - 해당 자원(URI)에 대한 CRUD Operation을 적용하는 것을 의미한다.
2. REST 구성 요소
    - **자원(Resource) : HTTP URI**
    - **자원에 대한 행위(Verb) : HTTP Method**
    - **자원에 대한 행위의 내용 (Representations) : HTTP Message Pay Load**
3. REST의 특징
    - Server-Client(서버-클라이언트 구조)
    - Stateless(무상태)
    - Cacheable(캐시 처리 가능)
    - Layered System(계층화)
    - Uniform Interface(인터페이스 일관성)
4. RESTful
    
    > **RESTFUL이란 REST의 원리를 따르는 시스템을 의미한다. 하지만 REST를 사용했다 하여 모두가 RESTful 한 것은 아니다.  REST API의 설계 규칙을 올바르게 지킨 시스템을 RESTful하다 말할 수 있으며,**
    > 
    > 
    > **모든 CRUD 기능을 POST로 처리 하는 API 혹은 URI 규칙을 올바르게 지키지 않은 API는 REST API의 설계 규칙을 올바르게 지키지 못한 시스템은 REST API를 사용하였지만 RESTful 하지 못한 시스템이라고 할 수 있다.**
    > 

### Queryset

> 쿼리셋(QuerySet)은 **전달받은 모델의 객체 목록**
> 

쿼리셋은 데이터베이스로부터 데이터를 읽고, 필터를 걸거나 정렬을 할 수 있다.

### django Manager
> Django 모델에 데이터베이스 쿼리작업을 제공하는 인터페이스