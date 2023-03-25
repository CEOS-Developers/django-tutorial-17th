# django-tutorial-17th
CEOS 17th Backend 1st Study


---
### django tutorial
가상환경 설정하는데 어려움이 있었다. pycharm에서는 interpreter를 이용하여 가상환경을 설정할 수 있는데, 현재 경로로 설정해도 가상환경이 실행이 안됐다.

https://domythang.tistory.com/463

위 링크를 참고하여 해결했다.

commit을 할 때 django-admin startproject로 만든 파일이 올라간다. .gitinore 파일이나 requirements.txt 파일이 안올라가서 따로 commit해서 올려주었다. 

commit 제목은 나름의 규칙으로 하려고 했는데 계속 잊는다..

---
### django part1
- 최상위 URLconf에서 polls앱의 URLconf를 참고하도록 inculde()함수를 이용하였다. 
- polls/urls.py 에서는 path()함수로 view를 호출했다. path()함수는 url 패턴을 가진 route, 호출할 view 함수 2가지 필수 인수가 있고 사전형으로 전달할 인수 kwargs, url의 이름 name 2가지 선택 인수가 있다.

---
### django part2
- settings.py의 DATABASE default 항목을 바꾸는 것으로 database를 바꿀 수 있다. django의 기본 database인 SQLite를 사용하지 않으면 이부분과 user, password, host의 추가 설정이 필요하다.
- polls앱의 모델을 만들었다. ```python manage.py sqlmigrate polls 0001``` 명령어를 이용하여 데이터베이스가 어떻게 관리되는지와 조건 등을 확인할 수 있다.

---
### django part3
- render()함수는 loader와 HttpResponse 를 쉽게 표현하게 해준다. requeset 객체를 첫번째 인수, 템플릿 이름을 두번째 인수, 사전형 객체를 세번째 선택적 인수로 받는다. 
- get_object_or_404()함수를 이용하여 객체를 받거나 존재하지 않으면 404에러를 쉽게 일으킬 수 있다.
- template에서 **00_set**을 이용하여 외래키에 대한 테이블 정보를 가져올 수 있다.
- ```{% for choice in question.choice_set.all %}``` question과 연결된 외래키 choice 모델을 _set을 이용하여 가져오는데, 모든 정보를 가져오기 위해 .all을 붙였다.
- ```<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>```url의 name을 설정하면 이렇게 짧게 사용할 수 있다. 특히 '앱 이름 : url name'으로 설정해주면 다른 앱에서 url name이 겹쳐도 괜찮다! 

---
### django part4
```
<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
<fieldset>
    <legend><h1>{{ question.question_text }}</h1></legend>
    {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
    {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
        <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
    {% endfor %}
</fieldset>
<input type="submit" value="Vote">
</form>
```
- method POST 방식으로 폼을 제출하면 POST 데이터 choice='선택한 항목의 ID'를 제출한다.
- 프론트를 잘 몰라서 헷갈렸는데, POST 제출을 통해 실질적으로 전달되는 값은 **value값**이다! id의 값은 label을 붙이기 위해 같게 설정한 값이다.
- forloop.counter는 for문을 반복한 횟수이다. 임의의 Qusetion와 연결된 Choice의 갯수가 3이라면 for 문을 3번 반복할 것이고, forloop.count값은 1, 2, 3 순으로 적용된다.
- **POST 폼을 사용할 때는 보안때문에 {% csrf_token %}을 꼭 써줘야 한다.**

```
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
 ```
- vote view는 일단 request를 받으면 해당하는 Question을 받아온다. 또, 받아온 Question의 Choice 항목을 _set을 이용해 selected_choice에 담는다.
- request.POST는 선택된 설문의 ID를 문자열로 반환한다. 만약 choice가 없으면 오류를 일으키고 error_message를 보낸다. 이것을 template에서 if문으로 보여주었다.
- POST항목을 성공적으로 처리했으면 HttpResponseRedirect를 반환한다. 이때 reverse() 함수를 이용하여 url을 직접 쓰지 않도록 한다.

```
from django.views import generic
from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
```
- generic view를 이용하여 더 쉽게 표현할 수 있다. gengeric view는 model='사용될 모델'을 이용하여 적용될 모델을 제공한다.
- DetailView는 기본적으로 <앱 이름>/<모델 이름>_detail.html을 사용하지만 template_name 설정을 통해 바꿀 수 있다. ListView도 마찬가지로 바꿀 수 있다.
- DetailView는 URL의 기본 키값이 PK라고 생각하므로 path의 인수 값을 <int:pk>로 바꿔준다.
- ListView는 Question 변수가 자동으로 제공되는데, 본래의 변수 이름은 object_list이지만 context_object_name을 이용하여 변수 이름을 바꿀 수 있다.
- ListView에서 따로 모델 설정을 해주지 않았는데, get_queryset()함수를 오버라이딩하여 최근에 작성된 5개의 Question을 가져와 model로 쓰도록 했다. 동적으로 사용하기 위해서는 def 로 queryset을 불러올때마다 return해야 한다. [참고](https://kgu0724.tistory.com/98)

| 이름                  | 속성                 | 디폴트값               |  
|:-------------------:|:------------------:|:------------------:|
| model               | 사용할 모델             |                    |  
| template_name       | 렌더링할 template 지정   | 앱이름/모델이름_list.html |   
| context_object_name | template에서 사용할 변수명 | object_list        | 
| ordering            | 생성일 정렬             |                    |   
| paginated_by        | 한 페이지에 보여줄 페이지 수   |                 
| page_kwargs         | 쿼리 스트링의 페이지 키워드    |                     
- ListView의 편리한 속성들이다.
- DetailView는 여기에 url.py의 path 함수로부터 전달받을 pk의 키워드 이름을 작성하는 pk_url_kwarg만 추가된다.

---
### 추가 및 후기
- detail.html에서 index.html로 가는 버튼 추가했다. 왔다갔다 하기 귀찮음
- 투표가 마이너스가 되면 안되니까 intergerfield를 positiveinterfield로 바꿔줬다.
- 다른 데이터베이스 사용해보고싶었는데 보안때문에 .env파일 생성하고 이것저것 하다보니 너무 복잡해졌다. postgresql을 사용하려했는데 연결이 계속 안된다. 왤까...좀 더 찾아보고 다시 시도해봐야 될거같다..
