from django.urls import path
from horoscope import views

urlpatterns = [
    path('horoscope/', views.get_horoscope, name='get-prediction'),
]