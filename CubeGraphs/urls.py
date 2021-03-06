"""CubeGraphs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from CubeGraphs import views as top_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', top_views.base, name='base'),
    url(r'^about/', include('about.urls')),
    url(r'^profile/', include('userProfile.urls')),
    url(r'^timer/', include('timer.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^community/', include('community.urls')),
    url(r'^track/', include('track.urls')),

    url(r'^login/', auth_views.login, name='login'),
    url(r'^logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/', top_views.signup, name='signup'),
    url(r'^changepass/', top_views.change_pass, name='change_pass')
]
