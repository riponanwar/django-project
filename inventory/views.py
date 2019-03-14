from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'index.html',{'name':'Anwar Hossain'})

def unda(request):
	return HttpResponse('<h1>Unda is always great</h1>') 