from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='Profile'),
    url(r'^update_mail/', views.update_mail, name='Add Mail'),
]