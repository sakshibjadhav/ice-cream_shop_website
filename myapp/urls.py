from django.contrib import admin
from django.urls import path,include
from myapp import views
urlpatterns = [
    path("", views.menu,name='menu'),
    path("menu/", views.menu,name='menu'),
    path("order/", views.order,name='order'),
    path("contact/", views.contact,name='contact'),

]