from django.shortcuts import render


# Create your views here.
def platform(request):
    return render(request, 'task3/platform.html')
def shop(request):
    return render(request, 'task3/shop.html')
def bag(request):
    return render(request, 'task3/bag.html')