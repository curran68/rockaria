# home/views.py

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

# Correctly import the Band AND Concert model from the 'bands' app
from bands.models import Band, Concert # <-- Ensure Concert is imported here

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

import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def book_tickets_view(request):
    """
    Handles ticket booking and creates a Stripe Checkout session.
    """
    if request.method == 'POST':
        form = TicketBookingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            tickets = form.cleaned_data['number_of_tickets']
            total_cost = tickets * 2000  # £20 per ticket in pence

            # Create Stripe Checkout session
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                customer_email=email,
                line_items=[{
                    'price_data': {
                        'currency': 'gbp',
                        'unit_amount': total_cost,
                        'product_data': {
                            'name': f'Rockaria Ticket(s) x{tickets}',
                        },
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri('/booking/success/'),
                cancel_url=request.build_absolute_uri('/booking/cancel/'),
            )

            return redirect(checkout_session.url, code=303)
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
    A view to display information about concerts, fetched from the database.
    """
    concerts = Concert.objects.all().order_by('date') # Fetch all Concert objects, ordered by date
    context = {
        'concerts': concerts # Pass the fetched concerts to the template
    }
    return render(request, 'home/concerts.html', context) # Render the concerts.html template with the data