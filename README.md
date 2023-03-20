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

# 일단 settings.py에서 allowed_host는 test 환경이 아니면 nginx를 활용해서 proxy server를 활용하는 방식이다.
# debug가 true가 아니라면 allowed host는 그냥 비워두는게 test 환경에 좋음


# #runserver 의 자동 변경 기능

# 개발 서버는 요청이 들어올 때마다 자동으로 Python 코드를 다시 불러옵니다. 코드의 변경사항을 반영하기 위해서 굳이 서버를 재기동 하지 않아도 됩니다. 그러나, 파일을 추가하는 등의 몇몇의 동작은 개발서버가 자동으로 인식하지 못하기 때문에, 이런 상황에서는 서버를 재기동 해야 적용됩니다.

# 일단 안전하게 코드르 추가하면 서버를 다시 키고 끄는게 좋다~

# urls.py에서 url patterns 에서 현재 url 기준으로 route에 해당하는 원소가 오면  뒤에 있는 파일로 유도를 하는 방식이다.

# spring의 request mapping과 유사하다고 할 수 있음
