# home/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# The 'from httpx import request' line is commented out and not used, so it's safe to remove.
# You don't need 'from httpx import request' unless you are specifically making HTTP requests using the httpx library.

# Create your views here.

def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')

@login_required
def profile(request):
    return render(request, 'home/profile.html')

@staff_member_required
def admin_dashboard(request):
    # Cleaned up: Removed the unreachable second return statement.
    # If you need to render product_management, you should do it conditionaly
    # or redirect there. For now, it will only render admin_dashboard.html.
    return render(request, 'home/admin_dashboard.html')

def product_management(request):
    return render(request, 'home/product_management.html')

# Add these NEW functions for Book Tickets and Basket:
def book_tickets_view(request):
    """ A placeholder view for the 'Book Tickets' page. """
    # You will eventually create a template named 'home/book_tickets.html'
    return render(request, 'home/book_tickets.html')

def view_basket_view(request):
    """ A placeholder view for the shopping basket/cart page. """
    # You will eventually create a template named 'home/basket.html'
    return render(request, 'home/basket.html')


# The bands_view and concerts_view are no longer linked from the navbar.
# If you still need these pages/views for other purposes, keep them.
# If not, and they are only served for the homepage buttons, you could keep them.
# I'll keep them here for completeness based on previous discussions,
# but they are not the cause of the current NoReverseMatch.
def bands_view(request):
    """ A view to display information about bands. """
    return render(request, 'home/bands.html')

def concerts_view(request):
    """ A view to display information about concerts. """
    return render(request, 'home/concerts.html')