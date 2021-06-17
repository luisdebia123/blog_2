from django.urls import path
from .import views

app_name='app_blog_02' 

urlpatterns = [    
    path('', views.principal, name='principal'),

]