from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('admin/', admin.site.urls),
    path('members/', views.members, name='members'),
    path('members/details/<slug:slug>', views.details, name='details'),
]