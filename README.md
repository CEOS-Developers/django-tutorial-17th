# 1주차 미션: Django 튜토리얼
___
# 1장

## Project vs App

- App: a Web application that does 'something'
- Project: a collection of configuration and apps for a particular website

> Project 
> > App
> 
> > App

### Command for Creating an app
> $ python manage.py startapp polls

### include()를 통한 URL 매핑
- 각각의 App 안에 urls.py 파일을 만들고 메인 urls.py 파일에서 각 App의 urls.py 파일로 URL 매핑을 위탁하게 할 수 있다. 
```
path('polls/', include('polls.urls')),
```
- 이러한 URL 매핑 방식은 특히 다수의 App들을 포함하는 큰 프로젝트의 경우 편리한 방식이다.
- URL 매핑 시 **중복에 주의**한다.

### path()의 인수: name
```
path('', views.index, name='index'),
```
- path 함수의 파라미터로 name='index'가 들어가있다.
- (옵셔널) 이 이름은 해당 URL을 참조할 때 사용되며, 코드의 가독성과 유지 보수성을 높일 수 있음.
- reverse('index') 함수를 사용하여 views.index 함수에 해당하는 URL을 생성.
___
# 2장

### Database
- MySQL을 사용하였다.
- **애플 실리콘 (M1, M2)의 경우 추가적 설정이 필요하다 !!**
> $ pip install pymysql

pymysql을 설치해주는 명령어
``` 
import pymysql  
pymysql.install_as_MySQLdb()
```

setting.py 에 상기 코드를 추가해준다.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # use mysql
        'NAME': env('DB_NAME'),
        'USER': env('DB_USERNAME'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
settings.py의 DATABASE를 다음과 같이 수정해준다. ( .env에 환경설정 분리 저장하였다. )<br>
[.env 환경설정 분리 저장하는법 by Alice Ridgway](https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f)


### Database - Flow

- polls/models.py에서 모델을 만든다
- mysite/settings.py -> INSTALLED_APPS 에 PollsConfig을 등록한다
> $ python manage.py makemigrations polls
> 
> $ python manage.py sqlmigrate polls 0001
> 
> $ python manage.py migrate
- 이렇게 migrate 하면 데이터베이스에 등록된다

- /admin 페이지에서 관리하는거 쉽고 좋네요
- 전체적으로 코드들이 시원시원하니 직관적이네요
___
# 3장

### App

> GET localhost:8080/polls/34/
- 다음과 같은 GET 요청이 들어온다고 가정하자.
- mysite.urls에서 urlpatterns라는 변수를 찾는다.
- 'polls/'를 찾은 후 남은 텍스트 '34/'를 <polls.urls> URLconf로 전달하여 남은 처리를 진행한다.
- '\<int:question_id>/'와 일치하여, 결과적으로 detail() 뷰 함수가 호출된다.
 
### Template

> polls/templates/polls/index.html

- 왜 templates 안에 polls 디렉토리 또 만들지?
- ..싶어서 경로상 polls를 뺐다. 다른 앱 만들고 중복 터지면 그 때 생각하기로 했다.


> template = loader.get_template('/index.html')

- 현재 polls/views.py다.
- (수정) 고집 부리려 했는데 암만 봐도 이후에 중복 문제가 터질 것 같아서 원복하였다.

#### get_object_or_404

```
def detail(request, question_id):
 
   question = get_object_or_404(Question, pk=question_id)
   return render(request, 'polls/detail.html', {'question': question})
```

- try-catch 구문을 축약시켜주는 라이브러리다.
- get_object_or_404() 함수는 Django 모델을 첫번째 인자로 받고, 몇개의 키워드 인수를 모델 관리자의 get() 함수에 넘긴다.
- 만약 객체가 존재하지 않을 경우, Http404 예외가 발생한다.

### 템플릿에서 하드코딩된 URL 제거하기

- 하드코딩된 URL은 유지보수에 걸림돌이 되므로, 이러한 강력한 결합을 피한다.

### URL의 namespace

- polls/urls.py 파일에 app_name을 추가하여 어플리케이션의 네임스페이스 설정
___
# 4장

- 4장은 전반적으로 코드 다듬기 느낌이네요.
- view.py: 
```
print(question.choice_set)
``` 

- 선택지 없이 choice_set을 찍어보면 polls.Choice.None이 나온다.
- 이 때 .get()을 하면 에러(KeyError: 'choice')가 터지기 때문에 try-except 구문을 실행한다.
___
# Overview
## MTV (Model, Template, View)

|      MVC      |     MTV     |
|:-------------:|:-----------:|
|    `Model`    |   `Model`   |
|    `View`     | `Template`  |
| `Controller`  |   `View`    |

- 다른 프레임워크에서 보던 MVC와 대응하는 개념이다.
<br><br>
- Model: DB에 저장하는 데이터로, 장고 ORM 매핑을 통해 파이썬으로 DB 관리 가능
- Template: 유저에게 보여지는 화면을 의미 
  - Django Template 문법을 이용해 html 파일 내에서 context로 받은 데이터를 활용할 수 있음
- View: 로직 수행 역할을 한다

### URLConf (URL 설계)
- URL 패턴을 정의하여 해당 URL과 뷰를 매핑하는 단계
```
from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
]
```
- 이처럼 path 함수를 이용해 URL을 뷰와 손쉽게 매핑시킬 수 있음


