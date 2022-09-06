from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'api', views.VacunaViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.VacunaCreateView.as_view(), name='create'),
    path('modificar/<int:pk>/', views.DetailView.as_view(), name='modificar'),
    path('update/<int:pk>/', views.VacunaUpdateView.as_view(), name='vacuna-update'),
    path('delete/<int:pk>/', views.delete, name='vacuna-delete'),

]

urlpatterns += router.urls