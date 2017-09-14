from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='Timer'),
    url(r'^submit/', views.submit, name='Submit'),
    url(r'^scramble/', views.get_scramble, name='Get-Scramble'),
]
