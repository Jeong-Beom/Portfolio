from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def starter_page(request):
    return render(request, 'main/starter-page.html')