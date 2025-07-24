from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('admin/', admin.site.urls),
    path('members/', views.members, name='members'),
    path('members/details/<slug:slug>', views.details, name='details'),
    path('members/add', views.add_member_form, name='add_member'),
    path('members/edit/<int:member_id>/', views.add_member_form, name='edit_member'),
    path('members/delete/<int:member_id>/', views.delete_member, name='delete_member'),
]