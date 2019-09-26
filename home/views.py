from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'pages/home.html')
def contact(request):
    return render(request,'pages/contact.html')
def error_404(request):
    data = {}
    return render(request,'pages/error.html', data)
def error_500(request):
    data = {}
    return render(request,'pages/error.html', data)