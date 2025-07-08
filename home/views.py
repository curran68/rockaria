from django.shortcuts import render, redirect, reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.conf import settings
from django.contrib.messages import get_messages

import stripe

from bands.models import Band, Concert
from .forms import TicketBookingForm

stripe.api_key = settings.STRIPE_SECRET_KEY

# --- Homepage View ---
def index(request):
    """Render the main homepage."""
    return render(request, 'home/index.html')

# --- User & Account Views ---
@login_required
def profile(request):
    """Display the user's profile if authenticated."""
    return render(request, 'home/profile.html')

def custom_logout_view(request):
    """Log out the user and display a message."""
    logout(request)
    messages.info(request, "You have signed out.")
    return redirect('home')

# --- Staff/Admin Views ---
@staff_member_required
def admin_dashboard(request):
    """Dashboard for staff members."""
    return render(request, 'home/admin_dashboard.html')

def product_management(request):
    """Page for product-related admin tools."""
    return render(request, 'home/product_management.html')

# --- Ticket Booking Views ---
def book_tickets_view(request):
    """
    Handles ticket booking and Stripe Checkout session.
    Clears leftover messages from previous login/logout flow.
    """
    list(get_messages(request))  # 🧹 Consume any stale messages like "You have signed out"

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

    return render(request, 'home/book_tickets.html', {'form': form})

def view_basket_view(request):
    """Placeholder for user's basket/cart."""
    return render(request, 'home/basket.html')

# --- Band & Concert Views ---
def bands_view(request):
    """Display band information from the database."""
    bands = Band.objects.all()
    return render(request, 'home/bands.html', {'bands': bands})

def concerts_view(request):
    """Display concert info, sorted by date."""
    concerts = Concert.objects.all().order_by('date')
    return render(request, 'home/concerts.html', {'concerts': concerts})

def privacy_policy_view(request):
    return render(request, 'home/privacy.html')

def terms_view(request):
    return render(request, 'home/terms.html')

def contact_view(request):
    return render(request, 'home/contact.html')

def book_tickets(request, concert_id):
    concert = get_object_or_404(Concert, id=concert_id)
    # your form logic here
    return render(request, 'book_tickets.html', {'concert': concert})


