from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    my_dict = {'insert_me':"hello vrom veiws.py"}
    return render(request,'first_app/index.html',context=my_dict)

def index1(request):
    return HttpResponse("my project")