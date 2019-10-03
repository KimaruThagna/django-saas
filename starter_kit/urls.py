"""KeenEye URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from . import views
app_name='starter_kit'
urlpatterns = [
    url(r'^$',views.Home, name='home'),
    url(r'^logout/$',views.GoodBye, name='logout'),
    url(r'^home/$',views.Landing, name='landing'),
    url(r'^charge/$',views.app_charge, name='charge'),
    url(r'^uploads/$',views.UploadPage, name='uploads'),
    url(r'^upload-request/$',views.Uploadform, name='uploadform'),
    url(r'^results/(?P<id>.+)$',views.ResultsPage, name='results'),
    url(r'^processing/(?P<requestNum>.+)/$',views.process_image, name='process'),
]
