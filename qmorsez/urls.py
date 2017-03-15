from django.conf.urls import url
from . import views

app_name='qmorsez'

urlpatterns =[
    url(r'^$', views.index,name='qmorsez'),
]
