from django.shortcuts import render , redirect
from django.views.generic import CreateView , TemplateView , UpdateView , DeleteView , DetailView
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , authenticate , logout
from django.views.decorators.http import require_http_methods

class HomeView(TemplateView):
    template_name = 'users/home.html'

def register(req):
    if req.method == 'POST':
        form1 = UserForm(req.POST)
        form2 = RegisterForm(req.POST)
        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.set_password(form1.cleaned_data.get('password'))
            user.save()

            regi = form2.save(commit=False)
            regi.user = user
            regi.save()

            return redirect('login')
    else:
        form1 = UserForm()
        form2 = RegisterForm()
    return render(req , 'users/register.html' , {'form1':form1 , 'form2':form2})


@require_http_methods(["GET", "POST"])
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'users/login.html')

    
@login_required
def logout_user(req):
    logout(req)

    return redirect('home')