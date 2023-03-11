from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def form(request):
    return render(request,'form.html')
def sample(request):
    return render(request,'sample.html')
def main(request):
    return render(request,'main.html')
def pujith(request):
    return HttpResponse('<h1><marquee>hai pujith available html pages are form, sample, main</marquee></h1>')
def rendering(request):
    return HttpResponse('<h1>Rendering is a process of interacting with templates and extracting the specified html page to the function</h1>')
def process(request):
    return HttpResponse('<h3> First we enter the url in browser then browser will send the http request to settings.py file but settings.py is not a right file to handle the request to then it wents to urls.py file from settings.py ,,, in urls.py we have did the urlmapping so it will check the suffix which will match,,after matching directly it will go to the views.py file here some rendering process will happen,,after extracting the specified html page back to function then function will directly return the response to the browser</h3> ')
def creating(resquest):
    return HttpResponse('<h3> First we want to create the project then we need to create application after that create one template folder then register in settings.py file ,, for created apps go to  INSTALLED APPS then register,,for  templates import os  then create one varibale as TEMPLATES_DIR=os.path.join(BASE_DIR,"templates") then go to TEMPLATES then inside DIRS=[TEMPLATES_DIR]</h3>')