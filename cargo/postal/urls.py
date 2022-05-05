from xml.etree.ElementInclude import include
from django.urls import path

from . import views 
urlpatterns= [
path('',views.home,name='home'),
path('login',views.login,name='login'),
path('signup',views.Userregestration,name='signup'),
path('services',views.services,name='services'),
path('home',views.home1,name='home1'),
path('Aboutus',views.Aboutus,name='Aboutus'),
path('booking',views.booking,name='booking'),

]