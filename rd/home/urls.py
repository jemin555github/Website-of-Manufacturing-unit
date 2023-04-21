from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path("about",views.about,name='About '),
    path("quality",views.quality,name='quality'),
    path("capabilities",views.capabilities,name='capabilities'),
    path("contact",views.contact,name='contact'),
    path("product",views.product,name='product'),
    # path("p2",views.p2,name='product'),
    # path("p3",views.p3,name='product'),
    # path("p4",views.p4,name='product'),
    # path("p5",views.p5,name='product'),
    # path("p6",views.p6,name='product'),
    # path("p7",views.p7,name='product'),
    # path("p8",views.p8,name='product'),

]  


    