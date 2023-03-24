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

## 1주차 과제 정리
## part 1 ; 뷰
:장고 앱의 logic 담당(파일 다운로드 등)
* 뷰를 호출하기 위해서는 URL 코드를 작성하고, 뷰와 연결해주어야 한다. 사용되는 것이 URLconf이다. -> urls.py 파일 생성

* include() 함수를 사용하여 polls의 url을 참조하도록
<pre>
<code>
urlpatterns = [
    path('polls/', include('polls.urls')),
]
</code>
</pre>

#### 흐름
1. 최상위 URLconf(mysite urls.py)에서 우리가 작성한 URL을 연결해준다. 
예를 들어 127.0.0.1/polls/라는 url이 들어왔다면 이를 파싱해서 polls라는 해당 path를 잡아내고 polls,url로 연결시켜주는 것이다. 즉, path별로 다른 앱으로 분기를 시켜준다.
2. 
<pre>
<code>
urlpatterns = [
    path('', views.index, name='index'),
]
</code>
</pre>
polls 앱(polls urls.py)에서는 전달 받으면 /polls/ 이외에 아무것도 없음
3. 그럼 path 내에서 views.index는 view 내부로 연결시켜줌
4. 
<pre>
<code>
def index(request) :
    return HttpResponse(" -- ")
</code>
</pre>
view 내부의 index 함수에서는 " -- " Response를 클라이언트에게 전달
* path() 인수 : route(url 패턴 가진 문자열), view(경로로부터 특정한 뷰 함수를 호출) + kwargs, name(이름 지으면, 템플릿을 포함한 장고 어디서나 명확하게 참조)


## part 2 : 모델
다른 database를 사용하고 싶다면 settings.py 파일에서 이 부분을 변경해주면 된다.
저는 sqlite를 그대로 사용하였습니다 !

### 모델 : database의 구조
실습 앱에서는 Choice, Question 두 개의 모델을 클래스로 만듦. 
* Question 모델 - 질문, 출판 날짜
* Choice 모델 - 선택 텍스트, 투표 집계라는 필드를 가짐
* -> models.py 파일에 작성

** 새로 알게 된 점
* Choice의 모델의 ForeignKey(왜래키)
<pre>
<code>
question = models.ForeignKey(Question, on_delete=models.CASCADE
</code>
</pre>
* Choice 테이블 내의 question은 Question 테이블을 참조
* 하나의 Question에 여러 개의 Choice를 갖는 경우이기에 일대다
* CASCADE - Question이 삭제가 되면 Choice의 question도 삭제가 된다.

### 모델 활성화 
Migration? 모델의 변경 내역을 DB에 적용시키는 방법
1. setting.py에 polls.app.PollsConfig를 추가시켜 알려준다.
2. makemigration 명령어 - 모델을 변경했다는 사실, 변경사항에 대한 migration을 만듦
* Migration을 생성하는 명령어인데 뒤에 앱 이름을 입력하면 해당 앱에서만 마이그레이션 생성, 생략하면 전체 앱에 대해서 마이그레이션 생성
3. migrate 명령어 - migration 적용하는 명령어(즉 실제 DB에 변경사항을 적용하는)
* 이 외에 manage.py showmigrations [app_name]을 하면 프로젝트의 마이그레이션에 대해 적용여부를 한 눈에 보여줌

## part 3
 view에서는 request라는 인자를 받고, HttpResponse라는 함수를 리턴 하게 됨. 클라이언트에게 request를 받게 되면 안에 여러 정보가 담겨 있음.
 
* 뷰가 HttpResponse 반환 시 render() method 사용하면,
<pre>
<code>
def index(request):
    latest_question_list = Question.objects.order_by(-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
</code>
</pre>
* 1번째 인수로 request 객체
* 2번째 인수로 templete 이름
* 3번째 인수로 context 사전형 객체 넣어
* 최종적으로 HttpResponse 객체를 반환

### 404 에러
get_object_or_404(객체, 키워드 인수) : 키워드 인수에 해당하는 객체 없을 때 예외발생

## part 4 : 클래스 기반 뷰(소스코드 줄어듦)
### 제네릭 뷰
* 일반적인 패턴을 추상화하여 앱을 작성할 때 파이썬 코드를 작성하지 않도록 도움.
* URLconf 변환 -> 불필요한 오래된 보기 중 일부 삭제 -> 장고의 제네릭 뷰를 기반으로 새로운 뷰 도임