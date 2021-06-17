from django.urls import path
from .import views
from .views import ( EntradasListView, Create_Entradas )


app_name='app_entradas' 

urlpatterns = [    
#    path('index/', views.index, name='index'), 3 con función
    path('index/', EntradasListView.as_view(), name='list_entradas'),
    path('crear/', Create_Entradas.as_view(), name='create_entradas'),   
    


]