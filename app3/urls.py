from django.urls import path
from app3.views import *

app_name='pujith'

urlpatterns=[
    path('main/',main,name='main'),
    path('sample/',sample,name='sample'),
    path('form/',form,name='form'),
    path('pujith/',pujith,name='pujith'),
]