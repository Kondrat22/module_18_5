from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def index(request):
    return render(request, 'task2/index.html')

class index2(TemplateView):
    template_name = 'task2/index2.html'

