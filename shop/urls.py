from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='shop-home'),
    path('chi-siamo/', views.about, name='shop-about'),
]

