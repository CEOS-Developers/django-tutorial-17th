# 1주차 미션: Django 튜토리얼

## 스터디 자료
[1주차 : Django와 개발 환경 설정](https://motley-way-58c.notion.site/Django-67e5994dfebd429d882d4b2b0e58e6a0)

## 미션
- [Writing your first Django app](https://docs.djangoproject.com/ko/3.2/intro/tutorial01/)의 Part 1~4 따라합니다.
- 코딩의 단위를 기능별로 나누어 Commit 메세지를 작성합니다.
- 새롭게 알게 된 것을 정리합니다.

## 목표
- Django 의 MTV 패턴을 이해합니다.

## 기한
- 2023년 3월 25일 토요일  

<br/>

# 📚Django-tutorial 내용 정리
## Part1
### 프로젝트 생성하기

<pre><code>$ django-admin startproject [project_name]</code></pre>

<pre><code>
[project_name]/
      manage.py
      [project_name]/
          __init__.py
          settings.py
          urls.py
          asgi.py
          wsgi.py
</code></pre>

<div align=left>
  <li> manage.py ⇒ 프로젝트 진행에서 필요한 여러 기능들이 들어간 utility 파일</li>
  <li>__init__.py: Python으로 하여금 이 디렉토리를 패키지처럼 다루라고 알려주는 용도의 단순한 빈 파일</li>
  <li>settings.py: Django 프로젝트의 환경 및 구성을 저장</li>
  <li>urls.py: 어떤 path를 어디로 연결해줄지 routing 해주는 역할</li>
  <li>asgi.py: 프로젝프로젝트를 제공하기 위한 ASGI 호환 웹 서버의 진입점</li>
  <li>wsgi.py: 프로젝트를 서비스하기 위한 WSGI 호환 웹 서버의 진입점</li>
  
<br/>
  
### 개발 Sever 동작 시키기
  
<pre><code>$ python manage.py runserver </code></pre>
  
  <li> 자동 변경 기능: 개발 서버는 요청이 들어올 때마다 자동으로 Python 코드를 다시 불러와 반영(파일을 추가하는 등의 몇몇의 동작은 서버 재가동 필요)</li>
  
### 포트 변경하기
  
<pre><code>$ python manage.py runserver 포트번호</code></pre>
  
### 서버의 IP와 포트 모두 변경하기
  
<pre><code>$ python manage.py runserver 서버의 IP: 포트번호</code></pre>
  
<br/>

### 생성된 View를 Path로 연결 짓기(URLconf)
  
  <li>views.py: 뷰를 생성 및 보관</li>
  <li>urls.py: 경로 설정</li>
  <li>include(): 다른 URLconf들을 참조 가능하게 해줌(현재까지의 경로외에 남은 경로부분을 include 된 URLconf로 전달)</li>

<br/>
  
### Path() 인수
  
  <li>route: URL 패턴을 가진 문자열(경로)</li>
  <li>view: HttpRequest 객체를 첫번째 인수, 전달받은 data를 두번째 인수로하여 특정한 view 함수를 호출</li>
  <li>kwargs: 임의의 키워드 인수들을 목표한 view 에 사전형으로 전달</li>
  <li>name: URL의 이름, 템플릿을 포함한 Django 어디에서나 명확하게 참조 가능</li>

<br/>
  
<br/>
  
## Part2
### Settings.py

  <li>MySQL 연결하기</li>
  
  <pre><code>
  # 연결을 위한 패키지 설정
  import pymysql
  pymysql.install_as_MySQLdb()
  </code></pre>

  <pre><code>
  # 개발환경 기준
  DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "django_study",
        'USER': Mysql 계정명,
        'PASSWORD': Mysql 비밀번호,
        'HOST': '127.0.0.1',
        'PORT': 포트번호,
      }
  }
  </code></pre>
  
#### INSTALLED_APPS: 현재 활성화된(=사용되는) 모든 Django 어플리케이션들의 이름들
  
  <li>django.contrib.admin – 관리용 사이트</li>
  <li>django.contrib.auth – 인증 시스템</li>
  <li>django.contrib.contenttypes – 컨텐츠 타입을 위한 프레임워크</li>
  <li>django.contrib.sessions – 세션 프레임워크</li>
  <li>django.contrib.messages – 메세징 프레임워크</li>
  <li>django.contrib.staticfiles – 정적 파일을 관리하는 프레임워크</li>

<br/>
  
### Model 만들기
  
  <li>Model: 메타데이터를 가진 데이터베이스의 구조(layout)</li>
  <li>데이터베이스의 각 필드는 Field 클래스의 인스턴스로서 표현</li>
  
 <pre><code>
  from django.db import models
  
  # Question 테이블과 question_text, pub_date 속성들 생성
  
  class Question(models.Model):
      question_text = models.CharField(max_length=200)
      pub_date = models.DateTimeField('date published')
 </code></pre>

### Model 활성화 
  <li> INSTALLED_APPS 설정에 추가</li>
  
  <code><pre>
  INSTALLED_APPS = [
   'polls.apps.PollsConfig',
   ...
  ]
  </code></pre>
  
  <li> 변경사항에 대한 migration 생성</li>
    
  <code><pre>
  $ python manage.py makemigrations [app_name]
  </code></pre>
    
  <li> 변경사항을 DB에 적용</li>
    
  <code><pre>
   $ python manage.py migrate
  </code></pre>
 
    
### API 가지고 놀기(DB 접근하기)
<code><pre>
$ python manage.py shell
</code></pre>
    
### 관리자 사이트 이용하기
    
  <li> 관리자 계정 생성 시작하기 </li>
  
   <code><pre>
   $ python manage.py createsuperuser
    
   Username: [계정 ID]
    
   mail address: [Email]
    
   Password: **********
   Password (again): *********
 </code></pre>
 
<li> 권한 부여하기 </li>

 <code><pre>
     # [app_name]/admin.py
    
   from django.contrib import admin
   from .models import Question

   admin.site.register(Question)
 </code></pre>
  
<li> 관리자 사이트: http://127.0.0.1:8000/admin/  </li>

<br/>

<br/>

## Part3
### View 에서 Template 반환하기
  
<li> templates 디렉토리 생성하기  </li>
  
 <pre><code>
[project_name]/
      [app_name]/
          templates/
            # app_dir 템플릿 로더 작동하는 방식 때문
            /[app_name]
              /[template_name].html
          ...
 </code></pre>

<li> render()를 통해 HttpResponse로 templates 반환하기 </li>
  
 <pre><code>
 ...
 # context => template에 전달할 data
 return render(request, '[app_name]/[template_name].html', context)
 </code></pre>

<br/>

<br/>

## Part4
### Generic View
<li> Url에 따른 Data 반환, Template 반환과 같은 일반적인 패턴을 추상화한 Django의 shortcut </li>
<li> 각 제너릭 뷰는 어떤 모델이 적용될 것인지를 알아야하기에 model 속성을 사용하여 제공 </li>
 <pre><code>
 urlpatterns = [
    ...
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    ...
 ]
 </code></pre>
 
 <pre><code>
 from django.views import generic
 
 # 전달받은 Url의 key 값으로 data가 반영된 template을 불러오기 위해 Model 설정 및 templat_name 설정
 class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
 </code></pre>
