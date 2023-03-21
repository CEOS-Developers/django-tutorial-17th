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
- **애플 실리콘 (M1, M2)의 경우 추가적 설정이 필요하다 !!**
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

- /admin 페이지에서 관리하는거 쉽고 좋네요
- 전체적으로 코드들이 시원시원하니 직관적이네요

# 3장

### App

> GET localhost:8080/polls/34/

- mysite.urls에서 urlpatterns라는 변수를 찾는다.
- 'polls/'를 찾은 후엔, "34/"를 〈polls.urls〉 URLconf로 전달한다.
- "34" -> \<int:question_id> (question_id), 결과적으로 detail() 뷰 함수가 호출.
 
### Template

> polls/templates/polls/index.html

- 왜 templates 안에 polls 디렉토리 또 만들지?
- ..싶어서 경로상 polls를 뺐다. 다른 앱 만들고 중복 터지면 그 때 생각하기로 했다.


> template = loader.get_template('/index.html')

- 현재 polls/views.py다.
- (수정) 고집 부리려 했는데 암만 봐도 이후에 중복 문제가 터질 것 같아서 원복하였다.
- (결론) 공식 문서에 시비를 걸지 말자.

#### get_object_or_404

>  def detail(request, question_id):
> 
>   question = get_object_or_404(Question, pk=question_id)
>   return render(request, 'polls/detail.html', {'question': question})

- try-catch 구문을 축약시켜주는 라이브러리다. 좋다.
- get_object_or_404() 함수는 Django 모델을 첫번째 인자로 받고, 몇개의 키워드 인수를 모델 관리자의 get() 함수에 넘깁니다.
- 만약 객체가 존재하지 않을 경우, Http404 예외가 발생합니다.

### 템플릿에서 하드코딩된 URL 제거하기

- 하드코딩된 URL은 유지보수에 걸림돌이 되므로, 이러한 강력한 결합을 피한다.

### URL의 namespace

- polls/urls.py 파일에 app_name을 추가하여 어플리케이션의 네임스페이스 설정
