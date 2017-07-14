from datetime import datetime
import hashlib
import hmac
import base64

from django.conf import settings
from django.shortcuts import render

from .constants import *
from .models import *


def index(request):
    return render(request, 'generic.html', {'heading': "perma-payments",
                                            'message': "a window to CyberSource Secure Acceptance Web/Mobile"})

def subscribe(request):
    s_agreement = SubscriptionAgreement(
        registrar=1,
        status='Pending'
    )
    s_agreement.save()
    s_request = SubscriptionRequest(
        subscription_agreement=s_agreement,
        amount=get_price(),
        recurring_amount=get_price(),
        recurring_frequency='monthly',
    )
    s_request.save()
    signed_fields = {
        'access_key': settings.CS_ACCESS_KEY,
        'amount': s_request.amount,
        'currency': s_request.currency,
        'locale': s_request.locale,
        'payment_method': s_request.payment_method,
        'profile_id': settings.CS_PROFILE_ID,
        'recurring_amount': s_request.recurring_amount,
        'recurring_frequency': s_request.recurring_frequency,
        'reference_number': s_request.reference_number,
        'signed_date_time': s_request.get_formatted_datetime(),
        'signed_field_names': '',
        'transaction_type': s_request.transaction_type,
        'transaction_uuid': s_request.transaction_uuid,
        'unsigned_field_names': '',

        # billing infomation
        'bill_to_forename': CS_TEST_CUSTOMER['first_name'],
        'bill_to_surname': CS_TEST_CUSTOMER['last_name'],
        'bill_to_email': CS_TEST_CUSTOMER['email'],
        'bill_to_address_line1': CS_TEST_CUSTOMER['street1'],
        'bill_to_address_city': CS_TEST_CUSTOMER['city'],
        'bill_to_address_state': CS_TEST_CUSTOMER['state'],
        'bill_to_address_postal_code': CS_TEST_CUSTOMER['postal_code'],
        'bill_to_address_country': CS_TEST_CUSTOMER['country'],
    }
    unsigned_fields = {}
    unsigned_fields.update(CS_TEST_CARD['visa'])
    signed_fields['signed_field_names'] = ','.join(sorted(signed_fields))
    signed_fields['unsigned_field_names'] = ','.join(sorted(unsigned_fields))
    data_to_sign = data_to_string(signed_fields)
    context = {}
    context.update(signed_fields)
    context.update(unsigned_fields)
    context['signature'] = sign_data(data_to_sign)
    context['heading'] = "Subscribe"
    context['post_to_url'] = CS_PAYMENT_URL[settings.CS_MODE]
    return render(request, 'subscribe.html', context)


def data_to_string(data):
    return ','.join('{}={}'.format(key, data[key]) for key in sorted(data))

def sign_data(data_string):
    """
    Sign with HMAC sha256 and base64 encode
    """
    message = bytes(data_string, 'utf-8')
    secret = bytes(settings.CS_SECRET_KEY, 'utf-8')
    hash = hmac.new(secret, message, hashlib.sha256)
    return base64.b64encode(hash.digest())

def get_price():
    """
    This should return the correct price for a customer.
    """
    return "1.00"
