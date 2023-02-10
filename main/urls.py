from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.main),
    path('<str:faculty>/', views.main),
    path('<str:faculty>/<str:spec>/', views.main),
    path('<str:faculty>/<str:spec>/<str:group>/', views.sched),
]
