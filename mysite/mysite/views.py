from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

def index(request, msg=''):
    if request.user.is_authenticated:
        return redirect('/splogs')
    if request.POST:
        username = request.POST['user']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/splogs')
        else:
            return  render(request,'login.html', {'msg':'Invalid username or password!', 'login_logout': "Login"})
    return  render(request,'login.html', {'msg': msg, 'login_logout': "Login"})

def logout_request(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/', msg="Logout")

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })

def password_change_done(request):
    return redirect('/')

def account(request):
    if request.user.is_authenticated:
        return redirect('/password_change')
    else:
        return redirect('/')
        #return redirect('/password_reset')


