from django.urls import path
from app2.views import *

app_name='nothing'

urlpatterns=[
    path('sample/',sample,name='sample'),
    path('main/',main,name='main'),
    path('pujith/',pujith,name='pujith'),
    path('form/',form,name='form'),
]