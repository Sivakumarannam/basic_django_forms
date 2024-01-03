from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.


def create_forms(request):
    EFO=Forms()
    d={'djforms':EFO}
    if request.method=='POST':
        NFO=Forms(request.POST)
        if NFO.is_valid():
            return HttpResponse(str(NFO.cleaned_data))
        else:
            return HttpResponse('Not valid Data')
    

    return render(request,'create_forms.html',d)
