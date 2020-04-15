from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<em>My second app</em>")


def help(request):
    helpdict = {'help_insert':'HELP PAGE!!!!'}
    return render(request, 'second_app/help.html',context=helpdict)