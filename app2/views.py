from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sample(request):
    return render(request,'sample.html')
def main(request):
    return render(request,'main.html')
def pujith(request):
    return HttpResponse('<h1><marquee>hai pujith available html pages are form, sample, main</marquee></h1>')
def form(request):
    return render(request,'form.html')