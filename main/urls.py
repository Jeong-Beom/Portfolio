from django.urls import path
from .views import base_views

app_name = 'main'

urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),
    path('portfolio_details/', base_views.portfolio_details, name='portfolio_details'),
    path('service_details/', base_views.service_details, name='service_details'),
    path('starter_page/', base_views.starter_page, name='starter_page'),
]