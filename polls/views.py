from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request):
    return HttpResponse("<h1>Heelo world!</h1>")

def help(request):
    abc = {'var':'Tra'}
    return render(request, 'main.html', context=abc)

def cat(request):
    return render(request,'main.html', context=None)