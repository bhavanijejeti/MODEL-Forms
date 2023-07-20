from django.shortcuts import render
# Create your views here.
from app1.forms import *
from django.http import HttpResponse
def inserttopic(request):
    tmfo=Topicmodelform()
    d={'tmfo':tmfo}
    if request.method=='POST':
        tmfod=Topicmodelform(request.POST)
        if tmfod.is_valid():
            tmfod.save()
            return HttpResponse('data is inserted')
    return render(request,'inserttopic.html',d)

def insertwebpage(request):
    wbo=Webpagemodelform()
    d={'wbo':wbo}
    if request.method=='POST':
        wbo=Webpagemodelform(request.POST)
    if wbo.is_valid():
        wbo.save()
        return HttpResponse('wbo is submited')
    return render(request,'insertwebpage.html',d)

def insertar(request):
    aro=AccessRecordmodelform()
    d={'aro':aro}
    if request.method=='POST':
        aro=AccessRecordmodelform(request.POST)
    if aro.is_valid():
        aro.save()
        return HttpResponse('aro is submited')
    return render(request,'insertar.html',d)

