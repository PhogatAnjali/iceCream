from django.http.response import HttpResponse
from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable1":"Anjali is Great",
        "variable2":"Neeraj is Great"
    }
    return render(request,'index.html',context)
    # return HttpResponse("This is HomePage!")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("This is AboutPage!")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("This is ServicesPage!")

def contact(request):
    return render(request,'contact.html')
    #return HttpResponse("This is ContactPage!")