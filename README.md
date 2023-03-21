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


## 새로 알게된 내용

### manage.py
* 여기에서 모든 설징이 결정된다.
~~~python
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
~~~
이 줄에서 settings 을 불러올 파일과 디렉토리를 정한다.

### setttings.py
* settings.py에서 allowed host는 test 환경이 아니라면 nginx서버를 활용해서 api 입력을 받는다.
* debug 가 true가 아니라면 host느 그냥 비워두는게 test 환경에 좋음

### urls.py

* url patterns 에서 현재 url 기준으로 route에 해당하는 원소가 오면  뒤에 있는 파일로 유도를 하는 방식이다.
* spring의 request mapping과 유사함. 단 root 폴더에 존재하는 

### 그 외 알게 된점

* 개발 서버는 요청이 들어올 때마다 자동으로 python 코드를 읽고 상태를 바꾸지만, 파일에 따라서 다르다.
* 고로 수정사항이 생기면 서버를 재가동하는 것이 정신건강에 좋다. 

