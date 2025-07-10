# payments/views.py
import stripe
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect # Import render and redirect
from django.contrib import messages # For displaying messages to the user

# Set your secret key once, outside of your views
stripe.api_key = settings.STRIPE_SECRET_KEY

# --- View to render the page with the "Buy Now" button ---
def buy_product_view(request):
    # You might pass product details here if dynamic
    context = {
        'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY,
        'product_name': 'Rockaria Event Ticket',
        'price': '15.00', # For display purposes
    }
    return render(request, 'payments/buy_product.html', context)


# --- View to create the Stripe Checkout Session (your existing view) ---
@csrf_exempt # CSRF exempt for API endpoint, but ensure robust security
def create_checkout_session(request):
    # You would typically get product_id/amount from request.POST
    # and retrieve actual product/price from your database here for security
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'gbp', # Use your desired currency, e.g., 'gbp' for UK
                    'product_data': {'name': 'Rockaria Event Ticket'},
                    'unit_amount': 1500, # Amount in cents (15.00 GBP)
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/payments/success/'), # Use absolute URI
            cancel_url=request.build_absolute_uri('/payments/cancel/'),   # Use absolute URI
            # customer_email='user@example.com', # Optional: pre-fill customer email if logged in
            # client_reference_id='order_123', # Optional: Your internal order ID for reconciliation
        )
        return JsonResponse({'id': session.id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


# --- Stripe Webhook Endpoint (your existing view) ---
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except (ValueError, stripe.error.SignatureVerificationError):
        # Invalid payload or signature
        return HttpResponse(status=400)
    except Exception as e:
        # Handle other exceptions
        return HttpResponse(content=str(e), status=400)

    # Handle the event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print("✅ Payment successful (via Webhook):", session['id'])
        # TODO: Fulfill the order here.
        # - Update your database (mark order as paid, create ticket, etc.)
        # - Send confirmation email
        # - You can retrieve more details using session.customer, session.metadata, etc.
    elif event['type'] == 'checkout.session.async_payment_succeeded':
        session = event['data']['object']
        print("✅ Async Payment Succeeded (via Webhook):", session['id'])
        # Handle delayed payment success (e.g., SEPA Direct Debit)
    elif event['type'] == 'checkout.session.async_payment_failed':
        session = event['data']['object']
        print("❌ Async Payment Failed (via Webhook):", session['id'])
        # Handle delayed payment failure
    # Add other event types you want to handle
    else:
        print(f"Unhandled event type: {event['type']}")

    return HttpResponse(status=200)


# --- Success and Cancel Pages ---
def payment_success_view(request):
    # This view is hit when user is redirected after successful payment
    # NOTE: Do NOT fulfill orders here. Order fulfillment should happen in the webhook.
    # This is primarily for displaying a "Thank You" message.
    messages.success(request, "Your payment was successful! Thank you for your purchase.")
    return render(request, 'payments/payment_success.html')

def payment_cancel_view(request):
    messages.info(request, "Your payment was cancelled. You can try again.")
    return render(request, 'payments/payment_cancel.html')