from django.urls import path, include
from apps.applications.views import PostCheckoutAPIView, PostContactUsAPIView, GetCheckoutAPIView, GetContactUsAPIView
from . import views

from rest_framework.routers import SimpleRouter

# router = SimpleRouter()
# router.register(r'checkout/', views.PostCheckoutAPIView.as_view(), basename='checkout')

urlpatterns = [
    # Checkout
    path('checkout_update/<int:pk>/', views.PostCheckoutAPIView.as_view(), name='post_checkout'),
    # Contact Us
    path('post_contact_us', views.PostContactUsAPIView.as_view(), name='post-contact-us'),
    path('get-contact-us', views.GetContactUsAPIView.as_view(), name='get-contact-us'),
]
# router = SimpleRouter()
# router.register('checkout/add', views.PostCheckoutAPIView, basename='checkout')

# urlpatterns += router.urls
