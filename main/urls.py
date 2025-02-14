from django.urls import path
from .views import base_views, portfolio_details_views, service_details_views

app_name = 'main'

urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),
    path('starter_page/', base_views.starter_page, name='starter_page'),

    # portfolio_details.views.py
    path('portfolio_details/pp1', portfolio_details_views.portfolio_details_pp1, name='portfolio_details_pp1'),
    path('portfolio_details/pp2', portfolio_details_views.portfolio_details_pp2, name='portfolio_details_pp2'),
    
    # service_details_views_py
    path('service_details/ltmetal', service_details_views.service_details_ltmetal, name='service_details_ltmetal'),
    path('service_details/samsungelectronics', service_details_views.service_details_samsungelectronics, name='service_details_samsungelectronics'),
    path('service_details/golfzon', service_details_views.service_details_golfzon, name='service_details_golfzon'),
]