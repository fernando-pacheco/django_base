from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('imagem/<int:foto_id>', views.imagem, name='imagem'),
    path('nova-imagem/', views.nova_imagem, name='nova_imagem'),
    path('editar-imagem/<int:foto_id>', views.editar_imagem, name='editar_imagem'),
    path('deletar-imagem/<int:foto_id>', views.deletar_imagem, name='deletar_imagem'),
    path('buscar/', views.buscar, name='buscar'),

]