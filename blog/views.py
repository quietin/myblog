from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    html = "<html><body>abcd</body></html>"
    # return HttpResponse(html)
    return render(request, 'home.html')


def base(request):
    return render(request, 'base.html')