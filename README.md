# 1주차 미션: Django 튜토리얼

# 1장

## Project vs App

- App: a Web application that does 'something'
- Project: a collection of configuration and apps for a particular website

> Project 
> > App
> 
> > App

### Command for Creating an app
> python manage.py startapp polls

### include()를 통한 URL 매핑
- 각각의 App 안에 urls.py 파일을 만들고 메인 urls.py 파일에서 각 App의 urls.py 파일로 URL 매핑을 위탁하게 할 수 있다.
> path('polls/', include('polls.urls')),
- 이러한 URL 매핑 방식은 특히 다수의 App들을 포함하는 큰 프로젝트의 경우 편리한 방식이다.
- URL 매핑 시 **중복에 주의**한다.

### path()의 인수: name
> path('', views.index, name='index'),
- path 함수의 파라미터로 name='index'가 들어가있다.
- (옵셔널) 이 이름은 해당 URL을 참조할 때 사용되며, 코드의 가독성과 유지 보수성을 높일 수 있음.
- reverse('index') 함수를 사용하여 views.index 함수에 해당하는 URL을 생성.

# 2장

### Database
- MySQL을 사용하였다.
- 애플 실리콘의 경우 추가적 설정이 필요하다 !!
> pip install pymysql

pymysql을 설치해주는 명령어
> import pymysql  
pymysql.install_as_MySQLdb()

setting.py 에 상기 코드를 추가해준다.

### Database - Flow

- polls/models.py에서 모델을 만든다
- mysite/settings.py -> INSTALLED_APPS 에 PollsConfig을 등록한다
> $ python manage.py makemigrations polls
> 
> $ python manage.py sqlmigrate polls 0001
> 
> $ python manage.py migrate
- 이렇게 migrate 하면 데이터베이스에 등록된다

### 2장 느낀점..?

- /admin 페이지에서 관리하는거 쉽고 좋네요
- 전체적으로 코드들이 시원시원하니 직관적이네요
