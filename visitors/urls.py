from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('checkout/<int:pk>/', views.visitor_checkout, name='visitor_checkout'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('export/', views.export_visitors_csv, name='export_visitors_csv'),

]
