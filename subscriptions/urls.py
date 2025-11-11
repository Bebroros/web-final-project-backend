from django.urls import path
from subscriptions import views

urlpatterns = [
path('subs/', views.SubsList.as_view(), name='sub-list'),
    path('subs/<int:pk>/', views.SubsDetails.as_view(), name='sub-detail'),
]