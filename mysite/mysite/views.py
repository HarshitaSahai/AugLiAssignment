from django.shortcuts import render, redirect
#from mysite.forms import uploadImage
from django.http import HttpResponse 
#from mysite.models import uploadImage
#from .forms import *
import sys
import requests

from subprocess import run,PIPE
def button(request):

    return render(request,'upload.html')



def external(request):

    # if(request.method == "POST"):
    #     form = uploadImage(request.POST, request.FILES)
    #     #pic=request.FILES.get('pic')
    #     #uploadImage(pic=pic)

    #     if(form.is_valid()):
    #         form.save()
    #     return HttpResponse('successfully uploaded')
    # #else:
    #     #form = uploadImage()

    inp= request.POST.get('pic')
    print(inp)
    out = run([sys.executable,'./mysite//image-to-text.py'],shell=True,stdout=PIPE)
    print(out)

    return render(request,'upload.html',{'data1': out.stdout})