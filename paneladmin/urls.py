from django.contrib import admin
from django.urls import path
from paneladmin import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', views.login),
    path('panelindex/', views.panelindex),
]