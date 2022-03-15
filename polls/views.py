from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

'''
    Listview와 DetailView의 두가지 제너릭 뷰 사용중, 각각 "개체 목록 표시", "특정 개체 유형에 대한 세부 정보 페이지 표시" 개념을 추상화함.

    튜토리얼의 이전 부분에서 템플릿은 question 및 latest_question_list 컨텍스트 변수를 포함하는 컨텍스트와 함께 제공되었습니다. DetailView 의 경우 question 변수가 자동으로 제공되는데, 이는 우리가 Django 모델(Question)을 사용하고 있기 때문에 Django가 컨텍스트 변수의 적절한 이름을 결정할 수 있습니다. 그러나 ListView의 경우 자동으로 생성되는 컨텍스트 변수는 question_list``입니다. 이것을 덮어 쓰려면 ``context_object_name 속성을 제공하고, 대신에 latest_question_list 를 사용하도록 지정하십시오. 새로운 기본 컨텍스트 변수와 일치하도록 템플릿을 변경할 수도 있지만, 원하는 변수를 사용하도록 Django에게 지시하는 것이 훨씬 쉽습니다.??이해불가..
    아래 읽어보기.
    https://akpark.tistory.com/34
'''

class IndexView(generic.ListView):
    template_name = 'polls/index.html' #default value : <app_name>/<model_name>_list.html, which is polls/question_list.html #왜 question??
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question 
    template_name = 'polls/detail.html' #default value : <app_name>/<model_name>_detail.html, which is polls/question_detail.html #왜?? question??


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.