from django.shortcuts import render

# Create your views here.

def conditions(request):

    d={'a':1000,'b':2000,'c':3000}

    return render(request,'conditional.html',d)
