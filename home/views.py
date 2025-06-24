from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from httpx import request

# Create your views here.

@login_required
def profile(request):
    return render(request, 'home/profile.html')


@staff_member_required
def admin_dashboard(request):
    return render(request, 'home/admin_dashboard.html')
    return render(request, 'home/product_management.html')

def product_management(request):
    return render(request, 'home/product_management.html')


def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html')
