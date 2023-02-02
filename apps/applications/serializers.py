from rest_framework import serializers

from .models import Checkout, ContactUs


class CheckoutSerializer(serializers.ModelSerializer):
    """
    serializer for Checkout is:
    ('id', 'first_name', 'last_name', 'company_name', 'phone', 'email',
    'country', 'street_address', 'apartment_entrance', 'house', 'orders_notes')
    \nbased on default 'Checkout' model
    """

    class Meta:
        model = Checkout
        fields = ('id', 'uuid', 'first_name', 'last_name', 'company_name', 'phone', 'email',
                  'country', 'emirate', 'street_address', 'apartment_entrance', 'house', 'order_notes', 'order_id',
                  'choices'
                  )


class ContactUsSerializer(serializers.ModelSerializer):
    """
    serializer for ContactUs is:
    ('id', 'first_name', 'last_name', 'email',
    'phone_number', 'message')
    \nbased on default 'ContactUs' model
    """

    class Meta:
        model = ContactUs
        fields = ('id',
                  # 'first_name', 'last_name',
                  'email', 'full_name',
                  # 'phone_number',
                  'message')
