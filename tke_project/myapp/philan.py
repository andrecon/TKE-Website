from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    context = {
        "variable":"App",
        "title":"TKE",
    }
    return render(request, "sections/philanthropy.html", context=context)