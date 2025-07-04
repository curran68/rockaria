from django.shortcuts import render

# Create your views here.

import stripe
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def create_checkout_session(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {'name': 'Sample Product'},
                'unit_amount': 1500,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/success/',
        cancel_url='http://localhost:8000/cancel/',
    )
    return JsonResponse({'id': session.id})

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
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print("✅ Payment successful:", session)

    return HttpResponse(status=200)

