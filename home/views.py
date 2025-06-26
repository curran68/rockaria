# home/views.py

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

# Correctly import the Band model from the 'bands' app
from bands.models import Band
from .forms import TicketBookingForm

# --- Core Views ---

def index(request):
    """
    A view to return the main homepage.
    """
    return render(request, 'home/index.html')

# --- User & Account Related Views ---

@login_required
def profile(request):
    """
    A view for authenticated users to see their profile.
    Requires user to be logged in.
    """
    return render(request, 'home/profile.html')

# --- Admin & Management Views ---

@staff_member_required
def admin_dashboard(request):
    """
    A view for staff members to access the admin dashboard.
    """
    return render(request, 'home/admin_dashboard.html')

def product_management(request):
    """
    A view for product management related tasks.
    """
    return render(request, 'home/product_management.html')

# --- Ticket Booking & Basket Views ---

def book_tickets_view(request):
    """
    View for displaying and processing the ticket booking form.
    Handles both GET (display empty form) and POST (process form submission).
    """
    if request.method == 'POST':
        form = TicketBookingForm(request.POST)
        if form.is_valid():
            num_tickets = form.cleaned_data['number_of_tickets']
            email = form.cleaned_data['email']

            print(f"Booking {num_tickets} tickets for {email}")
            messages.success(request, f"Successfully requested {num_tickets} tickets for {email}! We've sent a confirmation to your email.")
            return redirect(reverse('book_tickets'))
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = TicketBookingForm()

    context = {
        'form': form,
    }
    return render(request, 'home/book_tickets.html', context)


def view_basket_view(request):
    """
    A placeholder view for the shopping basket/cart page.
    """
    return render(request, 'home/basket.html')

# --- Other Content Views ---

def bands_view(request):
    """
    A view to display information about bands, fetched from the database.
    """
    bands = Band.objects.all() # Fetch all Band objects
    context = {
        'bands': bands # Pass the fetched bands to the template
    }
    return render(request, 'home/bands.html', context) # Render the bands.html template with the data

def concerts_view(request):
    """
    A view to display information about concerts.
    """
    return render(request, 'home/concerts.html')