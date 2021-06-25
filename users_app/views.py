from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import CustomRegsitrationForm
from django.contrib import messages


def register(request):
    if request.method == "POST":
        register_form = CustomRegsitrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("New User Account Created, Login to Get Started"))
            return redirect('register')

    else:
        register_form = CustomRegsitrationForm()
    return render(request,'register.html', {'register_form':register_form})