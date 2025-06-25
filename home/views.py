# home/views.py

from django.shortcuts import render, redirect, reverse # Ensure redirect and reverse are imported
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages # For displaying messages (like form success/error)

from .forms import TicketBookingForm # Make sure this import is correct based on your forms.py location

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
    Only one return statement is kept. If you need to show product_management,
    consider redirecting or rendering product_management.html based on conditions.
    """
    return render(request, 'home/admin_dashboard.html')

def product_management(request):
    """
    A view for product management related tasks.
    (Consider adding @staff_member_required if only staff should access this).
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

            # In a real application, you would save this to a database,
            # send confirmation email, process payment, etc.
            print(f"Booking {num_tickets} tickets for {email}") # For demonstration
            
            messages.success(request, f"Successfully requested {num_tickets} tickets for {email}! We've sent a confirmation to your email.")
            return redirect(reverse('book_tickets')) # Redirect to clear the form and show message
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
    This is where items added for purchase would typically be displayed.
    """
    return render(request, 'home/basket.html')

# --- Other Content Views (e.g., for direct band/concert pages) ---
# These are kept for completeness based on previous discussions,
# even if not currently linked from the main navbar.

def bands_view(request):
    """
    A view to display information about bands.
    """
    return render(request, 'home/bands.html')

def concerts_view(request):
    """
    A view to display information about concerts.
    """
    return render(request, 'home/concerts.html')