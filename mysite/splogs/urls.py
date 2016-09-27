from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addlog/', views.addlog, name='addlog'),
    url(r'^viewlog/', views.viewlog, name='viewlog'),
    url(r'^pay/', views.pay, name='pay'),
    url(r'^histpmt/', views.histpmt, name='histpmt'),
]
