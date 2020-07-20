from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as log_in, logout as log_out


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            log_in(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
        else:
            return redirect('/authorization/login/?next=/&error=true')
    else:
        return render(request, 'authentication/login.html')


def logout(request):
    log_out(request)
    return HttpResponse()
