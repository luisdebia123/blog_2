from django.urls import path
from .import views
from .views import ( UsuariosListView, Create_Usuarios )


app_name='app_usuarios' 

urlpatterns = [    
#    path('index/', views.index, name='index'),
    path('index/', UsuariosListView.as_view(), name='list_usuarios'),
    path('crear/', Create_Usuarios.as_view(), name='create_usuarios'),
]