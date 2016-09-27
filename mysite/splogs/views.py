from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, render_to_response, redirect
from .models import Logs, Pmt
from .forms import LogsForm, PmtForm
from django.http import HttpResponse
from django.template import RequestContext, loader
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from compAve import SharedPurchase, getName
# Create your views here.

def index(request):
    if not request.user.is_authenticated: return redirect('/')
    if len(request.user.first_name) > 0: uName=request.user.first_name
    else: uName=request.user.username
    t = loader.get_template('index.html')
    c = RequestContext(request, {'login_logout': "Logout", 'username': uName, 'user': request.user})
    return HttpResponse(t.render(c), content_type="application/xhtml+xml")
@csrf_protect
def addlog(request):
    if not request.user.is_authenticated: return redirect('/')
    form = LogsForm()
    if request.POST:
        form = LogsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    if len(request.user.first_name) > 0: uName=request.user.first_name
    else: uName=request.user.username
    return render(request,'form.html', {'today': datetime.today().strftime("%Y-%m-%d"), 'form': form, 'name': getName(byName=str(uName)).title(), 'login_logout': "Logout", 'username': uName, 'user': request.user})
    #return render_to_response('addlog.html',{ 'form': form },RequestContext(request))

def viewlog(request):
    if not request.user.is_authenticated: return redirect('/')
    a=SharedPurchase(initWithPurchase=Logs.objects.all(), andPayment=Pmt.objects.all())
    text=str(a)+'\n'#+'-'+'\n'
    summary=text
    rawData=Logs.objects.order_by('-date')#[s.split() for strList]
    for s in rawData:
        s.name=getName(byName=s.name).title()
    #text.replace('\n','</br>')
    #return HttpResponse("<pre>%s</pre>"%text)
    if len(request.user.first_name) > 0: uName=request.user.first_name
    else: uName=request.user.username
    t = loader.get_template('view.html')
    c = RequestContext(request, {'sum': '{:.2f}'.format(a.sum), 'ave': '{:.2f}'.format(a.ave), 'indiv': a.getList(), 'rawData': rawData, 'login_logout': "Logout", 'username': uName, 'user': request.user})
    return HttpResponse(t.render(c))#, content_type="application/xhtml+xml")

@csrf_protect
def pay(request):
    if not request.user.is_authenticated: return redirect('/')
    form = PmtForm()
    if request.POST:
        form = PmtForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    if len(request.user.first_name) > 0: uName=request.user.first_name
    else: uName=request.user.username
    return render(request,'pmtform.html', {'today': datetime.today().strftime("%Y-%m-%d"), 'form': form, 'name': getName(byName=str(uName)).title(), 'login_logout': "Logout", 'username': uName, 'user': request.user})

def histpmt(request):
    if not request.user.is_authenticated: return redirect('/')
    rawData=Pmt.objects.order_by('-date')
    for s in rawData:
        s.fromN=getName(byName=s.fromN).title()
        s.toN=getName(byName=s.toN).title()
    if len(request.user.first_name) > 0: uName=request.user.first_name
    else: uName=request.user.username
    t = loader.get_template('viewHistPmt.html')
    c = RequestContext(request, {'rawData': rawData, 'login_logout': "Logout", 'username': uName, 'user': request.user})
    return HttpResponse(t.render(c), content_type="application/xhtml+xml")
