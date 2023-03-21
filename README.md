# 1주차 미션: Django 튜토리얼

## 스터디 자료
[1주차 : Django와 개발 환경 설정](https://motley-way-58c.notion.site/Django-67e5994dfebd429d882d)

## 미션
- [Writing your first Django app](https://docs.djangoproject.com/ko/3.2/intro/tutorial01/)의 Part 1~4 따라 합니다.
- 코딩의 단위를 기능별로 나누어 Commit 메시지를 작성합니다.
- 새롭게 알게 된 것을 정리합니다.

## 목표
- Django 의 MTV 패턴을 이해합니다.

## 기한
- 2023년 3월 25일 토요일


## 새로 알게 된 내용

### manage.py
* 여기에서 설정 파일을 불러오는 명령어가 있다.
* manage.py 에서 db를 시뮬레이션할 수 있는 shell 명령어 존재
* makemigration 과 migrate 명령어 존재

~~~python
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
~~~
이 줄에서 settings 을 불러올 파일과 디렉토리를 정한다.

### setttings.py
* settings.py에서 allowed host는 test 환경이 아니라면 ng nix 서버를 활용해서 API 입력을 받는다.
* debug 가 true가 아니라면 host는 그냥 비워두는 게 test 환경에 좋음
* setting에서 시간대와 언어를 바꾸는 것이 가능하다.
* INSTALLED APPS에는 미리 설치된 패키지뿐 아니라 개발자가 저장한 앱을 apps.py 에 존재하는 config 클래스를 받을 수 있다.

### urls.py

* URL patterns에서 현재 URL 기준으로 route에 해당하는 원소가 오면 뒤에 있는 파일로 유도하는 방식이다.
* spring의 request mapping과 유사함. 단 root 폴더에 존재하는 admin은 예외이다.
* URS 에서 name 파라미터의 쓰임새는 다음과 같다. 쉽게 말해서 view에서 역으로 URL을 참조할 수 있다.  [링크](https://stackoverflow.com/questions/12818377/django-name-parameter-in-urlpatterns)
* 앱이 하나라면 괜찮지만, 앱이 여러 개가 되면 URL 이름이 헷갈리기 때문에 app_name이라는 것을 정의 해줘야 한다.

### admin.py

* 각 app에 존재하는 admin.py 에서 해당 객체를 다음 코드로 등록할 수 있음 
~~~python
admin.site.register(객체)
~~~

### views.py

* httpresponse 객체를 브라우저에 돌려주는 역할을 한다.
* render 함수는 html을 받고, 해당하는 인자를 받아서 return 한다.
* 제너릭 뷰 [링크](https://ivans-story.tistory.com/91)

### migration

* migration을 하는 과정은 makemigrations과 migrate 두 단계로 진행된다.
* makemigrations는 장고에 알려주고, migrate가 실질적으로 migration이 적용된다.
* commit과 push의 관계를 생각하면 쉬울 것 같다.

### 제너릭 뷰

* 반복되는 작업을 피하고자 만든 클래스이다. view에서 활용하면 활용도가 높다.

### 기타

* 개발 서버는 요청이 들어올 때마다 자동으로 python 코드를 읽고 상태를 바꾸지만, 파일에 따라서 다르다.
* 고로 수정사항이 생기면 서버를 재가동하는 것이 정신건강에 좋다.
* datatime now보다는 timezone.now를 사용하는 것이 좋다. [timezone aware하게 datetime을 return 한다.](https://stackoverflow.com/questions/26949959/timezone-now-vs-datetime-datetime-now)
* post 명령을 수행할 때는 csrf token을 생성 해야한다.
* post data를 다루고 난 이후에는 HttpResponseRedirect 함수를 실행해야 한다.
* 객체에서 자신을 참조하는(자신을 외래키로 가지고 있는) 객체에 접근하기 위해서 (객체이름)_set 으로 접근한다.
* manage.py shell은 실시간으로 필드 값이 반영되지 않는다. 페이지에서 객체를 수정했다면 shell을 종료하고 재접속해야 필드 값 업데이트가 반영이 되는 것으로 보임

### 의문점

* 분명히 API를 restful 하게 만들기 위해서는 뒤에 슬래시(/) 를 붙이지 않는 것이 규칙이다.
* 하지만 장고 공식 문서는 다음과 뒤에 슬래시(/)를 붙이고 있는 이유를 알고 싶음
* 왜 붙이면 안 되는지는 [링크](https://yozm.wishket.com/magazine/detail/1347/) 에 나와 있음
* 스프링의 취약점이고 장고에는 상관이 없다는 이유에서 나온 코드인지 궁금함
* 장고 공식 홈페이지에서도 url 마지막에 슬래시(/)가 있는 것을 보면 장고의 특성인지 궁금함


### 추가로 작성한 코드

* polls/models.py 에서 pub_date를 생성자에서 인자로 받지 않고 객체가 생성될 때 자동으로 생성 시간을 설정
* polls/models.py 에서 modified_date를 설정해서 자동으로 최종 수정 일자를 기록하도록 설정하였다.
