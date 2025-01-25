from django.contrib import admin
from django.urls import path, include
from paneladmin import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', views.loginpanel, name='loginpanel'),
    path('panelindex/', views.panelindex, name='panelindex'),
    path('logout/', views.signout, name='logout'),
]