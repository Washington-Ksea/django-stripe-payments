from django.urls import path

from payments import views

urlpatterns = [
    path('charge/', views.charge, name='charge'),
    path('', views.HomePageView.as_view(), name='home')
]