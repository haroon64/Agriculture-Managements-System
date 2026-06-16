from django.shortcuts import render
from django.shortcuts import redirect, render
# Create your views here.

def landing_page(request):
    return render(request, 'pages/base.html')
