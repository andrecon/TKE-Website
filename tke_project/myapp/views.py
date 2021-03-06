from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Gallery
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
import json
# Create your views here.
from django.http import HttpResponse

# Built-in Django CreateView
from django.views.generic import ListView, CreateView 

#Handle the redirect back to our homepage 
from django.urls import reverse_lazy 

# Create your views here.
from django.http import HttpResponse
from . import forms
from . import models
from .forms import GalleryForm


def index(request):
    context = {
        "variable":"App",
        "title":"TKE",
    }
    return render(request, "index.html", context=context)

# A page representing a list of objects.
class GalleryView(ListView):
    model = Gallery
    template_name = 'index.html'

class CreateImageView(CreateView): 
    model = Gallery
    form_class = GalleryForm
    template_name = 'sections/photoPost.html'
    success_url = reverse_lazy('index')


def signup(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("/login/")
    else:
        form_instance = forms.RegistrationForm()
    context = {
        "form":form_instance,
    }
    return render(request, "registration/signup.html", context=context)

def logout_view(request):
    logout(request)
    return redirect("/login/")

def contact(request):
    context = {
        "username": str(request.user.username)
    }
    return render(request, "sections/contact.html",context=context)

def chat(request):
    
    return render(request,"sections/chat.html", {})

def room(request, room_name):
    return render(request,'sections/room.html',{
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username))
    })

def rush(request):
    if request.method == "POST":
        form_instance = forms.RushTke(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('/thanks')
    else:
        form_instance = forms.RushTke()
    context = {
        "form":form_instance,
    }
    return render(request, "sections/rush.html", context=context)

def thanks(request):
    return render(request,"sections/thanks.html", {})
