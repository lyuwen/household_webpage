"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^logout/', views.logout_request, name='logout_request'),
    url(r'^splogs/', include('splogs.urls')),
    url(r'^bills/', include('bills.urls')),
    #url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^account/', views.account, name='account'),
    url('^password_change/$', auth_views.password_change, name='password_change'),
    url('^password_reset/$', auth_views.password_reset, name='password_change'),
    url('^password_change/done$', views.password_change_done, name='password_change_done'),
    url('^password_reset/done$', views.password_change_done, name='password_reset_done'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""
from django.contrib.flatpages import views
# Your other patterns here
urlpatterns += [
    url(r'^(?P<url>.*/)$', views.flatpage),
]
"""
