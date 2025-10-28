from django.urls import path
from . import views

urlpatterns = [
    path('add_contato/',views.add_contato, name='add_contato'),
    path('Listar_contato/', views.listar_contato, name='Listar_contato'),
    path('editarContato/<int:id>',views.editarContato, name='editarContato'),
    path('excluirContato/<int:id>',views.excluirContato, name='excluirContato'),
    path('buscar_contato/',views.buscar_contato, name='buscar_contato'),
]