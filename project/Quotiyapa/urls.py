"""Quotiyapa URL Configuration
"""
from django.conf.urls import include,   url
from django.contrib import admin
from QuoteApp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name="home"),
    url(r'^add-quote/$', views.add_quote, name="add_quote"),
    url(r'^', include('registration.backends.hmac.urls')),
    url(r'^profile/(?P<username>[-\w.]+)/$', views.user_profile, name="user_profile")
]
