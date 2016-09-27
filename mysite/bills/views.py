from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    if not request.user.is_authenticated: return redirect('/')
    inp=[[ss.strip() for ss in s.split("|")] for s in open("files/bill_data.txt") if s.strip()[0]!='#']
    if len(request.user.first_name) > 0: uName=request.user.first_name
    else: uName=request.user.username
    t = loader.get_template('generic.html')
    c = RequestContext(request,{'inp':inp, 'login_logout': "Logout", 'username': uName, 'user': request.user})
    return HttpResponse(t.render(c), content_type="application/xhtml+xml")
