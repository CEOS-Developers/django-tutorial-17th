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

## 오류 해결
 - development server at http://127.0.0.1:8000/admin 이 주소값을 가진 페이지를 열게 하려면 python manage.py runserver를 해주어야 함
 - q.was_published_recently() 가 실행이 안됨 -> 새로운 터미널을 열어서 cd ./mysite 한 후 python manage.py shell을 다시 실행 해서 오류 해결
 - cd ../ : 현재 파일에서 빠져나와서 이전 파일로 나가는 명령어


## []
0) 깨달은 점
  다음부터는 part별로 commit 및 내용 정리를 해야겠다..

1) Django는 파이썬 기반이다.

2) 오류 해결한 것
   q.was_published_recently() 가 실행이 안됨 : 새로운 터미널을 열어서 cd ./mysite 한 후 python manage.py shell을 다시 실행 해서 오류 해결
   cd ../ : 현재 파일에서 빠져나와서 이전 파일로 나가는 명령어

3) HTTP
 : 컴퓨터들끼리 HTML파일을 주고받을 수 있도록 하는 소통방식 또는 약속(protocol)이다.
  클라이언트는 서버에게 request를, 서버는 response를 클라이언트에게 보낸다.

4) 가상환경에서 작업들을 수행한다.

5) No module named django : 장고 라이브러리가 설치가 안되어있음
   따라서 가상환경 구동(myenv), 장고 라이브러리 구축 해야함 
  
6) mysite라는 프로젝트 생성 (중요 : url&setting)
manage.py: Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인의 유틸리티 입니다. manage.py 에 대한 자세한 정보는 django-admin and manage.py 에서 확인할 수 있습니다.
mysite/ 디렉토리 내부에는 프로젝트를 위한 실제 Python 패키지들이 저장됩니다. 이 디렉토리 내의 이름을 이용하여, (mysite.urls 와 같은 식으로) 프로젝트의 어디서나 Python 패키지들을 임포트할 수 있습니다.
mysite/__init__.py: Python으로 하여금 이 디렉토리를 패키지처럼 다루라고 알려주는 용도의 단순한 빈 파일입니다. Python 초심자라면, Python 공식 홈페이지의 패키지를 읽어보세요.
mysite/settings.py: 현재 Django 프로젝트의 환경 및 구성을 저장합니다. Django settings에서 환경 설정이 어떻게 동작하는지 확인할 수 있습니다.
mysite/urls.py: 현재 Django project 의 URL 선언을 저장합니다. Django 로 작성된 사이트의 《목차》 라고 할 수 있습니다. URL dispatcher 에서 URL 에 대한 자세한 내용을 읽어보세요.
mysite/asgi.py: An entry-point for ASGI-compatible web servers to serve your project. See ASGI를 사용하여 배포하는 방법 for more details.
mysite/wsgi.py: 현재 프로젝트를 서비스하기 위한 WSGI 호환 웹 서버의 진입점입니다. WSGI를 사용하여 배포하는 방법를 읽어보세요.  

7) client가 web server에 요청 -> web server(nginx, apache)가 요청을 merge -> wsgi(web server와 장고 프레임웍을 연결)
-> request(client가 요청한 주소)가 url 파일에서 잘게 나누어짐(=파싱) ->view.py 데베작업 -> template(디자인 작업) -> 사용자가 response 받음 
-> wsgi -> client가 화면을 볼 수 있음
