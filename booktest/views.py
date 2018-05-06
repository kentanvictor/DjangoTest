from django.http import *
from django.template import RequestContext,loader
from django.shortcuts import render

# Create your views here.
from booktest.models import *


def index(request):
    booklist = BookInfo.objects.all()
    context = {'list':booklist}
    return render(request,'booktest/index.html',context)


def show(request,id):
    book = BookInfo.objects.get(pk=id)
    herolist=book.heroinfo_set.all()
    context1 = {'list':herolist}
    return render(request,'booktest/show.html',context1)