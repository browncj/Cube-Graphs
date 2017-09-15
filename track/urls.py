from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='Track'),
    url(r'^stats/', views.stats, name='Statistics'),
    url(r'^tables/', views.tables, name='Tables'),
    url(r'^charts/', views.charts, name='Charts'),
    url(r'solve-remove/([a-zA-Z0-9_-]+)?$', views.remove_solve, name='Solve-Remove'),
]
