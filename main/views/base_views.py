from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def portfolio_details(request):
    return render(request, 'main/portfolio-details.html')

def service_details(request):
    return render(request, 'main/service-details.html')

def starter_page(request):
    return render(request, 'main/starter-page.html')