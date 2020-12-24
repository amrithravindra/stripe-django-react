from django.shortcuts import render
import stripe
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
stripe.api_key = "sk_test_51HxEBgBt936UMiAM3pAjX7u7pfm15DLkwreaBdGQxMq7J1ZHcZEDpqlgzXxNunwCUk2cLrLlQKSztRNzDUL8g6bl00mCwJmAmA" # your real key will be much longer

@api_view(['POST'])
def test_payment(request):
    test_payment_intent = stripe.PaymentIntent.create(
        amount=1000, 
        currency='usd', 
        payment_method_types=['card'],
        receipt_email='test@example.com')
    return Response(status=status.HTTP_200_OK, data=test_payment_intent)