from django.urls import path
from .import views
from .views import ( DetalleListView )


app_name='app_detalle' 

urlpatterns = [    
#    path('index/', views.index, name='index'),
    path('index/', DetalleListView.as_view(), name='list_detalle'),

]