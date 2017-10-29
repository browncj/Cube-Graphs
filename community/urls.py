from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='Community'),
    url(r'^chat/', views.chat, name='Chat'),
    url(r'^reddit/', views.reddit, name='Reddit'),
]
