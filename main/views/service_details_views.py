from django.shortcuts import render

def service_details_ltmetal(request):
    return render(request, 'main/service-details-ltmetal.html')

def service_details_samsungelectronics(request):
    return render(request, 'main/service-details-samsungelectronics.html')
    
def service_details_golfzon(request):
    return render(request, 'main/service-details-golfzon.html')