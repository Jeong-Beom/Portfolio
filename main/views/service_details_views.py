from django.shortcuts import render

def service_details_sample(request):
    return render(request, 'main/service-details-sample.html')
