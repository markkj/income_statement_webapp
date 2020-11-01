from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm , UserLoginForm 
from django.http.response import HttpResponse , HttpResponseBadRequest
from api.views import query_transaction , today_report , get_all_total

@login_required(login_url='signin')
def index(request):
    hist_trans = query_transaction(request)
    todayreport = today_report(request)
    profilereport = get_all_total(request)
    return render(request , 'index.html',{
        'hist_trans':hist_trans,
        'today_report':todayreport,
        'profilereport':profilereport
    })

def signin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                request.session.set_expiry(86400)
                login(request, user)
                return redirect('/')
                
            else:
                response = "Password or username is incorrect.!!"
                return render(request, 'signin.html',{'form':form,'response':response})


    else:
        form = UserLoginForm()
    return render(request , 'signin.html',{'form':form})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            form.save()
            user = authenticate(username=username, password=raw_password)
            request.session.set_expiry(86400)
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request , 'signup.html',{'form':form})

def signout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('signin')
    else:
        response = "HTTP_405_METHOD_NOT_ALLOWED"
        return HttpResponseBadRequest()