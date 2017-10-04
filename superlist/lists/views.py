from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return render(template_name='home_page.html', request=request)

