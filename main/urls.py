from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('<str:faculty>/', views.spec),
    path('<str:spec>', views.hello)
]
