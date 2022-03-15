"""mysite_django_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
'''
URL 처리 방법(ex. /polls/23/)
1. ROOT_URLCONF(project.urls, 지금 이 파일)로 요청보냄
2. polls/ 발견 -> 23/만을 polls.urls에 보냄(polls/urls.py)
3. poll.urls에 있는 <int:question_id>/와 일치하여, 결과적으로 deatil() 뷰함수가 호출된다. // detail()함수에 대해서는 나중에 알아보자
detail(request=<HttpRequest Ojbect>, question_id=23)
'''
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')), #include : 다른 URLconfs를 참조할 수 있도록 설정
]
