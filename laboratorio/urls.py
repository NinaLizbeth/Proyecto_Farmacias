from django.urls import path
from .views import inicio
from .views import (
    
    LaboratorioListView,
    LaboratorioCreateView,
    LaboratorioUpdateView,
    LaboratorioDeleteView,
)

app_name = 'laboratorio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('laboratorios/', LaboratorioListView.as_view(), name='list'),  
    path('laboratorios/create/', LaboratorioCreateView.as_view(), name='create'),
    path('laboratorios/update/<int:pk>/', LaboratorioUpdateView.as_view(), name='update'),
    path('laboratorios/delete/<int:pk>/', LaboratorioDeleteView.as_view(), name='delete'),
]

