from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse("<h1>tech with Pawel! ! </h1>")

def v1(response):
    return HttpResponse("<h1>View V1! ! </h1>")

def v2(response, id):
    return HttpResponse("<h1>%s</h1>" %id)