from django.urls import path
from .import views
from .views import ( CategoriasListView, Create_Categorias )


app_name='app_categorias' 

urlpatterns = [    
#    path('index/', views.index, name='index'),
    path('index/', CategoriasListView.as_view(), name='list_categorias'),
    path('crear/', Create_Categorias.as_view(), name='create_categorias'),


]