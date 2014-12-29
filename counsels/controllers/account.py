from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def login(request):
    return render(request, 'account/login.html')
