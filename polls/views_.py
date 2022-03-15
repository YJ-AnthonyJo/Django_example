from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from polls.models import Question, Choice

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    print(context)
    return HttpResponse(render(request, 'polls/index.html',context)) #difference from third version : this version set template path using shortcuts.render
    #below : third version
    # lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'lastest_question_list': lastest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
    #below : second version
    # lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in lastest_question_list])
    # return HttpResponse(output)
    #below : first version 
    # return HttpResponse("Hello world. You're at the polls index.")

#below two functions(detail, results) are very similar(also index function is).
#these functions do following works : get data from DB, load templates, return rendered page..
#these works are very usual in web dev, so Django provide "generic views" shortcuts.
#for use generic views, I change this file name to views_.py and make new views.py which generic views are used.
def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id) # using shortcuts -> get object or 404 exception
    return render(request, 'polls/detail.html', {'question' : question})
    #below : second version
    # try:
    #     question = Question.objects.get(pk = question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question' : question})
    #below : first version
    # return HttpResponse("You're looking at question %s."%question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

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
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # 위 주석에도 나와있듯이, POST데이터를 성공적으로 처리한 후에는 항상 HttpResponseRedirect를 반환해야한다.
        # 이는 django에서 뿐만이 아니라, 일반적으로 좋은 웹 개발 관행이다.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        #reverse에 대해서는 후에 자세히 알아보자. 우선은 /polls/question.id/results/가 호출된다는 것만 알아두자