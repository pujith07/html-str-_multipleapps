from django.urls import path
from app1.views import *

app_name='something'

urlpatterns=[
    path('form/',form,name='form'),
    path('sample/',sample,name='sample'),
    path('main/',main,name='main'),
    path('pujith/',pujith,name='pujith'),
    path('rendering/',rendering,name='rendering'),
    path('process/',process,name='process'),
    path('creating/',creating,name='creating'),
]