from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.prediction, name='predict'),  # Fixed: 'views.prediction' instead of 'views.predict'
]
