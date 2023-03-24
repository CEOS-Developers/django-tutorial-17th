# 1주차 미션: Django 튜토리얼

## 과제 내용 정리
### 뷰
* 정의: 특정 기능과 템플릿을 제공하는 웹 페이지의 한 종류
* 역할
  1. 요청된 페이지의 내용이 담긴 HttpResponse객체를 반환
  2. Http 404와 같은 에러를 발생
* URL로부터 뷰를 얻기 위해서는 URL패턴을 뷰에 연결시켜주는 URLconf를 사용한다.
  * URLconf를 생성하기 위해서는 urls.py라는 파일을 새로 만들어야 한다.
* Python 코드를 편집하지 않고 뷰의 페이지 디자인을 바꾸고 싶을 때 -> **Django의 템플릿 시스템**을 사용하여 Python 코드와 디자인을 분리
* 뷰가 HttpResponse객체를 반환할 때 render() 메소드를 사용하면, 아래와 같이 첫번째 인수로 request 객체, 두번째 인수로 템플릿의 이름, 세번째 인수로 context 사전형 객체를 넣어 최종적으로 **해당 템플릿의 HttpResponse객체를 반환**한다.
<pre>
<code>
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
</code>
</pre>
* Http404에러
  * get_object_or_404(객체, 키워드 인수): 키워드 인수에 해당하는 객체가 없을 경우, Http 404 예외 발생
### 제네릭 뷰 
* 일반적인 패턴을 추상화하여 앱을 작성하기 위한 도구
### path()
* path(' ', views.index,name='index')
  * 첫번째 인수(필수) = route(URL패턴을 가진 문자열, 여기서 공백인 이유는 디폴트, 즉 기본 웹페이지를 요구했기 때문)
  * 두번째 인수(필수) = view(해당 URL에 상응하는 view를 지정해준다)
  * 세번째 인수(선택) = kwargs(임의의 키워드 인수들은 해당 view에 사전형으로 전달된다)
  * 네번째 인수(선택) = name(URL에 이름을 붙여 어디에서나 명확하게 참조가 가능하도록 한다)
### include()
* 다른 URLconf를 참조할 수 있게 한다.
* 매번 공통되는 앞부분의 경로에, 뒷부분의 앱의 경로만 갖다붙여서 빠르게 이동할 수 있게 해준다.
* 언제 사용?
  * 다른 URL패턴을 포함할 때마다 항상 사용해야 한다.
* 브라우저에 "http://localhost:8000/polls/" 를 입력했을 때의 과정
  1. mysite/url.py 에 path('polls/',include('polls.urls')) 첫번째 인수인 polls/경로를 공통 경로로 인식
  2. 두번째 인수인 include('polls.urls') -> polls/urls.py파일로 넘어감
  3. path(' ', views.index, name='index') 이므로 다른 주소로 이동하지 않고, polls/views.py의 index라는 함수를 실행시킴
  4. 최종적으로 HttpResponse를 반환함
### 모델
* 정의: 어플리케이션에 사용될 데이터를 저장하기 위한 구조 역할
* 파이썬 클래스와 데이터베이스 테이블을 매핑할 때
  * Model: 데이터베이스의 테이블과 매핑
  * Model instance: 데이터베이스 테이블의 1 row(DB 인스턴스란 실체화된 값을 의미)
* 데이터베이스의 각 필드(테이블)는 field클래스의 인스턴스(속성)로서 표현됨
* charfield는 문자 필드를 표현함(=도메인) -> 어떤 자료형을 가질 수 있는지 알려줌
* 몇몇 field클래스는 필수 인수를 필요로 함
* 몇몇 field클래스는 선택적 인수를 가질 수 있음(default 지정시, 기본값이 0임)
* foreignkey를 가질 수 있음 -> 관계차수로는 1:1, 1:m, m:n 을 가질 수 있음
* makemigrations 명령어: 모델을 변경/추가한 사실을 알리고, 변경사항을 migration으로 저장시키고 싶다는 것을 Django에게 알림
* migrate 명령어: migration을 실행시키고, 데이터베이스 스키마를 관리
* <모델의 변경 3단계 지침>
  1. models.py 에서 모델을 변경
  2. python manage.py makemigrations을 통해 모델을 변경했다는 사실과 이 변경사항에 대한 migration을 만듦
  3. python manage.py migrate을 통해 변경사항을 데이터베이스에 적용함
## 추가한 부분
### DB 변경
* 기본적으로 제공되는 SQLite를 사용하지 않고, **MySQL**로 데이터베이스를 변경하였다.
* MySQL을 사용하기 위해서는 mysqlclient를 다운받아야 한다. 하지만 자꾸 에러가 나서 확인을 해보니 파이썬 버전 3.10부터는 mysqlclient가 지원되지 않는다는 사실을 깨닫게 되었다...ㅠ그래서 내가 현재 가지고 있는 파이썬을 모두 제거하고 버전 3.9로 다시 실행하여 성공적으로 데이터베이스를 바꿀 수 있었다. 
* 이 과정에서 settings.py에 추가한 DB에 관련된 개인정보들은 gitignore처리하여 github에 공개되지 않도록 하였다. 
